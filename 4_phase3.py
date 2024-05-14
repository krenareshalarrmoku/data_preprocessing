import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
df = pd.read_csv("data/student_spending.csv")

# Visualization Based on Data Type
# Numerical data visualization (histogram)
plt.figure(figsize=(8, 6))
sns.histplot(df['monthly_income'], kde=True)
plt.title('Distribution of Monthly Income')
plt.xlabel('Monthly Income')
plt.ylabel('Frequency')
plt.show()

# Categorical data visualization (bar plot)
plt.figure(figsize=(8, 6))
sns.countplot(x='year_in_school', data=df)
plt.title('Distribution of Students by Year in School')
plt.xlabel('Year in School')
plt.ylabel('Count')
plt.show()

# Static Visualization

# Box plot (static)
plt.figure(figsize=(10, 8))
sns.boxplot(x='gender', y='monthly_income', data=df)
plt.title('Monthly Income by Gender')
plt.xlabel('Gender')
plt.ylabel('Monthly Income')
plt.show()

# Interactive Visualization

# Scatter plot (interactive)
fig = px.scatter(df, x='tuition', y='housing', color='year_in_school', hover_name='major', title='Tuition vs. Housing by Year in School')
fig.show()

# Multidimensional Data Visualization

# Pair plot (multidimensional)
sns.pairplot(df[['monthly_income', 'tuition', 'housing', 'food', 'transportation']])
plt.suptitle('Pair Plot of Numerical Features', y=1.02)
plt.show()
