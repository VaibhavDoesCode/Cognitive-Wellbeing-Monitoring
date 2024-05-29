# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a5gJKWaDGraLbjZzveNMJwBg0sgb-PJn

AI MENTAL FITNESS TRACKER

About the data


* Data Overview: This is a **Mental Health** csv data
"""

#importing the required libraries
import warnings
warnings.filterwarnings('ignore')
import numpy as np #linear algebra
import pandas as pd #data preocessing,cvs file I/O(e.g. pd.read_csv)
import seaborn as sns #Seaborn is a Python data visualisation library based on matplotlib
import matplotlib.pyplot as plt #Matplotlib is a low level graph plotting library in python that serves visual abilities
import plotly.express as px #allows you to create interactive plots with very little codes

"""Exploratory Data Analysis

Load and prepare the data
"""

#prevalence-by-mental-and-substance-use disorder.csv
df1=pd.read_csv("/content/prevalence-by-mental-and-substance-use-disorder.csv")
#mental-and-substance-use-as-share-of-disease.csv
df2=pd.read_csv("/content/mental-and-substance-use-as-share-of-disease -AI (5).csv")

#prevalence-by-mental-and-substance-use disorder.csv
df1.head()

#mental-and-substance-use-as-share-of-disease.csv
df2.head(10)

#Merging two datasets:mental-and-substance-use-as-share-of-disease.csv,prevalence-by-mental-and-substance-use disorder.csv
data = pd.merge(df1,df2)
data.head(10)

"""Data Cleaning"""

#Missing data values in dataset
data.isnull().sum()

#view the data
data.head(10)

#size=row*column,shape=tuple of array dimension (row, column)
data.size,data.shape

data.set_axis(['Country','Year','Schizophrenia','Bipolar_disorder','Eating_disorder','Anxiety','drug_usage','depression','alcohol','mental_fitness,','missing_labels'], axis='columns')

data.head(10)

"""Visualisation"""

