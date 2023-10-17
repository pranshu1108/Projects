import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\hp\Downloads\Olympics.csv")

df_swimming = df[df['Sport'] == 'Swimming']
df_swimming['Team'].value_counts()

df_swim_top3 = df_swimming.loc[df_swimming['Team'].isin(['United States', 'Germany', 'Australia'])]

plt.figure(figsize = (10,6))
plt.subplot(1, 2, 1)
sns.boxplot(data = df_swim_top3, x = 'Team', y = "Height")
plt.title("Boxplot")

plt.subplot(1,2,2)
sns.histplot(data = df_swim_top3, x = "Height", bins = 20, kde= True)
plt.ylabel('Frequency')
plt.title("Histogram")
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(data = df_swim_top3, x = 'Team', y = 'Weight', ax = axes[0])
axes[0].set_title('Box Plot')

sns.histplot(data = df_swim_top3, x = 'Weight', bins = 20, kde = True, ax = axes[1])
axes[1].set_title("Histogram")
axes[1].set_ylabel("Frequency")
plt.tight_layout()
plt.show()