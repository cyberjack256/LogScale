import csv

# Open the input file and create the output file
with open('input.csv', newline='') as infile, open('output.csv', 'w', newline='') as outfile:

    # Create a CSV reader and writer objects
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header row to the output file
    writer.writerow(['CRASH DATE', 'CRASH TIME', 'BOROUGH', 'ZIP CODE', 'LATITUDE', 'LONGITUDE', 'LOCATION', 'ON STREET NAME', 'CROSS STREET NAME', 'OFF STREET NAME', 'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED', 'NUMBER OF PEDESTRIANS KILLED', 'NUMBER OF CYCLIST INJURED', 'NUMBER OF CYCLIST KILLED', 'NUMBER OF MOTORIST INJURED', 'NUMBER OF MOTORIST KILLED', 'CONTRIBUTING FACTOR VEHICLE 1', 'CONTRIBUTING FACTOR VEHICLE 2', 'CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4', 'CONTRIBUTING FACTOR VEHICLE 5', 'UNIQUE KEY', 'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2', 'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5'])

    # Loop through each row in the input file
    for row in reader:

        # Replace the empty values with "EMPTY"
        for i in range(len(row)):
            if not row[i]:
                row[i] = "EMPTY"

        # Write the updated row to the output file
        writer.writerow(row)
