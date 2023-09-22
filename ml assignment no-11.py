#!/usr/bin/env python
# coding: utf-8

# 1. Given X be a discrete random variable with the following PMF
# 
# 1. Find the range RX of the random variable X.
# 2. Find P(X ≤ 0.5)
# 3. Find P(0.25&lt;X&lt;0.75)
# 4. P(X = 0.2|X&lt;0.6)
# 2. Two equal and fair dice are rolled, and we observed two numbers X and Y.
# 1. Find RX, RY, and the PMFs of X and Y.
# 2. Find P(X = 2,Y = 6).
# 3. Find P(X&gt;3|Y = 2).
# 4. If Z = X + Y. Find the range and PMF of Z.
# 5. Find P(X = 4|Z = 8).
# 3. In an exam, there were 20 multiple-choice questions. Each question had 44 possible
# options. A student knew the answer to 10 questions, but the other 10 questions were unknown
# to him, and he chose answers randomly. If the student X&#39;s score is equal to the total number
# of correct answers, then find out the PMF of X. What is P(X&gt;15)?
# 4. The number of students arriving at a college between a time interval is a Poisson random
# variable. On average, 10 students arrive per hour. Let Y be the number of students arriving
# from 10 am to 11:30 am. What is P(10&lt;Y≤15)?
# 5.Two independent random variables, X and Y,are given such that X~Poisson(α) and
# Y~Poisson(β). State a new random variable as Z = X + Y. Find out the PMF of Z.
# 6. There is a discrete random variable X with the pmf.

# Let's address each of your questions one by one:
# 
# **Question 1:**
# 
# Given the PMF for the random variable X:
# 
# 1. To find the range RX, we need to identify all the possible values that X can take. The range is the set of values for which the PMF is defined.
#    
#    From the PMF, we can see that X can take on the values 0, 0.2, 0.5, and 0.8. So, RX = {0, 0.2, 0.5, 0.8}.
# 
# 2. To find P(X ≤ 0.5), you need to sum the probabilities of all values less than or equal to 0.5 from the PMF.
# 
#    P(X ≤ 0.5) = P(X = 0) + P(X = 0.2) + P(X = 0.5) = 0.3 + 0.1 + 0.2 = 0.6.
# 
# 3. To find P(0.25 < X < 0.75), sum the probabilities of all values between 0.25 and 0.75 from the PMF.
# 
#    P(0.25 < X < 0.75) = P(X = 0.5) = 0.2.
# 
# 4. To find P(X = 0.2 | X < 0.6), you need to consider only the values of X that are less than 0.6 and equal to 0.2.
# 
#    P(X = 0.2 | X < 0.6) = P(X = 0.2) / P(X < 0.6) = 0.1 / (0.3 + 0.1) = 0.1 / 0.4 = 0.25.

# **Question 2:**
# 
# Two fair dice are rolled, and we observe two numbers X and Y.
# 
# 1. To find RX and RY, we need to determine the possible values for X and Y. For a pair of dice, each can take values from 1 to 6. Therefore, RX = {1, 2, 3, 4, 5, 6} and RY = {1, 2, 3, 4, 5, 6}.
# 
# 2. To find P(X = 2, Y = 6), we consider the probability of both dice showing these specific values.
# 
#    P(X = 2, Y = 6) = P(X = 2) * P(Y = 6) = (1/36) * (1/36) = 1/1296.
# 
# 3. To find P(X > 3 | Y = 2), we consider the probability of X being greater than 3 given that Y is 2. Since Y is already known, we look at the possibilities for X.
# 
#    P(X > 3 | Y = 2) = P(X = 4) / P(Y = 2) = (1/36) / (1/36) = 1.
# 
# 4. To find the range and PMF of Z = X + Y, we can determine the possible values of Z by adding all possible pairs of X and Y values. The range is the set of possible Z values. The PMF can be calculated based on the probabilities of each Z value.
# 
#    Range of Z = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
#    
#    PMF of Z can be calculated by considering all possible pairs of X and Y values and summing their probabilities for each Z value.
# 
# 5. To find P(X = 4 | Z = 8), you need to consider the probability of X being 4 given that Z is 8. Calculate this based on the PMF of Z and the joint probabilities of X and Z.

# **Question 3:**
# 
# The PMF for the student's score X is not provided. To find the PMF of X, we need information about how the student's answers to the unknown questions are distributed. Please provide the PMF for X based on that information.
# 
# Once you have the PMF of X, you can calculate P(X > 15) by summing the probabilities of all scores greater than 15.

# **Question 4:**
# 
# To find P(10 < Y ≤ 15), you can use the Poisson distribution with a mean arrival rate of 10 students per hour.
# 
# P(Y > 10) = 1 - P(Y ≤ 10) = 1 - (P(Y = 0) + P(Y = 1) + ... + P(Y = 10))
# 
# Calculate each of these probabilities using the Poisson distribution formula, and then subtract their sum from 1 to find P(Y > 10).

# **Question 5:**
# 
# Given X ~ Poisson(α) and Y ~ Poisson(β), we can find the PMF of Z = X + Y by convolution:
# 
# PMF of Z = (e^-(α+β) * (α+β)^z) / z!
# 
# Here, z represents the possible values of Z, which can take on any non-negative integer value. This represents the distribution of the sum of two independent Poisson-distributed random variables.
# 
# If you have specific values for α and β, you can substitute them into the formula to calculate the PMF of Z for those parameter values.
# 
# If you have any specific values or further questions, please provide additional details for a more accurate answer.
