
#load packages needed

import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib as plt
import matplotlib.pyplot as plt

#set your working directory- replace the file path in orange with where the project folder is stored on your machine
os.chdir('/Users/jennifershelton/Downloads/SBA/Intermediate')

#print working directory to make sure you're in the right folder
os.getcwd()

#import the data file- you can copy and paste it into the orange field
#for this business project there are multiple files, so duplicate this line and create unique variable names for each of them
df = pd.read_csv('public_up_to_150k_12_220403.csv')

print(df.shape)

print (df.columns, len(df.columns))

print(df.head())