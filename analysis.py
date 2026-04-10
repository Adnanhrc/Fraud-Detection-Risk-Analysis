# import pandas as pd

# # Load dataset
# df = pd.read_csv("creditcard.csv")

# # -------------------------------
# # BASIC OVERVIEW
# # -------------------------------
# print("Dataset Shape:", df.shape)
# print("\n")

# # -------------------------------
# # DATA INFORMATION
# # -------------------------------
# print("Dataset Info:")
# print(df.info())
# print("\n")

# # -------------------------------
# # FIRST 5 ROWS
# # -------------------------------
# print("Sample Data:")
# print(df.head())
# print("\n")

# # -------------------------------
# # CLASS DISTRIBUTION (VERY IMPORTANT)
# # -------------------------------
# print("Fraud vs Normal Transactions:")
# print(df['Class'].value_counts())
# print("\n")

# # -------------------------------
# # FRAUD PERCENTAGE
# # -------------------------------
# fraud_percentage = (df['Class'].value_counts(normalize=True) * 100)
# print("Fraud Percentage:")
# print(fraud_percentage)


# # -------------------------------
# # FEATURE ENGINEERING
# # -------------------------------

# # 1. High Transaction Amount Flag
# threshold = df['Amount'].quantile(0.95)  # top 5% transactions
# df['High_Amount_Flag'] = df['Amount'] > threshold

# # 2. Convert Time to Hours (simulate time of day)
# df['Hour'] = (df['Time'] // 3600) % 24

# # 3. Night Transaction Flag (fraud often happens at night)
# df['Night_Transaction'] = df['Hour'].apply(lambda x: 1 if (x >= 0 and x <= 6) else 0)

# # 4. Amount Z-Score (detect outliers)
# df['Amount_Zscore'] = (df['Amount'] - df['Amount'].mean()) / df['Amount'].std()

# # 5. Extreme Amount Flag
# df['Extreme_Amount'] = df['Amount_Zscore'].apply(lambda x: 1 if abs(x) > 3 else 0)

# # Show new columns
# print(df[['Amount', 'High_Amount_Flag', 'Hour', 'Night_Transaction', 'Amount_Zscore', 'Extreme_Amount']].head())




# # -------------------------------
# # RISK SCORING SYSTEM
# # -------------------------------

# # Assign risk scores
# df['Risk_Score'] = (
#     df['High_Amount_Flag'].astype(int) * 2 +
#     df['Night_Transaction'] * 1 +
#     df['Extreme_Amount'] * 3
# )

# # Define threshold for suspicious transactions
# df['Suspicious'] = df['Risk_Score'].apply(lambda x: 1 if x >= 3 else 0)

# # Show top suspicious transactions
# suspicious_df = df[df['Suspicious'] == 1]

# print("Total Suspicious Transactions:", suspicious_df.shape[0])
# print("\nTop Suspicious Transactions:")
# print(suspicious_df[['Amount', 'Hour', 'Risk_Score']].head(10))




# # -------------------------------
# # MODEL VALIDATION
# # -------------------------------

# # Compare suspicious vs actual fraud
# comparison = pd.crosstab(df['Suspicious'], df['Class'])

# print("Confusion Matrix:")
# print(comparison)

# # Calculate how many real frauds we caught
# fraud_captured = df[(df['Suspicious'] == 1) & (df['Class'] == 1)].shape[0]
# total_fraud = df[df['Class'] == 1].shape[0]

# print("\nFraud Captured:", fraud_captured)
# print("Total Fraud:", total_fraud)

# print("\nDetection Rate (%):", (fraud_captured / total_fraud) * 100)






# # -------------------------------
# # IMPROVED RISK SCORING
# # -------------------------------

# df['Improved_Risk_Score'] = (
#     df['High_Amount_Flag'].astype(int) * 2 +
#     df['Night_Transaction'] * 1 +
#     df['Extreme_Amount'] * 3 +
#     (df['Amount'] > 1000).astype(int) * 2   # extra rule
# )

# df['Improved_Suspicious'] = df['Improved_Risk_Score'].apply(lambda x: 1 if x >= 4 else 0)

# # Evaluate again
# comparison2 = pd.crosstab(df['Improved_Suspicious'], df['Class'])

# print("Improved Confusion Matrix:")
# print(comparison2)

# fraud_captured2 = df[(df['Improved_Suspicious'] == 1) & (df['Class'] == 1)].shape[0]

# print("\nImproved Fraud Captured:", fraud_captured2)
# print("Detection Rate (%):", (fraud_captured2 / total_fraud) * 100)





















# 1%
"""
===========================================
FRAUD DETECTION PROJECT (END-TO-END)
===========================================

Objective:
Detect fraudulent transactions using:
1. Rule-Based Approach
2. Machine Learning (Logistic Regression)

Dataset:
Credit Card Transactions (Highly Imbalanced)

Author: [Your Name]
===========================================
"""

# -------------------------------
# IMPORT LIBRARIES
# -------------------------------
import pandas as pd
import numpy as np

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("creditcard.csv")

print("="*50)
print("DATASET OVERVIEW")
print("="*50)

# Shape of dataset
print("Dataset Shape:", df.shape)

# Fraud vs Normal distribution
print("\nFraud vs Normal Transactions:")
print(df['Class'].value_counts())

# Percentage distribution
print("\nFraud Percentage (%):")
print(df['Class'].value_counts(normalize=True) * 100)

# -------------------------------
# FEATURE ENGINEERING
# -------------------------------
print("\n" + "="*50)
print("FEATURE ENGINEERING")
print("="*50)

# 1. High Amount Flag (Top 5% transactions)
threshold = df['Amount'].quantile(0.95)
df['High_Amount_Flag'] = df['Amount'] > threshold

# 2. Convert Time into Hour (simulate time of day)
df['Hour'] = (df['Time'] // 3600) % 24

# 3. Night Transaction Flag (fraud often occurs at night)
df['Night_Transaction'] = df['Hour'].apply(lambda x: 1 if (0 <= x <= 6) else 0)

# 4. Z-score for Amount (detect unusual transactions)
df['Amount_Zscore'] = (df['Amount'] - df['Amount'].mean()) / df['Amount'].std()

# 5. Extreme Amount Flag (outliers)
df['Extreme_Amount'] = df['Amount_Zscore'].apply(lambda x: 1 if abs(x) > 3 else 0)

# Preview new features
print("\nFeature Engineering Preview:")
print(df[['Amount', 'High_Amount_Flag', 'Hour', 'Night_Transaction', 'Extreme_Amount']].head())

# -------------------------------
# RULE-BASED FRAUD DETECTION
# -------------------------------
print("\n" + "="*50)
print("RULE-BASED MODEL")
print("="*50)

# Assign risk score based on business logic
df['Risk_Score'] = (
    df['High_Amount_Flag'].astype(int) * 2 +
    df['Night_Transaction'] * 1 +
    df['Extreme_Amount'] * 3
)

# Flag suspicious transactions
df['Suspicious'] = df['Risk_Score'].apply(lambda x: 1 if x >= 3 else 0)

# Evaluate rule-based model
print("\nRule-Based Confusion Matrix:")
print(pd.crosstab(df['Suspicious'], df['Class']))

# -------------------------------
# MACHINE LEARNING MODEL
# -------------------------------
print("\n" + "="*50)
print("MACHINE LEARNING MODEL (LOGISTIC REGRESSION)")
print("="*50)

# Select features
features = ['Amount', 'Hour', 'High_Amount_Flag', 'Night_Transaction', 'Extreme_Amount']
X = df[features]
y = df['Class']

# Train-test split (important for fair evaluation)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y   # maintain class imbalance ratio
)

# Logistic Regression with class balancing (CRITICAL FIX)
model = LogisticRegression(max_iter=1000, class_weight='balanced')

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# -------------------------------
# MODEL EVALUATION
# -------------------------------
print("\nML Model Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# -------------------------------
# FEATURE IMPORTANCE
# -------------------------------
print("\n" + "="*50)
print("FEATURE IMPORTANCE")
print("="*50)

importance = pd.DataFrame({
    'Feature': features,
    'Coefficient': model.coef_[0]
})

print(importance.sort_values(by='Coefficient', ascending=False))

# -------------------------------
# EXPORT DATA FOR POWER BI
# -------------------------------
df.to_csv("final_fraud_data.csv", index=False)

print("\n✅ Final dataset exported successfully for Power BI")

# -------------------------------
# PROJECT SUMMARY (PRINT OUTPUT)
# -------------------------------
print("\n" + "="*50)
print("PROJECT SUMMARY")
print("="*50)

print("""
1. Dataset is highly imbalanced (~0.17% fraud)
2. Rule-based model detects limited fraud cases
3. ML model improved recall using class balancing
4. Trade-off observed: higher detection vs false positives
5. Suitable for business insights & dashboard visualization
""")