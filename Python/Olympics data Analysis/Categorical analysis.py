import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\hp\Downloads\Olympics.csv")
# print(df.columns)
df_swimming = df[df["Sport"] == 'Swimming']
df_swimming['Team'].value_counts()
df_swim_top3 = df_swimming.loc[df_swimming['Team'].isin(['United States','Germany','Australia'])]

plt.figure(figsize= (8,4))
sns.set_style('whitegrid')
x = sns.barplot(data = df_swim_top3, y = 'Height', x = 'Sex')
x.set(title = 'Average Height based on Gender')
# plt.show()

plt.figure(figsize= (8,4))
sns.set_style('whitegrid')
x = sns.barplot(data = df_swim_top3, y = 'Weight', x = 'Sex')
x.set(title = 'Average Weight based on Gender')
# plt.show()

plt.figure(figsize= (8,4))
sns.set_style('whitegrid')
x = sns.barplot(data = df_swim_top3, y = 'Medal', x = 'Sex', estimator= sum, palette = 'Set1')
x.set(title = 'Medal count based on Gender')
plt.show()

# Male swimmers of the top 3 participating countries have more average height and weight compared to female swimmers.
# Whereas in terms of total medal tally is same for both males and females.