🚀 📊 Fraud Detection & Risk Analysis
📌 Project Overview

This project focuses on detecting fraudulent financial transactions using both rule-based logic and machine learning techniques. It simulates a real-world fraud analytics scenario similar to those handled by consulting firms like Deloitte.

The dataset contains over 280,000 transactions with a highly imbalanced fraud rate (~0.17%), making it a challenging and realistic problem.

🎯 Objectives
Identify suspicious transaction patterns
Build a rule-based fraud detection system
Apply machine learning for improved detection
Evaluate model performance using real metrics
Create a business-ready dashboard (Power BI)
📂 Dataset
Source: Kaggle Credit Card Fraud Dataset
Total Transactions: 284,807
Fraud Cases: 492 (~0.17%)

⚠️ Note: Dataset is not included due to size limitations.
👉 Download here:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

🛠️ Tools & Technologies
Python (Pandas, NumPy)
Scikit-learn (Logistic Regression)
Power BI (Dashboard)
VS Code
Git & GitHub
⚙️ Feature Engineering

To simulate real-world fraud detection logic, the following features were created:

🔹 High Transaction Flag (Top 5% transactions)
🔹 Hour of Transaction (time-based behavior)
🔹 Night Transaction Indicator (0–6 AM risk window)
🔹 Z-score for Amount (statistical anomaly detection)
🔹 Extreme Transaction Flag (outliers)
🔍 Rule-Based Model

A risk scoring system was designed using business rules:

High amount → higher risk
Night transaction → moderate risk
Extreme value → strong anomaly
📊 Result:
Detected limited fraud cases
High number of false positives
Demonstrates limitations of static rules
🤖 Machine Learning Model

Model used: Logistic Regression

⚙️ Key Improvement:
Applied class_weight='balanced' to handle dataset imbalance
📊 Results:
Fraud Detection Recall: ~34%
Significant improvement from initial 0%
Trade-off: Increased false positives
📈 Model Evaluation Insights
Accuracy is misleading due to class imbalance
Recall is more important for fraud detection
Trade-off between precision vs recall
Model highlights real-world challenges in fraud analytics
📊 Power BI Dashboard

The dashboard provides business insights:

🔹 Overview Page
Total Transactions
Fraud Count
Fraud Percentage
🔹 Fraud Analysis
High Amount vs Fraud
Time-based fraud patterns
Night transaction analysis
🔹 Model Performance
Fraud detected vs missed
Visual representation of confusion matrix
💼 Business Impact
Identifies high-risk transactions
Helps financial institutions monitor fraud
Demonstrates limitations of rule-based systems
Recommends advanced ML for better detection
🏆 Key Learnings
Handling imbalanced datasets is critical
Accuracy alone is not a good metric
Feature engineering is crucial in fraud detection
Trade-offs are inevitable in real-world models
🔮 Future Improvements
Apply advanced models (Random Forest, XGBoost)
Use SMOTE for imbalance handling
Tune model thresholds
Improve precision-recall balance
👨‍💻 Author

Adnan
Aspiring Data Analyst | Fraud & Risk Analytics Enthusiast
