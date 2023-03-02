LogScale
```bash
#!/bin/bash

# Define the directories to remove
dirs_to_remove=(/opt/data /opt/data/kafka-data /home/vagrant)

# Loop through the directories and remove them if they exist with sudo permission
for dir in "${dirs_to_remove[@]}"
do
    if [ -d "$dir" ]
    then
        echo "WARNING: You are about to destroy $dir, which may affect any running Docker environments."
        read -p "Are you sure you want to continue? [y/n] " choice
        case "$choice" in 
            y|Y )
                echo "Removing $dir..."
                sudo rm -rf "$dir"
                ;;
            * )
                echo "Aborting script."
                exit 1
                ;;
        esac
    else
        echo "$dir does not exist."
    fi
done

# Verify that the directories have been removed
for dir in "${dirs_to_remove[@]}"
do
    if [ -d "$dir" ]
    then
        echo "Failed to remove $dir. Aborting script."
        exit 1
    fi
done

# Create new directories with sudo permission
echo "Creating new directories..."
sudo mkdir -p /opt/data/kafka-data /opt/data /home/vagrant

# Verify that the directories have been created
for dir in "${dirs_to_remove[@]}"
do
    if [ ! -d "$dir" ]
    then
        echo "Failed to create $dir. Aborting script."
        exit 1
    fi
done

echo "Directories have been removed and new directories have been created."

sudo docker run -d --restart-=always -v /opt/data:data -v /opt/data/kafaka-data:/kafka-data -v /home/vagrant:/etc/humio:ro --add-host ip-XXX-XX-X-XX.ec2.internal:127.0.0.1 --net-host --name=logscale --ulimit="nofile=8192:8192" --env-file=humio.conf humio/humio:stable

```

Shipper

```bash
sudo apt update -y
sudo apt upgrade -y
# Download FileBeat 
#https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation-configuration.html
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.6.2-amd64.deb
# Install FileBeat
sudo dpkg -i filebeat-8.6.2-amd64.deb
```

```yaml
filebeat.inputs:
- paths:
    - /var/log/traffic/*.log
  encoding: utf-8
  fields:
    aField: value

queue.mem:
  events: 8000
  flush.min_events: 1000
  flush.timeout: 1s

output:
  elasticsearch:
    hosts: ["http://192.168.86.27:8080/api/v1/ingest/elastic-bulk"]
    username: ANYTHING
    password: REPLACEME
    compression_level: 5
    bulk_max_size: 200
    worker: 5

setup.ilm.enabled: false
output.elasticsearch.allow_older_versions: true
```    

```bash
sudo systemctl enable filebeat
sudo systemctl restart filebeat
```

Direct the students through writing a bash script to split the austin traffic data.

```bash
#!/bin/bash

# Prompt the user to enter the path to the input file
read -p "Enter the path to the input file: " input_file

# Prompt the user to enter the path to the output directory
read -p "Enter the path to the output directory: " output_dir

# Get the total number of lines in the input file
total_lines=$(wc -l < "$input_file")

# Initialize a counter variable for the progress messages
count=0

# Loop through each line in the input file
while IFS= read -r line; do
  # Extract the date from the log line using two `cut` commands
  # The first `cut` command splits the line into fields separated by commas
  # The second `cut` command takes the second field (which contains the date and time)
  # and splits it into fields separated by spaces, then takes the first field (which
  # contains the date)
  date=$(echo "$line" | cut -d, -f2 | cut -d' ' -f1)

  # Convert the date to the ISO format used in the output directory structure
  iso_date=$(date -d"$date" "+%Y-%m")

  # Create the output directory if it doesn't exist
  mkdir -p "$output_dir/$iso_date"

  # Write the log line to the appropriate output file
  output_file="$output_dir/$iso_date/$iso_date_austin_traffic_log.log"
  echo "$line" >> "$output_file"

  # Increment the counter and display a progress message
  count=$((count+1))
  echo "Processed line $count of $total_lines"
done < "$input_file"

```

```bash
#!/bin/bash

# Set these variables to match your environment
HUMIO_HOST="192.168.86.27"
SENDER="ANYTHING"
INGEST_TOKEN="myingesttoken"
read -e -p "Enter the path to the directory housing ISO log folders: (e.g., /var/log/traffic/austin) " USER_DIR
# Loop through each directory in the "austin" directory
for dir in "$USER_DIR/*"; do
  if [[ -d "$dir" ]]; then
    # Extract the ISO date from the directory name
    iso_date=$(echo "$dir" | grep -Eo '[0-9]{4}-[0-9]{2}-[0-9]{2}')

    # Create a separate directory for the filebeat instance
    instance_dir="/opt/filebeat-$iso_date"
    mkdir -p "$instance_dir/logs"

    # Create the filebeat configuration file
    config_file="$instance_dir/filebeat.yml"
    cat <<EOF >"$config_file"
filebeat:
  inputs:
    - paths:
        - $dir/*.log
      fields:
        "@humioBackfill": "$iso_date"
        "@tags": ["@type", "@humioBackfill"]

queue.mem:
  events: 8000
  flush.min_events: 200
  flush.timeout: 1s

output:
  elasticsearch:
    hosts: ["http://$HUMIO_HOST:8080/api/v1/ingest/elastic-bulk"]
    username: $SENDER
    password: $INGEST_TOKEN
    compression_level: 5
    bulk_max_size: 200
    worker: 4
EOF

    # Launch filebeat in run-once mode for the current configuration file
    registry_dir="$instance_dir/registry"
    rm -rf "$registry_dir"
    filebeat -e --once \
      --path.config "$instance_dir" \
      --path.data "$instance_dir" \
      --path.home "$instance_dir" \
      --path.logs "$instance_dir/logs"
  fi
done
```
