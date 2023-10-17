import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\hp\Downloads\Olympics.csv")

# Line Plot

plt.figure(figsize = (10,6))
sns.set_style('whitegrid')
plt.title("Height over time")
sns.lineplot(x= df['Year'], y = df['Height'], errorbar = None)
plt.xlabel('Olympics Year')
plt.ylabel('Average Height')
plt.show()

# Height over time based on gender

plt.figure(figsize = (10,6))
sns.set_style('whitegrid')
plt.title("Height over time")
sns.lineplot(x= df['Year'], y = df['Height'],hue= df['Sex'], errorbar = None)
plt.xlabel('Olympics Year')
plt.ylabel('Average Height')
plt.show()