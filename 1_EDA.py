# 1_EDA.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('D:\Customer-Churn-Prediction-main\Customer-Churn-Prediction-main\data\Churn_Modelling.csv')

# Display shape and columns
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

# Display first 5 rows
print(df.head())

# Check for null values
print("Missing values:\n", df.isnull().sum())

# Summary statistics
print(df.describe())
# Count of churned vs retained
plt.figure(figsize=(6,4))
sns.countplot(x='Exited', data=df)
plt.title('Churn Count (0 = Retained, 1 = Churned)')
plt.xlabel('Exited')
plt.ylabel('Count')
plt.show()
#Gender vs Churn
plt.figure(figsize=(6,4))
sns.countplot(x='Gender', hue='Exited', data=df)
plt.title('Churn by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Exited',labels=['NO','YES'])
plt.show()
# Geography vs Churn
plt.figure(figsize=(6,4))
sns.countplot(x='Geography', hue='Exited', data=df)
plt.title('Churn by Geography')
plt.xlabel('Geography')
plt.ylabel('Count')
plt.legend(title='Exited',labels=['NO','YES'])
plt.show()
# Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
#Pairplot for selected features
selected_features=['CreditScore','Age','Balance','EstimatedSalary','Exited']
sns.pairplot(df[selected_features],hue='Exited',palette='husl')
plt.suptitle('Pairploy of Selected Features',y=1.02)
plt.show()