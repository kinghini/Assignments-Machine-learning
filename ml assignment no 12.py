#!/usr/bin/env python
# coding: utf-8

# 1. What is prior probability? Give an example.
# 2. What is posterior probability? Give an example.
# 3. What is likelihood probability? Give an example.
# 
# 4. What is Naïve Bayes classifier? Why is it named so?
# 
# 5. What is optimal Bayes classifier?
# 
# 6. Write any two features of Bayesian learning methods.
# 
# 7. Define the concept of consistent learners.
# 
# 8. Write any two strengths of Bayes classifier.
# 
# 9. Write any two weaknesses of Bayes classifier.
# 
# 10. Explain how Naïve Bayes classifier is used for
# 
# 1. Text classification
# 
# 2. Spam filtering
# 
# 3. Market sentiment analysis

# 1. **Prior Probability**: Prior probability, often denoted as P(A), is the probability assigned to an event or hypothesis before considering any new evidence or data. It represents the initial belief or knowledge about the likelihood of an event occurring. An example could be the probability of a customer buying a product based on historical data before any new information or customer-specific data is available.

# 2. **Posterior Probability**: Posterior probability, often denoted as P(A|B), is the updated probability of an event or hypothesis after considering new evidence or data (B). It is calculated using Bayes' theorem and reflects the revised belief about the event given the observed data. For example, the probability of a medical condition given the results of diagnostic tests is a posterior probability.

# 3. **Likelihood Probability**: Likelihood probability, often denoted as P(B|A), represents the probability of observing a particular set of data or evidence (B) given that a specific hypothesis or event (A) is true. It quantifies how well the data supports the hypothesis. For instance, the probability of getting a positive test result given the presence of a medical condition is a likelihood probability.

# 4. **Naïve Bayes Classifier**: The Naïve Bayes classifier is a probabilistic machine learning algorithm used for classification tasks. It is named "naïve" because it makes a simplifying assumption that the features used for classification are conditionally independent, given the class label. Despite this simplification, Naïve Bayes can be surprisingly effective in many real-world applications, such as text classification and spam filtering.

# 5. **Optimal Bayes Classifier**: The optimal Bayes classifier is a theoretical classifier that assigns each data point to the class with the highest posterior probability. It is considered optimal because it minimizes the classification error when the true underlying probabilistic model is known. However, in practice, obtaining the exact posterior probabilities can be challenging, and Naïve Bayes is often used as a practical approximation.

# 6. **Features of Bayesian Learning Methods**:
#    - **Probabilistic Framework**: Bayesian learning methods provide a probabilistic framework for modeling uncertainty and updating beliefs based on evidence.
#    - **Incorporation of Prior Knowledge**: They allow the incorporation of prior knowledge or beliefs into the learning process, which can be especially useful when dealing with limited data.

# 7. **Consistent Learners**: Consistent learners are machine learning algorithms that, given enough training data, will converge to the correct target function as the amount of data increases. In other words, they are guaranteed to learn the true underlying pattern when provided with sufficient data.

# 8. **Strengths of Bayes Classifier**:
#    - **Effective with Small Datasets**: Naïve Bayes classifiers work well even with limited training data, making them suitable for applications where data is scarce.
#    - **Fast and Scalable**: They are computationally efficient and can handle high-dimensional feature spaces, making them suitable for real-time or large-scale applications.

# 9. **Weaknesses of Bayes Classifier**:
#    - **Assumption of Feature Independence**: The "naïve" assumption of feature independence may not hold in some real-world scenarios, which can lead to suboptimal performance.
#    - **Sensitivity to Input Data**: Bayes classifiers can be sensitive to the quality of the training data and the choice of prior probabilities, potentially leading to biased results.

# 10. **Naïve Bayes Classifier Usage**:
# 
#    1. **Text Classification**: Naïve Bayes is widely used for text classification tasks such as spam detection, sentiment analysis, and topic categorization. It calculates the probability of a document belonging to a particular category based on the words or features in the text.
# 
#    2. **Spam Filtering**: In spam filtering, Naïve Bayes classifies emails as spam or not spam based on the likelihood of certain words or patterns occurring in spam emails. It can be trained on a dataset of labeled emails to make predictions.
# 
#    3. **Market Sentiment Analysis**: Naïve Bayes can be used in market sentiment analysis to classify news articles, tweets, or social media posts as positive, negative, or neutral based on the sentiment expressed in the text. It helps gauge public sentiment about products or stocks.
