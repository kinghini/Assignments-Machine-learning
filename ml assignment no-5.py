#!/usr/bin/env python
# coding: utf-8

# 1. What are the key tasks that machine learning entails? What does data pre-processing imply?
# 2. Describe quantitative and qualitative data in depth. Make a distinction between the two.
# 3. Create a basic data collection that includes some sample records. Have at least one attribute from
# each of the machine learning data types.
# 
# 4. What are the various causes of machine learning data issues? What are the ramifications?
# 
# 5. Demonstrate various approaches to categorical data exploration with appropriate examples.
# 
# 6. How would the learning activity be affected if certain variables have missing values? Having said
# that, what can be done about it?
# 
# 7. Describe the various methods for dealing with missing data values in depth.
# 
# 8. What are the various data pre-processing techniques? Explain dimensionality reduction and
# function selection in a few words.
# 
# 9.
# 
# i. What is the IQR? What criteria are used to assess it?
# 
# ii. Describe the various components of a box plot in detail? When will the lower whisker
# surpass the upper whisker in length? How can box plots be used to identify outliers?
# 
# 10. Make brief notes on any two of the following:
# 
# 1. Data collected at regular intervals
# 
# 2. The gap between the quartiles
# 
# 3. Use a cross-tab
# 
# 1. Make a comparison between:
# 
# 1. Data with nominal and ordinal values
# 
# 2. Histogram and box plot
# 
# 3. The average and median

# 1. **Key Tasks in Machine Learning**:
#    - Data Collection: Gather relevant data for the problem.
#    - Data Preprocessing: Clean, transform, and prepare data for analysis.
#    - Feature Engineering: Create or select relevant features.
#    - Model Selection: Choose an appropriate algorithm.
#    - Model Training: Train the model on the data.
#    - Hyperparameter Tuning: Optimize model settings.
#    - Model Evaluation: Assess model performance.
#    - Deployment: Implement the model in real-world applications.
# 
#    **Data Preprocessing** involves activities like handling missing values, scaling, normalizing, encoding categorical data, and removing outliers to ensure data is suitable for machine learning.
# 
# 

# 2. **Quantitative vs. Qualitative Data**:
# 
#    - **Quantitative Data**: Also known as numerical data, it represents measurable quantities and is expressed in numerical terms. Examples include age, height, temperature, and income.
# 
#    - **Qualitative Data**: Also known as categorical data, it represents categories or labels and is non-numeric. Examples include gender (male, female), color (red, blue), and city names.
# 

# 
# 3. **Sample Data Collection**:
# 
#    Suppose we're collecting data on student performance:
# 
#    | Student ID | Age | Gender | Grade | Exam Score |
#    |------------|-----|--------|-------|------------|
#    | 1          | 20  | Male   | A     | 88         |
#    | 2          | 22  | Female | B     | 75         |
#    | 3          | 21  | Male   | C     | 62         |
#    | 4          | 19  | Female | A     | 92         |
#    | 5          | 20  | Male   | B     | 78         |
# 
#    This dataset includes both quantitative (Age, Exam Score) and qualitative (Gender, Grade) attributes.
# 

# 4. **Causes of Data Issues**:
#    - Missing Data: Data points with incomplete or absent values.
#    - Outliers: Extreme values that deviate significantly from the majority.
#    - Imbalanced Data: Unequal distribution of classes.
#    - Noisy Data: Data with errors, inconsistencies, or inaccuracies.
#    - Data Skewness: Biased data distribution.
# 
#    Ramifications include biased models, inaccurate predictions, and reduced model performance.
# 

# 5. **Approaches to Categorical Data Exploration**:
# 
#    a. **Frequency Table**: Create a table showing the count or frequency of each category.
#    Example: Count of customer genders in a survey.
# 
#    b. **Bar Chart**: Visualize categorical data using bars to represent category counts.
#    Example: Bar chart showing the distribution of car brands in a market.
# 
#    c. **Pie Chart**: Display the relative proportions of different categories in a circle.
#    Example: Pie chart showing the distribution of fruit preferences.
# 

# 6. **Impact of Missing Values**:
#    Missing values can lead to biased model training, reduced model accuracy, and loss of valuable information. To handle missing values, techniques like imputation (filling missing values with estimates) or excluding incomplete records can be applied.
# 

# 7. **Methods for Dealing with Missing Data**:
# 
#    a. **Deletion**: Remove rows or columns with missing values.
#    b. **Imputation**: Fill missing values with estimates (e.g., mean, median, mode).
#    c. **Prediction**: Use machine learning models to predict missing values based on other attributes.
#    d. **Flagging**: Introduce a binary flag variable to indicate missing data.
# 

# 8. **Data Preprocessing Techniques**:
# 
#    - **Dimensionality Reduction**: Reducing the number of features while preserving relevant information, often using techniques like Principal Component Analysis (PCA).
#    
#    - **Feature Selection**: Selecting a subset of relevant features to reduce model complexity and improve performance.
# 

# 9. **Box Plot**:
# 
#    i. **IQR (Interquartile Range)**: The IQR is the range between the first quartile (Q1) and the third quartile (Q3) of a dataset. It is used to assess the spread and variability of data.
# 
#    ii. **Components of a Box Plot**: A box plot consists of a box, whiskers, and data points. The lower whisker extends to the smallest value within 1.5 times the IQR below Q1, and the upper whisker extends to the largest value within 1.5 times the IQR above Q3. Outliers are shown as individual points beyond the whiskers.
# 
#    The lower whisker surpasses the upper whisker in length when the data distribution is skewed, with a long tail on the lower end.
# 
#    Box plots are used to visualize the central tendency, spread, and presence of outliers in a dataset.
# 

# 10. **Comparison**:
# 
#     1. **Data with Nominal and Ordinal Values**:
#        - Nominal data has no intrinsic order (e.g., colors).
#        - Ordinal data has a meaningful order (e.g., rankings).
# 
#     2. **Histogram and Box Plot**:
#        - Histogram displays the distribution of data values, showing frequency or density.
#        - Box plot summarizes data distribution, showing quartiles, outliers, and skewness.
# 
#     3. **Average and Median**:
#        - Average (mean) is the sum of values divided by the number of values.
#        - Median is the middle value in an ordered dataset. Median is less affected by outliers than the mean.

# In[ ]:




