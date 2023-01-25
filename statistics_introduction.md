# An Introduction to Statistics

## I. Data Types (5 minutes)

Definition: The types of data that can be collected and analyzed in statistics
Examples: Categorical, numerical

Scenario: A baker is interested in collecting data on the types of pastries that customers at their bakery purchase. They create a survey with the following options: muffins, scones, croissants, danishes. The data collected from the survey would be categorical data because the pastries cannot be ordered or ranked.

## II. Categorical Data (10 minutes)

Definition: Data that can be placed into categories, but cannot be ordered or ranked
Types: Nominal, ordinal
Examples: Type of pastry (muffin, scone, croissant, danish), type of bread (sourdough, whole wheat, rye), type of cookie (chocolate chip, oatmeal raisin, snickerdoodle)

Scenario: A baker is interested in determining whether there is a relationship between the type of flour used in a recipe and the resulting texture of the baked goods. They create a survey with the following options for flour type: all-purpose, whole wheat, almond, coconut. The data collected from the survey would be nominal data because the flour types do not have an inherent order.

Scenario: A baker is interested in determining whether there is a relationship between the baking time of a recipe and the resulting texture of the baked goods. They create a survey with the following options for baking time: underbaked, perfectly baked, overbaked. The data collected from the survey would be ordinal data because the baking times have a clear order (underbaked < perfectly baked < overbaked).


## III. Numerical Data (10 minutes)

Definition: Data that can be measured or counted
Types: Discrete, continuous
Examples: Number of pastries sold per day, weight of a loaf of bread, diameter of a cake

Scenario: A baker is interested in determining whether there is a relationship between the amount of sugar used in a recipe and the sweetness of the resulting baked goods. They create a survey with a question asking customers to rate the sweetness of the baked goods on a scale from 1 (not sweet) to 10 (very sweet). The data collected from the survey would be continuous numerical data because the sweetness can be measured on an infinite scale.

Scenario: A baker is interested in determining how many of each type of pastry they sell at their bakery each day. They keep track of the number of muffins, scones, croissants, and danishes sold every day for a week. The data collected would be discrete numerical data because the number of pastries sold can only take on integer values (e.g. 4 muffins, not 4.5 muffins).

## IV. Proportions (5 minutes)

Definition: A ratio that expresses the number of times a condition or occurrence is present in a given sample
Examples: Percentages, fractions

Scenario: Proportions are often used with categorical data, particularly ordinal data, to express the number or frequency of times a particular category or value is present in a sample. For example, if a bake shop surveyed 100 customers and found that 60 of them preferred muffins, the proportion of customers who preferred muffins would be 60/100 = 0.6, or 60%.

Scenario: Numerical data, on the other hand, can be used to calculate proportions, but it is not considered a proportion in and of itself. For example, if a bake shop tracked the number of pastries sold per day for a week, the numbers themselves (e.g. 35 pastries sold on Monday) would be numerical data, but they could be used to calculate proportions (e.g. 35/100 = 0.35, or 35% of the pastries sold that week were sold on Monday).


## V. Distributions (10 minutes)

Definition: The pattern in which data is distributed or arranged
Examples: Normal distribution, binomial distribution

Scenario: A baker is interested in determining the distribution of sweetness ratings for their baked goods. They survey 100 customers and create a histogram showing the frequency of each rating. If the histogram is bell-shaped and symmetrical, it is likely that the data follows a normal distribution.

Scenario: A baker is interested in determining the probability of a batch of cookies turning out perfectly baked. They know that the probability of a single cookie turning out perfectly baked is 0.8 (80%). They can use the binomial distribution to calculate the probability of getting a certain number of perfectly baked cookies in a batch of 10 cookies.

## VI. Sampling and Estimation (5 minutes)

Definition: The process of selecting a subset of data from a larger population to draw conclusions about the population as a whole
Examples: Random sampling, stratified sampling

Scenario: A baker wants to estimate the proportion of customers who prefer muffins to other pastries at their bakery. They randomly select a sample of 50 customers and find that 30 of them prefer muffins. They can use this sample to estimate that the proportion of all customers who prefer muffins is 30/50 = 0.6, or 60%.

Scenario: A baker wants to estimate the proportion of customers who prefer muffins to other pastries at their bakery, but they want to make sure that their sample is representative of the entire population of customers. They stratify their sample by gender and age, and ensure that their sample includes the same proportion of males and females and the same proportion of age groups as the overall population of customers.

## VII. Hypothesis Testing (5 minutes)

Definition: The process of evaluating statistical evidence to determine whether a hypothesis is true or false
Examples: Z-tests, t-tests, ANOVA

Z-test: A statistical test used to compare the mean of a sample to a known population mean. For example, a baker may use a Z-test to determine whether the average texture rating of their croissants (based on a sample of customers) is significantly different from the average rating for all croissants (the known population mean).

t-test: A statistical test used to compare the means of two samples. For example, a baker may use a t-test to determine whether the average texture rating of their croissants made with butter (based on a sample of customers) is significantly different from the average rating of their croissants made with vegetable shortening (based on a different sample of customers).

ANOVA (Analysis of Variance): A statistical test used to compare the means of three or more samples. For example, a baker may use ANOVA to determine whether the average texture ratings of their croissants made with butter, vegetable shortening, and a combination of the two are significantly different from each other.

Scenario: A baker is interested in determining whether there is a difference in the average texture ratings of no-knead bread made with whole wheat flour versus all-purpose flour. They bake a batch of no-knead bread using each type of flour and survey a sample of customers to rate the texture on a scale from 1 (dense and chewy) to 10 (light and fluffy). They can use a t-test to evaluate whether the difference in the average ratings is statistically significant.

## VIII. p-values (5 minutes)

Definition: The probability of obtaining a result as extreme or more extreme than the observed result, given that the null hypothesis is true
Examples: Interpreting p-values in hypothesis tests

Scenario: 
Imagine that a baker is interested in determining whether there is a difference in the average texture ratings of croissants made with butter versus croissants made with vegetable shortening. They bake a batch of croissants using each type of fat and survey a sample of customers to rate the texture on a scale from 1 (dense and chewy) to 10 (light and fluffy).

The baker calculates the average texture ratings for each type of croissant and finds that the average rating for croissants made with butter is 7.5 and the average rating for croissants made with vegetable shortening is 8.0. They want to determine whether this difference in the average ratings is statistically significant, or whether it could have occurred by chance.

To do this, the baker can use a statistical test called a t-test to calculate a p-value. The p-value is the probability of obtaining a result as extreme or more extreme than the observed result, given that the null hypothesis is true.

In this case, the null hypothesis is that there is no difference in the average texture ratings of croissants made with butter versus croissants made with vegetable shortening. If the p-value is low (typically less than 0.05), it means that it is unlikely that the observed difference in the average ratings occurred by chance and that the null hypothesis can be rejected. On the other hand, if the p-value is high (greater than 0.05), it means that the observed difference could have occurred by chance and that the null hypothesis cannot be rejected.

For example, if the baker's t-test calculates a p-value of 0.01, it means that there is only a 1% chance of observing a difference as extreme or more extreme than the one observed in the sample, given that there is no real difference in the average texture ratings of croissants made with butter versus croissants made with vegetable shortening. In this case, the baker can reject the null hypothesis and conclude that there is a statistically significant difference in the average texture ratings.

t = (mean1 - mean2) / [standard error * sqrt(1/n1 + 1/n2)]

where:

t is the t-statistic
mean1 is the mean of sample 1
mean2 is the mean of sample 2
standard error is the standard error of the difference between the means: sqrt((s1^2/n1) + (s2^2/n2))
n1 is the sample size of sample 1
n2 is the sample size of sample 2
s1 is the standard deviation of sample 1
s2 is the standard deviation of sample 2
To calculate the p-value, you can use the t-statistic to look up the p-value in a table of critical values for a t-distribution or you can use a computer software or calculator to calculate it.

The p-value is the probability of obtaining a result as extreme or more extreme than the observed result, given that the null hypothesis is true. If the p-value is low (typically less than 0.05), it means that it is unlikely that the observed difference occurred by chance and that the null hypothesis can be rejected. On the other hand, if the p-value is high (greater than 0.05), it means that the observed difference could have occurred by chance and that the null hypothesis cannot be rejected