# Learning LogScale with Dashboards

This repository contains a series of LogScale dashboards created for educational purposes. Each dashboard focuses on specific aspects of LogScale syntax and functionality, including aggregation commands, joins, match, arrays, filter, and case statements. These dashboards and associated widgets are created using LogScale version 1.88 stable.

## Structure of the Repository

Each dashboard in this repository covers a main topic and contains a set of widgets each covering subtopics. The main topics are:

- Aggregation Commands
- Arrays
- Filtering
- Filtering with Case Statements
- Filtering with the match() Function
- Join Functions
- Match Enrichment
- Parsing Functions
- Regular Expressions
- Times Dates and Time Zones

Dashboards and widgets are named using a consistent naming scheme: `MainTopic_Subtopic_WidgetName`. For example, `AggregationCommands_AgeAnalysis`. This structure allows for easy navigation and understanding of the content.

No actual data ingestion is performed for these dashboards. Instead, we use the createevents() function which generates sample event data for the query examples.

## Installation and Usage

### Install a Package from a File

1. Go to the Marketplace under the Settings tab in your view.
2. Go to Installed packages list under the Settings tab.
3. Click the Upload button. 
4. Drag and drop a package from your machine or use the file selector to navigate and choose a package Zip file from your local machine. For example, `Learning_LogScale_Dashboards.zip`.
5. You will be presented with a summary of the components that will be installed when the package has been added to your system.
6. Click the Install button to install the package. Click the Cancel button to return to the package summary.
7. Once the package has been installed, it will appear under the Packages → Installed section of the Settings tab.

For updating an existing package, follow the same steps but click "Update" instead of "Install".

You can also install or update packages using CLI with humioctl or GraphQL as shown in the LogScale documentation.

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## Disclaimer

Please note that these dashboards are for educational purposes only. Make sure to comply with all data privacy regulations and policies when using real data.
