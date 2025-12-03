import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os

# Ensure dashboards directory exists
os.makedirs('dashboards', exist_ok=True)

# Load Data
print("Loading data...")
df = pd.read_csv('data.csv')

# 1. Exploratory Data Analysis (EDA)
print("Performing EDA...")

# Income Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['annual_income'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Annual Income')
plt.xlabel('Annual Income ($)')
plt.ylabel('Count')
plt.savefig('dashboards/income_distribution.png')
plt.close()

# Vehicle Preference by Region
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='region', hue='vehicle_preference', palette='viridis')
plt.title('Vehicle Preference by Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.savefig('dashboards/vehicle_preference_by_region.png')
plt.close()

# Correlation Matrix
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.savefig('dashboards/correlation_matrix.png')
plt.close()

# 2. Customer Segmentation (K-Means Clustering)
print("Performing Customer Segmentation...")
features = ['age', 'annual_income', 'dealer_visit_count', 'purchase_probability']
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[features])

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(scaled_features)

# Cluster Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='annual_income', y='purchase_probability', hue='cluster', palette='deep', s=100)
plt.title('Customer Segments: Income vs Purchase Probability')
plt.xlabel('Annual Income')
plt.ylabel('Purchase Probability')
plt.savefig('dashboards/customer_segments.png')
plt.close()

cluster_summary = df.groupby('cluster')[features].mean()
print("Cluster Summary:\n", cluster_summary)
cluster_summary.to_csv('dashboards/cluster_summary.csv')

# 3. Forecasting (Simple Linear Regression)
# Predicting Purchase Probability based on Income and Age
print("Performing Forecasting...")
X = df[['annual_income', 'age', 'dealer_visit_count']]
y = df['purchase_probability']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

print(f"Model Coefficients: {model.coef_}")
print(f"Model Intercept: {model.intercept_}")
print(f"R-squared Score: {model.score(X_test, y_test)}")

# Save forecast plot
y_pred = model.predict(X_test)
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel('Actual Purchase Probability')
plt.ylabel('Predicted Purchase Probability')
plt.title('Actual vs Predicted Purchase Probability')
plt.savefig('dashboards/forecast_accuracy.png')
plt.close()

print("Analysis Complete. Artifacts saved to 'dashboards/' directory.")
