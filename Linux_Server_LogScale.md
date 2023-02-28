OS-Setup

From a BASH terminal, add the necessary repository (The version of Docker found in the standard repository isn't the latest Community Edition). 


1. Patch the OS and install the necessary dependencies
```bash
# Update and upgrade the OS
sudo apt update -y && sudo apt upgrade -y
# Install dependencies 
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release -y
```

2. Add the official Docker repository:
```bash
# Add the official Docker GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
#Add the official Docker repository
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
3. Install Docker
```bash
sudo apt install docker.io -y
```

4. Add the admin user to the docker group if not running as root

```bash
sudo usermod -aG docker #<name of the user>
```

1. Create two directories on the host machine: one to store data for Falcon LogScale in general and one for Kafka data. Pull the latest Humio image

```bash
# Create the directories
sudo mkdir -p /opt/logscale/mounts/data /opt/logscale/mounts/kafka-data /opt/logscale/ro
# Pull latest image of LogScale
docker pull humio/humio:latest
```


Within a BASH terminal, execute the command to 
```shell

# Set variables for the host data directory, Kafka data directory, and path to read-only files
HOST_DATA_DIR=/opt/logscale/mounts/data
HOST_KAFKA_DATA_DIR=/opt/logscale/mounts/kafka-data
PATH_TO_READONLY_FILES=/opt/logscale/ro
PATH_TO_CONFIG_FILE=/opt/logscale/humio.conf

# Start a Humio Docker container and map the specified directories
# The -v option is used to map a host directory to a directory in the Docker container
# The :ro option specifies that the mapped directory should be read-only in the container
# The --net=host option specifies that the container should use the host's network stack
# The --name option specifies a name for the container
# The --ulimit option sets resource limits for the container
# The --stop-timeout option specifies the time to wait for the container to stop before killing it
# The --env-file option specifies a file containing environment variables to set in the container
docker run -d -v $HOST_DATA_DIR:/data -v $HOST_KAFKA_DATA_DIR:/data/kafka-data -v $PATH_TO_READONLY_FILES:/etc/humio:ro --net=host --name=humio --ulimit="nofile=8192:8192" --stop-timeout 300 --env-file=$PATH_TO_CONFIG_FILE humio/humio:latest
```

