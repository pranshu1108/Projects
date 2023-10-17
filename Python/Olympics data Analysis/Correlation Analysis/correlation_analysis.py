import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\hp\Downloads\Olympics.csv")
numerical_columns = df.select_dtypes(include = np.number)
numerical_columns.corr()

plt.figure(figsize = (8,4))
sns.set_style('whitegrid')
x = sns.scatterplot(data = numerical_columns, palette = 'Set1')
plt.show()

#For sports - Gymnastics
df_gymnastics = df[df["Sport"] == "Gymnastics"][["Height", "Weight", "Sex"]]

plt.figure(figsize = (10,4))
sns.set_style('whitegrid')
sns.scatterplot(data = df_gymnastics, x = "Height", y = "Weight", hue = "Sex")
plt.show()

#For sports - weightlifting
df_weightlifting = df[df["Sport"] == "Weightlifting"]

plt.figure(figsize = (8,4))
sns.set_style('whitegrid')
x = sns.scatterplot(data = df_weightlifting, x = "Height", y = "Weight", hue = "Sex", palette = 'Set1')
x.set(title = 'scatter plot between height and weight based on gender for sport as Weightlifting')
plt.show()
