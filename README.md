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

# NYC_WIDGET_ANALYSIS - Learning Collisions Data Visualization

## Description
The NYC_WIDGET_ANALYSIS package is designed as a learning tool for individuals interested in data visualization. It employs a dataset centered around New York City collisions to provide examples of how different types of widgets can be utilized to effectively display and analyze data.

## Visualization
This package showcases various types of widgets, including but not limited to tables, bar graphs, line charts, and scatter plots. These widgets aim to demonstrate different ways of representing and interpreting data visually.

## Understanding the Data
While the dataset revolves around New York City collisions, the focus is not on the data itself, but rather on the methods used to visualize it. The data includes variables like borough, year, month, day, hour, total injured, and total fatalities. These variables are used to create diverse and complex visualizations.

## How to Use
This package is designed primarily for aspiring data scientists and anyone interested in data visualization. Users are encouraged to inspect the queries used to generate each widget and learn how to create different types of visualizations. Each query showcases different techniques and methods, making this package a valuable resource for learning and inspiration.

# NYC_HOURLY - Historical Context of Collisions by Hour of Day

## Description
The NYC_HOURLY package offers a comprehensive dashboard to visualize and understand the historical context of collisions in New York City segmented by hour of the day. This package not only provides the average number of injuries and fatalities per hour but also their standard deviations and the coefficient of variation (CV). 

## Visualization
Data is represented in a tabular format for quick and easy understanding. Each row of the table corresponds to a particular hour of the day (in 24-hour format), making it easy to interpret the information.

## Understanding the Data
The data has several columns, each revealing a different aspect of the collisions:

- **hour**: This signifies the hour of the day (in 24-hour format) when the collision occurred.
- **avg_injured**: This signifies the average number of people injured in collisions during each hour of the day.
- **std_total_injured**: This indicates the standard deviation of the number of people injured during each hour, showing the variability of this number across the day.
- **avg_fatality**: This indicates the average number of fatalities in collisions during each hour of the day.
- **std_total_fatality**: This shows the standard deviation of the number of fatalities, indicating the variability of fatalities throughout the day.
- **cv_injured** and **cv_fatality**: These represent the coefficients of variation for the number of people injured and the number of fatalities, respectively. These numbers help us understand the relative variability of these figures.

## How to Use
This package offers valuable insights for various entities like traffic authorities, city planners, and insurance companies, providing a detailed understanding of collision occurrences during different hours of the day. Researchers in the field of urban planning and traffic safety can also benefit from this dashboard.

# NYC_WEEKDAY - Historical Context of Collisions by Day of Week

## Description
This package provides a detailed data dashboard representing historical context of collisions in New York City categorized by each day of the week. The data not only shows the average number of people injured and killed in car accidents for each day, but also the standard deviation and the coefficient of variation (CV), offering a thorough understanding of collision incidents from a day-of-week perspective.

## Visualization
The package visualizes data in a tabular format, facilitating quick and intuitive comprehension of complex data sets. Days are represented as numbers (from 0 for Sunday to 6 for Saturday) for simplicity.

## Understanding the Data
The data contains several columns, each representing a different aspect of the collisions:

- **weekday**: The day of the week (0-6, with "0" being Sunday, "1" being Monday, and so on, up to "6" for Saturday)
- **avg_injured**: The average number of people injured in accidents on each day of the week
- **std_total_injured**: The standard deviation of the number of people injured, indicating the variability of this number on each day
- **avg_fatality**: The average number of fatalities in accidents on each day of the week
- **std_total_fatality**: The standard deviation of the number of fatalities, showing the variability of fatalities on each day
- **cv_injured** and **cv_fatality**: The coefficients of variation for the number of people injured and the number of fatalities, respectively. These figures help to understand the relative variability of these figures.

## How to Use
This dashboard can be utilized to analyze and predict the risk associated with different days of the week. It can be beneficial for traffic authorities, city planners, insurance companies, and researchers studying traffic safety and urban planning.



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
