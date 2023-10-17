import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\hp\Downloads\Olympics.csv")

# Creating a new column 'Sentiment'

conditions = [(df['Medal'] > 1), (df['Medal'] == 0), (df['Medal'] == 1)]
choices = ['Positive', 'Negative', 'Neutral']
df['Sentiment'] = np.select(conditions, choices, default = 'Negative')
print(df['Sentiment'].value_counts(normalize= True))

# Creating a Pie plot for analysing the percentage sentiment
plt.figure(figsize= (8,4))
plt.pie(df['Sentiment'].value_counts(), labels= df['Sentiment'].value_counts().index ,autopct= '%1.1f%%' )
plt.show()