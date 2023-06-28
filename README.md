# mh-cdc-data-analysis
Investing Populations with Critical Unmet Mental Health Needs


Datasets Utilized:
https://data.cdc.gov/NCHS/Mental-Health-Care-in-the-Last-4-Weeks/yni7-er2q/data

ABSTRACT:

This project aims to dive deeper into the impact the Coronavirus has had on mental health in the United States, with a focus on younger citizens. Specifically, we aim to explore and analyze the barriers in accessing support services and predict what percentage of people are not receiving mental healthcare. Support services, in this context, is defined as access to therapists, support groups, mental health clinicians, and medication. The data is derived from Household Pulse Survey data (a survey designed to collect data on how people’s lives have been impacted by the coronavirus pandemic) from the CDC website [3]. A Random Forest Regressor model will be used for prediction purposes.

INTRODUCTION:

About 4 in 10 adults in the U.S. reported symptoms of anxiety or depressive disorder during the pandemic. Many studies have shown that the pandemic has caused feelings of loneliness and isolation to spread amongst the general public with healthcare professionals feeling more burned out and being potentially unable to meet the demand for mental health support. In addition, younger people have reported feeling more effected by the pandemic and have reported a “youth mental health crisis.” With our general healthcare system having been under constant stress since the start of the pandemic, we wonder how the mental healthcare system specifically is meeting what evidently is a rising trend in demand for mental health assistance. Of course, with increased pressure on healthcare workers having to take on the brunt of the work during the pandemic, there has been plenty of concern around those who were unfortunately forced out of school or out of work.
  According to a study by the Institute for Health Metrics and Evaluation (IHME), throughout COVID-19 there has been a significant increase in reports of said mental health disorders - especially among women and younger people [4]. Furthermore, the American Psychological Association (APA), says that many psychologists have reported increased workloads and longer waitlists than before the pandemic. Moreover, 4 in 10 (41%) reported being unable to meet the demand for treatment and 46% said they felt burned out [1].Which leads us to the question, how has the demand for mental health assistance changed over the course of the Pandemic, compared to our system’s ability to meet it?  ​
  Now that we are nearing three years since the COVID-19 pandemic swept the nation, we know there have been numerous effects that could be explored and have not yet been explored. Specifically, the aim is to dive deeper into the impact the Coronavirus has had on mental health in the U.S., with a focus on younger citizens. Many have experienced an effect but not a lot of people talk about the barriers in accessing support services. We know that there is plenty of data to use and plenty of resources we can assess to guide us on our research and data analysis. Overall, we wish to gain further insights into this topic so as to raise awareness about mental health issues, and possibly provide recommendations to improve our current mental healthcare system. ​

GOALS AND OBJECTIVES:

The hope is to investigate and find patterns of disparities in the U.S. mental health system. On a general level, we’d like to know how well we are doing in responding to people’s need for mental health assistance. With increased demands for mental health support, we want to identify any overall trends occurring throughout the pandemic. With our system’s effectiveness in meeting said demands, we want to determine whether it is sufficient or not. Further insights that we want to explore would include changes in healthcare funding and growth in telehealth services. 

METHODOLOGY:
Data Acquisition: ​

The dataset was obtained from data.CDC.gov, Centers for Disease Control and Prevention. The data reflects responses from a Household Pulse survey, showcasing the economic and social impacts of the pandemic. We specifically investigated the mental wellness of certain groups. ​


Data Preparation:​

For the EDA phase, I started by dropping the columns that were not relevant to what we wanted to analyze with our model. The dataset initially contained extraneous data that we did not need such as the 'phase' of the trial which only corresponded to a date, and since we already had the dates for when the study occurred, we dropped the 'phase' column. Similarly, I dropped the 'lowCi,' 'highCi,' 'confidence,' and 'quartile range' columns because we did not plan on using them as data for our model. For changing types, we left everything as objects rather than strings, except for the 'start date' column which we converted to Python's datetime object because it was already formatted as such. We also noticed the data was structured in an unorthodox manner where 'group' and 'subgroup' columns had different categories as rows. For example, in the 'subgroup' column, factors like age range, state, race/ethnicity were each on individual rows so you could only look at one subgroup at a time. This means we were unable to have complete data on specific age ranges for races/ethnicities and for level of education. Due to us only being able to look at specific factors at a time, revisiting this question would probably lead us to selecting a better dataset that specifically looks at each person and describes all their characteristics and traits at a time rather than one item. ​

For  data analysis when we started getting into selecting and applying our model, we decided to dig deeper into the 'Indicator' section of our data and look at the groups of people who feel under the category of 'Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks.' We also looked the 'Value' column because that is the percentage of people based on the group that fell into the highlighted indicator. Going off this, we were able to look at which specific subgroups were not receiving mental health care but needed it.  ​



Model Selection:​

I explored the random forest regressor model which was helpful in predicting mental health trends to analyze how the U.S. mental health system can better assist people’s needs. The regressor was particularly useful in clearly identifying the outcomes and consequences of treatments or therapies taken by individuals. Furthermore, we were able to use the mean squared error to determine the accuracy of the model, whether a person is more at risk of certain mental health issues based on their lack of access to treatment/care. We chose this random forest regressor as opposed to classifier because we are looking at percentage values. Also, we chose random forest regressor as opposed to something like KNN because KKN only lets you look at two features while random forest regressor allows for multiple features like age range which can have upwards of seven. ​

RESULTS AND EVALUATION:
The State of Mental Health Care Availability​

Within the preliminary data investigation, younger age groups appear to have the highest proportion of people who needs therapy / counseling but do not receive it. Most notably, roughly one out of five people in the U.S. within the age of 18 to 29 lack support in mental healthcare when they identified themselves as needing it.​

Since each data point only includes information on one of those subsets for a population percentage volume, the accuracy of our model is constrained to this inherent lack of additional features in training data. However, our dataset also provides population percentage data for many different population grouping categories (with By Age being one of them). This allowed us to explore how our prediction model would perform after being trained on each of these grouping subsets. 

That being said, our model produces the lowest mean squared error when trained on data grouped by Sex and Age. We excluded evaluation results from National Estimate and by Gender Identity, due to the former being literal prediction data from the CDC and the latter having significantly higher mean squared error than the rest of our categories (25% versus average of 1.65% across other categories). Our top two categories to further train our model on is therefore Sex and Age. Data on those selected categories are widely available across different census surveys in many countries, thus allowing for the application of our model in identifying the proportion of populations of people who needs mental health care but do not have access to it. Our model overall has very low error rate and can definitely be improved upon across more training cycles.

CONCLUSION:
For a long time, there has been a perceived stigma surrounding mental health assistance. Through this project, we've been able to investigate the possible reasons for this stigma. By quantifying, through percentages,  the inability of obtaining adequate healthcare resources for mental health indicators, we've identified the significant barriers that people face.  In doing so, we met our goals and objectives of distinguishing the disparities in the U.S. mental health system and which groups of people need treatment but aren't getting it. ​

This model can be further improved on a larger scale of data. The more information available, the better it is for the U.S. healthcare system to support or find solutions that target more of the population. As more data becomes accessible in the coming months and years, this model can continue to be trained and evaluated for predictions in the future. ​

REFERENCES:
[1] American Psychological Association. (n.d.). Demand for mental health treatment continues to increase, say psychologists. American Psychological Association. Retrieved April 23, 2022,​

[2] Centers for Disease Control and Prevention. (2021, October 7). National and state trends in anxiety and depression severity scores among adults during the COVID-19 pandemic - United States, 2020–2021. Centers for Disease Control and Prevention. Retrieved April 23, 2022 ​

[3] Centers for Disease Control and Prevention. (n.d.). Mental health care in the last 4 weeks. Centers for Disease Control and Prevention. Retrieved April 23, 2022 ​

[4] The Lancet: COVID-19 pandemic led to Stark rise in depressive and anxiety disorders globally in 2020, with women and younger people most affected. Institute for Health Metrics and Evaluation. (2021, October 8). Retrieved April 23, 2022 ​

[5] Still recovering: Mental health impact of the COVID-19 pandemic in New York State. New York State Health Foundation. (2021, October 29). Retrieved April 23, 2022​
​
