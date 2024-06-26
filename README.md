# [LIN 371 Machine Learning for Text Analysis]([https://sites.google.com/utexas.edu/lin353c-introduction-to-comput/home](https://jessyli.com/courses/lin371)) <img align="right" width="100" height="100" src=Misc/UT_Seal.png>

## Table of Contents

- [Introduction](#introduction)
- [Assignments](#assignments)
- [Final Project](#final-project---predicting-political-and-ideological-alignment-using-x-data)

## Introduction

This repository contains all of the assignments and input text files for LIN 371 Machine Learning for Text Analysis with Professor Jessy in the Spring 2024 semester at the University of Texas at Austin. This course covers the intersection of linguistics and computer science through machine learning algorithms and statistics.

## Assignments

[Homework 1](https://github.com/eloragh/LIN-371/blob/main/Homework/hw1_eae2273.ipynb)
- Bayes Theorem, maximum a posteriori (MAP), sample and conditional entropy, sentiment analysis, log odds ratio

[Homework 2](https://github.com/eloragh/UT_Austin_LIN_371/blob/main/Homework/hw2_eae2273.ipynb)
- Naive Bayes, n-gram language model, tokenization, log conditional probabilities, perplexity, random text generation

[Homework 3](https://github.com/eloragh/UT_Austin_LIN_371/blob/main/Homework/hw3_eae2273.ipynb)
- Logistic regression, regularization, evaluation, vectorization, 10-fold cross-validation, POS tag extraction, column transform

[Homework 4](https://github.com/eloragh/UT_Austin_LIN_371/blob/main/Homework/hw4_eae2273.ipynb)
- Multi-layer perceptions, deep neural networks, overfitting, static word embeddings vs. contextualized word embeddings, neural network bias

## Final Project - Predicting Political and Ideological Alignment using X Data
<img align="left" width="400" height="300" src=Misc/political_compass_nontransparent.png>

This final project was done in collaboration with Rylan Vachon. Our goal was to use X data to plot different users on the [Political Compass](https://www.politicalcompass.org/). 

We collected 5,000+ datapoints for 190+ politicians. The data was preprocessed in different ways through three separate iterations:

  Iteration 1: CountVectorizer

  Iteration 2: GloVE Embeddings
  
  Iteration 3: BERT Embeddings

The data was used to train two separate linear regression models. Each model was responsible for predicting one of the two coordinates on a 10x10 cartesian plane.

To read more about the methodology and results, see [Predicting Political and Ideological Alignment using X Data.](https://github.com/eloragh/UT_Austin_LIN_371/tree/main/Political%20Compass%20Project)
