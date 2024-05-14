# Outlier Detection
# Example using z-score method
from scipy import stats
import pandas as pd

df = pd.read_csv("data/student_spending.csv")

# Select numerical columns for outlier detection
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

# Calculate z-scores for numerical columns
z_scores = stats.zscore(df[numerical_cols])

# Define threshold for outlier detection
threshold = 1.5

# Find outliers
outliers = (z_scores > threshold).any(axis=1)

# Print indices of rows containing outliers
print("Indices of rows containing outliers:")
print(df[outliers].index)

# Data Exploration - Summary Statistics
# Compute summary statistics for numerical features
summary_stats_numerical = df[numerical_cols].describe()

# Compute frequency counts for categorical features
summary_stats_categorical = {}
for col in df.select_dtypes(include=['object']).columns:
    summary_stats_categorical[col] = df[col].value_counts()

# Data Exploration - Multivariate Statistics
# Compute correlation matrix for numerical features
correlation_matrix = df[numerical_cols].corr()

# Visualize correlation matrix using heatmap
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()


