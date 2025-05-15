import pandas as pd #data read,process
import numpy as np #numerical python fast maths and functions
dataset1=pd.read_csv("academic.csv")
# print(dataset1.head())

dataset2=pd.read_csv("academic_detail.csv")
# print(dataset2.head())
# print(df.describe())
#checking missing values


print("mising values")
print(dataset2.isnull().sum())

