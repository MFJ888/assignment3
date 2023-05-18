# -*- coding: utf-8 -*-
"""
Created on Fri May 19 02:35:02 2023

@author: faisal
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#Reading data from csv file
# Load CSV data into a pandas DataFrame
Data = pd.read_csv('energy.csv')

# Function to normalize the data
def normalize_data(data):
    Scaler = MinMaxScaler()
    Scaled_data = scaler.fit_transform(data)
    return scaled_data

# Function to clean the data
def clean_data(data):
    # Remove any rows with missing values
    Cleaned_data = data.dropna()
    return cleaned_data


# Clean the data
Cleaned_data = clean_data(data)

# Extract data for x-axis and y-axis
X = cleaned_data['Country Name']
Y = cleaned_data['CO2 emission']

# Normalize the data
Y_normalized = normalize_data(y.values.reshape(-1, 1))

# Generate the graph
Plt.plot(x, y_normalized)
Plt.xlabel('CO2 Emissions')
Plt.ylabel('Per Capita')
Plt.title('Comparision CO2 Emissions with Countries per capita')
Plt.grid(True)

# Display the graph
Plt.show()
'''
https://www.kaggle.com/datasets/txtrouble/carbon-emissions
'''