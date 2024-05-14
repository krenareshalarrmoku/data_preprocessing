# importing libraries
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder

# Data gathering
print('\n\n# Data gathering')
for dirname, _, filenames in os.walk('data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv("data/student_spending.csv")

# Data Quality Check
print('\n\n# Data Quality Check')
print('\n\nHead')
print(df.head())
print('\n\nInfo')
print(df.info())
print('\n\nData Describe')
print(df.describe().T)

# Identify and Treat Null Values
print('\n\n# Identify and Treat Null Values')
print(df.isnull().sum())
df.dropna(inplace=True)

# Remove the first column
print('\n\n# Remove the first column')
df = df.iloc[:, 1:]
print(df.head(2))

# Data Type Definition
print('\n\n# Data Type Definition')
print(df.dtypes)

numerical_cols = [col for col in df.columns if df[col].dtype != 'O']

categorical_cols = [col for col in df.columns if df[col].dtype == 'O']

print('\n\nCategorical columns:')
for cat_col in categorical_cols:
    print(cat_col)
print('\n\nNumerical columns:')
for num_col in numerical_cols:
    print(num_col)

categorical_variables = ['gender', 'year_in_school', 'major', 'preferred_payment_method']

numerical_variables = ['age', 'monthly_income', 'financial_aid', 'tuition', 'housing', 'food', 'transportation',
                       'books_supplies', 'entertainment', 'personal_care', 'technology', 'health_wellness',
                       'miscellaneous', ]

# Descriptive statistics for numerical variables
numerical_desc = df[numerical_variables].describe()

# Descriptive statistics for categorical variables
categorical_desc = df[categorical_variables].astype('category').describe()

# Print the descriptive statistics
print("\n\nDescriptive Statistics for Numerical Variables:")
print(numerical_desc)

print("\n\nDescriptive Statistics for Categorical Variables:")
print(categorical_desc)

# Encoding Categorical Variables
print('\n\n# Encoding Categorical Variables')
encoder = LabelEncoder()
df['gender'] = encoder.fit_transform(df['gender'])
df['year_in_school'] = encoder.fit_transform(df['year_in_school'])
df['major'] = encoder.fit_transform(df['major'])
df['preferred_payment_method'] = encoder.fit_transform(df['preferred_payment_method'])
print(df.head())
# Dimension Reduction (if needed)
# Example: PCA (Principal Component Analysis)
from sklearn.decomposition import PCA

# Assuming 'df' contains numeric columns that need dimension reduction
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
X = df[numeric_cols]
print('\n\nNumeric column used for dimension reduction:\n', X)
# Specify the number of components you want to reduce to
n_components = 3
pca = PCA(n_components=n_components)
principal_components = pca.fit_transform(X)

# Create a DataFrame with reduced dimensions
df_reduced = pd.DataFrame(data=principal_components, columns=[f'PC{i + 1}' for i in range(n_components)])
print('\n\nData with reduced dimensions:', df_reduced)
# Attribute Creation
# Creating a new attribute 'total_expenses'
df['total_expenses'] = df['tuition'] + df['housing'] + df['food'] + df['transportation'] + df['books_supplies'] + df[
    'entertainment'] + df['personal_care'] + df['technology'] + df['health_wellness'] + df['miscellaneous']

# Discretization/Binarization (if needed)
# Binarizing the 'financial_aid' column
from sklearn.preprocessing import Binarizer

binarizer = Binarizer(threshold=0)  # Binarize any value greater than 0 to 1
df['has_financial_aid'] = binarizer.fit_transform(df[['financial_aid']])

# Example: Discretizing the 'monthly_income' column into three bins
from sklearn.preprocessing import KBinsDiscretizer

discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal',
                               strategy='quantile')  # Discretize into 3 bins based on quantiles
df['income_group'] = discretizer.fit_transform(df[['monthly_income']])

# Display the updated DataFrame
print('\n\nDisplay dataset head with binarized financial_aid column and discretized monthly_income column:')
print(df.head())

# Save current dataset state
df.to_csv('data/preprocessed_data.csv', index=False)

# Standardization/Normalization (if needed)
scaler = StandardScaler()
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Sample data
sample_df = df.sample(n=100, random_state=42)  # Adjust sample size as needed

# Save preprocessed data
sample_df.to_csv("data/standardization_data.csv", index=False)
