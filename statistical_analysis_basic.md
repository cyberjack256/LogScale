
# General Statistics Concepts to Conduct Analysis in LogScale

### Mean

The mean is the average value of a set of data. It is calculated by summing all of the values and dividing by the number of values.

To calculate the mean (average) of a field in LogScale, you can use the stats avg(field) as mean operator in your query. This operator will calculate the mean of the values in the field field and store the result in the mean field.

For example, to calculate the mean of the sales field in the sales dataset, you can use the following query:

```sql
| stats avg(field) as mean
```

This query will calculate the mean of the field and display the result in a table.

You can also use the stats avg(field) operator without the as mean clause to obtain the mean of the field field, but in this case the resulting field will be named avg(field) instead of mean.

You can modify this query as needed to match your specific dataset and field, and you can use it to calculate the mean for any time range or filters that you specify. LogScale will automatically perform the calculations in real-time as you run the query, so you can quickly and easily obtain the mean for your data.

### Median

The median is the middle value of a set of data when the values are arranged in numerical order.

```sql
| sort field
| eval middle = (count() + 1) / 2
| table field[round(middle)] as median
```

This query will sort the values in the field field in ascending order, then use the eval operator to calculate the index of the middle value (the median). It will use the table operator to display the value of the field field at the middle index, which will be the median.

For example, to calculate the median of the sales field in the sales dataset, you can use the following query:

```sql
| sort sales
| eval middle = (count() + 1) / 2
| table sales[round(middle)] as median

```

### Mode

The mode is the most frequently occurring value in a set of data.

To find the mode of a field in a LogScale query, you can use the mode() function. For example, to find the mode of the {field} field in the {dataset} dataset, you could use the following query which filters out any null values for the {field} field, and then calculates the mode (and optionally, mean) of the remaining values using the mode() (optionally mean()) function. The result will be a single|double value that represents the mode|mean of the {field} field.

```sql
| stats count(product_category) as count by product_category
| sort -count
| head 1
| table product_category as mode
```

This query will use the stats operator to count the number of occurrences of each value in the product_category field, then use the sort operator to sort the results in descending order by count. It will use the head operator to select the top result (the value with the highest count), and it will use the table operator to display the value of the product_category field for the top result, which will be the mode.

**Note** this query may return multiple values if there are multiple modes in the data (i.e. if there are two or more values that occur with the highest frequency). In this case, the mode() function will return all of the modes as an array.


### Range

The range is the difference between the highest and lowest values in a set of data.

To find the range of a field in a LogScale query, you can use the `max()` and `min()` functions to find the highest and lowest values, and then subtract the minimum value from the maximum value.

For example, to find the range of the `{field}` field in the `{dataset}` dataset, you could use the following query:

TODO: Calculate Range
```sql
| where {field} != null
| stats max({field}) as max, min({field}) as min
| eval range = max - min
```

This query filters out any null values for the {field} field, and then calculates the maximum and minimum values using the max() and min() functions. It then uses the eval operator to calculate the range by subtracting the minimum value from the maximum value. The result will be a single row with three columns: max, which contains the maximum value of the {field} field, min, which contains the minimum value of the {field} field, and range, which contains the range of the {field} field

You can also use the max(), min(), and eval operators in combination with other functions to perform more complex analyses. For example, you could use the bucket operator to group the data by a specific interval, and then use the max(), min(), and eval operators to find the range within each interval. You could also use the where operator to filter the data based on specific conditions, and then use the max(), min(), and eval operators to find the range of the remaining data.

### Variance

The variance is a measure of the spread or dispersion of a set of data. It is calculated by taking the sum of the squared differences between each value and the mean, and dividing by the number of values.

To find the variance of a field in a LogScale query, you can use the variance() function

```sql
| where {field} != null
| stats sum((({field} - avg({field}))^2)) as variance
| eval variance = variance / count()
```

This equation calculates the variance of the {field} field in the {dataset} by summing the squared differences between each value and the mean, and dividing by the number of values.

The sum() function is used to sum the squared differences between each value and the mean, which are calculated using the ({field} - avg({field}))^2 expression. The avg() function is used to calculate the mean of the {field} field, and the ({field} - avg({field})) expression calculates the difference between each value and the mean. The ^2 operator raises the result to the power of 2, which squares the differences. The sum() function then sums the squared differences to get the sum of the squared differences.

The eval operator is then used to divide the sum of the squared differences by the number of values using the variance = variance / count() expression. The count() function returns the number of values in the {field} field. The result is stored in a new field called variance, which represents the variance of the {field} field.

You can then use the variance field in your query to analyze the dispersion of the data around the mean. For example, you could use the where operator to filter the data based on the variance, or you could use the display operator to visualize the variance in a chart or graph.


#### Variance Example

Imagine that you are working for an insurance company, and you have been asked to analyze multiple datasets to identify trends or patterns in fraud claims that could help the company optimize its fraud detection processes. You have data on the amount of time it takes to process different types of fraud claims, and you want to use variance to identify which types of claims take the longest to process and which types of claims take the shortest to process.

To do this, you can use the variance() function in a LogScale query to calculate the variance of the time it takes to process different types of fraud claims. For example, you might use the following LogScale query to calculate the variance of the time it takes to process different types of fraud claims:

```sql
| where time_to_process != null and claim_type != null
| bucket claim_type
| stats sum(((time_to_process - avg(time_to_process))^2)) as variance
| eval variance = variance / count()
```

This query will calculate the variance of the time_to_process field in the fraud_claims dataset and display the variance for each claim_type. It will only include data from the fraud_claims table where the time_to_process and claim_type fields are not null.

It will use the stats operator to calculate the sum of the squares of the difference between each value of time_to_process and the mean of time_to_process (variance), and it will use the eval operator to divide the variance field by the total number of data points (count()) to obtain the variance. Finally, it will use the bucket operator to group the results by the claim_type field, and it will use the table operator to display the resulting values of the variance field for each claim_type.

This query will allow you to calculate the variance of the time_to_process field in the fraud_claims dataset, without using the variance() function, and it will only include data from the fraud_claims table where the time_to_process and claim_type fields are not null. It will also bucket the results by the claim_type field and display the variance for each claim_type.

You can then use the variance values to identify which types of fraud claims take the longest to process and which types of fraud claims take the shortest to process. For example, if you see that the variance of the time_to_process field is high for a particular group, it could indicate that the time it takes to process claims in that group is more variable and therefore more difficult to predict. This could be a sign that the company's fraud detection processes are less efficient for that type of claim, and that improvements could be made to optimize the process.

Using variance in this way can be a useful way to analyze multiple datasets and identify trends or patterns that could help the company optimize its fraud detection processes. It can help you identify which types of fraud claims are more difficult to process.

### Standard Deviation:
The standard deviation is a measure of the spread or dispersion of a set of data. It is calculated by taking the square root of the variance.

To find the standard deviation of a field in a LogScale query, you can use the stddev() function. For example, to find the standard deviation of the {field} field in the {dataset} dataset, you could use the following query:

```sql
| where {field} != null
| stats stddev({field}) as stddev
```

This query filters out any null values for the {field} field, and then calculates the standard deviation of the remaining values using the stddev() function. The result will be a single value that represents the standard deviation of the {field} field.

You can also use the stddev() function in combination with other functions to perform more complex analyses. For example, you could use the bucket operator to group the data by a specific interval, and then use the stddev() function to find the standard deviation within each interval. You could also use the where operator to filter the data based on specific conditions, and then use the stddev() function to find the standard deviation of the remaining data.

**Note** that the stddev() function calculates the sample standard deviation, which is a measure of the spread or dispersion of a sample of data. If you want to calculate the population standard deviation, you can use the pstddev() function instead. The population standard deviation is a measure of the spread or dispersion of an entire population of data.

#### Standard Deviation Example:

Imagine that you are working for a manufacturing company, and you have been asked to analyze the data on the production of different parts to identify trends or patterns that could help the company optimize its production processes. You have data on the size of different parts and the time it takes to produce each part, and you want to use standard deviation to identify which parts have the most variable size and production time.

To do this, you can use the stddev() function in a LogScale query to calculate the standard deviation of the size and production time of different parts. For example, you might use the following LogScale query to calculate the standard deviation of the size of different parts:

```sql
| where part_size != null and part_type != null
| bucket part_type
| stats stddev(part_size) as stddev
```
This query filters out any rows where either the part_size or part_type field is null, and then groups the data by the part_type field using the bucket operator. It then calculates the standard deviation of the part_size field within each group using the stddev() function. The result will be a series of rows, one for each group, with two columns: part_type, which contains the group name, and stddev, which contains the standard deviation of the part_size field within the group.

You can then use the standard deviation values to identify which parts have the most variable size. For example, if you see that the standard deviation of the part_size field is high for a particular group, it could indicate that the size of parts in that group is more variable and therefore more difficult to predict. This could be a sign that the company's production processes are less efficient for that type of part, and that improvements could be made to optimize the process.

You can repeat this process to calculate the standard deviation of the production time for different parts, and use the standard deviation values to identify which parts have the most variable production time. Using standard deviation in this way can be a useful way to analyze manufacturing datasets and identify trends or patterns that could help the company optimize its production processes. It can help you identify which parts are more difficult to produce and which parts are easier to produce, and can help you optimize your production schedule to maximize efficiency and reduce costs.

### Correlation

Correlation is a statistical measure that describes the relationship between two variables. A positive correlation means that the variables are directly related (i.e. when one variable increases, the other variable also increases), while a negative correlation means that the variables are inversely related (i.e. when one variable increases, the other variable decreases).

To find the statistical correlation between two fields in a LogScale query, you can use the corr() function. The corr() function calculates the Pearson correlation coefficient, which is a measure of the linear relationship between two variables. A Pearson correlation coefficient of 1 indicates a strong positive correlation, a Pearson correlation coefficient of -1 indicates a strong negative correlation, and a Pearson correlation coefficient of 0 indicates no correlation.

For example, to find the Pearson correlation coefficient between the {field1} field and the {field2} field in the {dataset} dataset, you could use the following query:

```sql
| where {field1} != null and {field2} != null
| stats sum(field1 * field2) as sum_xy, sum(field1) as sum_x, sum(field2) as sum_y, sum(field1^2) as sum_x2, sum(field2^2) as sum_y2, count() as n by _source
| eval r = sum_xy - (sum_x * sum_y) / n, d = (sum_x2 - (sum_x^2) / n) * (sum_y2 - (sum_y^2) / n)
| eval r = r / sqrt(d)
| table r
```

This query filters out any rows where either {field1} or {field2} is null, and then calculates the Pearson correlation coefficient between {field1} and {field2} using the corr() function. The result will be a single value that represents the Pearson correlation coefficient between {field1} and {field2}.

You can also use the corr() function in combination with other functions to perform more complex analyses. For example, you could use the bucket operator to group the data by a specific interval, and then use the corr() function to find the correlation between {field1} and {field2} within each interval.

#### Correlation Example:

Imagine that you are working for a company that sells outdoor gear, and you have been asked to analyze the sales data for different product categories. You have data on the sales of different types of tents, sleeping bags, and backpacks, and you want to see if there is a relationship between the sales of these different product categories.

To do this, you can use the Pearson correlation coefficient to measure the linear relationship between the sales of different product categories. For example, you might use the following LogScale query to calculate the Pearson correlation coefficient between the sales of tents and sleeping bags:

```sql
| where product_category = "tent" or product_category = "sleeping_bag"
| stats sum(sales * product_category) as sum_xy, sum(sales) as sum_x, sum(product_category) as sum_y, sum(sales^2) as sum_x2, sum(product_category^2) as sum_y2, count() as n
| eval r = sum_xy - (sum_x * sum_y) / n, d = (sum_x2 - (sum_x^2) / n) * (sum_y2 - (sum_y^2) / n)
| eval correlation = r / sqrt(d)
| table correlation
```

This query will calculate the Pearson correlation coefficient between the sales and product_category fields in the dataset. It will use the formula for the Pearson correlation coefficient to perform the calculation. The resulting value of the correlation coefficient will be displayed in a table under the correlation column.

This query will only include data from the sales table where the product_category field is either "tent" or "sleeping_bag". It will use the stats operator to calculate the sum of the product of sales and product_category (sum_xy), the sum of sales (sum_x), the sum of product_category (sum_y), the sum of the squares of sales (sum_x2), the sum of the squares of product_category (sum_y2), and the total number of data points (n). It will then use the eval operator to calculate the Pearson correlation coefficient r and the value of d, and it will divide r by the square root of d to normalize the result and store it in the correlation field. Finally, it will use the table operator to display the resulting value of the correlation field.

This query will allow you to calculate the Pearson correlation coefficient between the sales and product_category fields in the dataset, and it will only include data from the sales table where the product_category field is either "tent" or "sleeping_bag". 

You can repeat this process to calculate the Pearson correlation coefficient between the sales of other product categories, such as backpacks and sleeping bags, or tents and backpacks. This will allow you to see if there is a strong positive or negative correlation between the sales of different product categories, and can help you identify any trends or patterns in the data.

Using the Pearson correlation coefficient can be a useful way to analyze data when you want to see if there is a linear relationship between two variables. It can be particularly useful when you are data mining.

### Regression
Regression is a statistical method that is used to model the relationship between a dependent variable and one or more independent variables. It involves fitting a line or curve to the data that best represents the relationship between the variables.

To find statistical regression in a LogScale query, you can use the regression() function. The regression() function calculates the least squares regression line for a set of data, which is a statistical method used to model the relationship between a dependent variable and one or more independent variables. The regression line is a line that best fits the data, and is used to make predictions about future trends or patterns based on the data.

For example, to find the least squares regression line for the {field1} field and the {field2} field in the {dataset} dataset, you could use the following query:

```sql
| where {field1} != null and {field2} != null
| stats sum(field1 * field2) as sum_xy, sum(field1) as sum_x, sum(field2) as sum_y, sum(field1^2) as sum_x2, count() as n
| eval slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x^2), intercept = (sum_y - slope * sum_x) / n
| table slope, intercept
```

This query will calculate the slope and intercept of the least squares regression line for the field1 and field2 fields in the dataset. It uses the stats operator to calculate the sum of the product of field1 and field2 (sum_xy), the sum of field1 (sum_x), the sum of field2 (sum_y), the sum of the squares of field1 (sum_x2), and the total number of data points (n). It then uses the eval operator to calculate the slope and intercept of the regression line using the least squares method, and it stores the results in the slope and intercept fields. Finally, it uses the table operator to display the resulting values of the slope and intercept fields.


Using the equation to calculate regression can be a useful way to analyze data when you want to model the relationship between two variables and make predictions about future trends or patterns based on the data. It can be particularly useful when you are data mining and trying to identify patterns or trends in the data that could help inform business decisions.

#### Regression Example:

Imagine that you are working for a company that operates a fleet of vehicles, and you have been asked to analyze the data on the maintenance history of the vehicles to identify trends or patterns that could inform preventative maintenance practices. You have data on the number of miles driven by each vehicle and the number of maintenance events that have occurred for each vehicle, and you want to use statistical regression to model the relationship between these variables and make predictions about future maintenance events.

To do this, you can use the regression() function in a LogScale query to calculate the least squares regression line for the data. For example, you might use the following LogScale query to calculate the regression line for the number of miles driven and the number of maintenance events:

```sql
| where miles_driven != null and maintenance_events != null
| stats sum(miles_driven * maintenance_events) as sum_xy, sum(miles_driven) as sum_x, sum(maintenance_events) as sum_y, sum(miles_driven^2) as sum_x2, count() as n
| eval slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x^2), intercept = (sum_y - slope * sum_x) / n
| table slope, intercept
```

This query filters out any rows where either the miles_driven or maintenance_events field is null, and then calculates the least squares regression line between the miles_driven field and the maintenance_events field using the regression() function. The result will be a single value that represents the regression line for the data.

You can then use the regression line to make predictions about future maintenance events based on the number of miles driven by a vehicle. For example, if you know that a vehicle has driven 75,000 miles and you want to predict how many maintenance events it will need in the future, you can use the regression line to estimate the number of maintenance events based on the number of miles driven.

Using statistical regression in this way can be a useful way to analyze data and make predictions about future outcomes when you are conducting analysis for preventative maintenance. It can help you identify trends or patterns in the data that could inform your preventative maintenance practices, and can help you optimize your maintenance schedule to minimize downtime and reduce costs.

## Summary

These concepts can be used to summarize and describe the characteristics of a dataset, as well as to analyze the relationships between variables and make predictions or inferences about future trends or patterns.





## Work in Progress (Outliers with most commonly used methods Z Score and IQR)


TODO: Example for finding outliers using IQR
```sql
from {datasource}
where {field} is not null
  | count() as {field}_count
  | min({field}) as {field}_min
  | max({field}) as {field}_max
  | percentile({field}, 0.25) as {field}_p25
  | percentile({field}, 0.75) as {field}_p75
  | {field}_p75 - {field}_p25 as {field}_iqr
  | ({field}_p75 + (1.5 * {field}_iqr)) as {field}_upper_whisker
  | ({field}_p25 - (1.5 * {field}_iqr)) as {field}_lower_whisker
  | filter({field} > {field}_upper_whisker or {field} < {field}_lower_whisker)
  | count() as {field}_outliers
```
This query calculates summary statistics for the specified field (such as the count, minimum, maximum, and quartiles) and uses these values to identify outliers using the interquartile range (IQR) to create outlier fences. Outliers are defined as values that are more than 1.5 times the IQR above the upper quartile or below the lower quartile.

To use this query, you will need to replace {datasource} with the name of the data source that you want to analyze and {field} with the name of the field that you want to find outliers in. The query will return a count of the number of outliers that were found in the field.

TODO: example using Z score and standard deviation to find outliers

```sql
| from {dataset}
| where {field} != null
| bucket {field} by {interval}
| stats avg({field}) as avg, stddev({field}) as stddev
| join (
  | from {dataset}
  | where {field} != null
  | bucket {field} by {interval}
  | stats {field} as value
) on bucket
| where value > (avg + {n} * stddev) or value < (avg - {n} * stddev)
| project bucket, value
```

In this query, you will need to replace {dataset} with the name of the dataset that you want to analyze, {field} with the name of the field that you want to find outliers in, {interval} with the interval that you want to use to group the data (e.g. 1m, 1h, 1d, etc.), and {n} with the number of standard deviations that you want to use as the threshold for identifying outliers.

This query first groups the data by the specified interval and calculates the average and standard deviation of the {field} values. It then joins this data with the original data, filtering for only those {field} values that are outside of the specified number of standard deviations from the average. Finally, it projects the resulting data, showing the interval and the outlier values.

By running this query, you can identify any values that are significantly different from the rest of the data, which may indicate an outlier. You can then further investigate these values to understand why they are different and whether they are indicative of any underlying issues or patterns in the data.




## References for Labs:

### Dataset for Non-Alcoholic Drinks by Product Type with Analysis and Forecast 2022-2031
Non-alcoholic Drinks Market by Product Type (Soft Drinks, Premium Water, Tea & Coffee, Juice, Dairy Drinks, and Others), DistributionChannel (Supermarket/Hypermarket, Convenience Stores, Specialty Stores, Online Retails, and Others), and Price Point (Standard, Premium, and Luxury): Global Opportunity Analysis and Industry Forecast, 2022-2031

https://www.alliedmarketresearch.com/non-alcoholic-drinks-market # Can download the dataset in csv


### Recent News Article Showing the Power of Pearson's Coefficient Correlation to Determine Sales Outcomes
A golden age for nonalcoholic beers, wines and spirits pearson correlation coefficient
https://www.npr.org/sections/money/2023/01/03/1144621641/nonalcoholic-beer-wine-spirits-dry-january