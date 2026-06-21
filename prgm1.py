#prg 1...
# Import libraries
#1.Develop a program to create histograms for all numerical features and analyze the distribution of each feature. Generate box plots for all numerical features and identify any outliers. Use California Housing
#dataset.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv(r"D:\ML\Datasets\housing.csv")
print(df.head(10))
print(df.shape)
df.info()
df.nunique()
print(df.nunique())
df.isnull().sum()
print(df.isnull().sum())
df.duplicated().sum()
print(df.duplicated().sum())
df.describe()
print(df.describe())
Numerical = df.select_dtypes(include=[np.number]).columns 
print(Numerical)
for col in Numerical: plt.figure(figsize=(10, 6))
df[col].plot(kind='hist', title=col, bins=60, edgecolor='black') 
plt.ylabel('Frequency' )
plt.show()
for col in Numerical: plt.figure(figsize=(6, 6)) 
sns.boxplot(df[col], color='blue')
plt.title(col) 
plt.ylabel(col)
plt.show()
