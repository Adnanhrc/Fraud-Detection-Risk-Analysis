# 🚀 📊 Fraud Detection & Risk Analysis

## 📌 Overview

This project focuses on detecting fraudulent financial transactions using a combination of **rule-based logic and machine learning techniques**.

It simulates a real-world fraud analytics use case similar to those handled by consulting firms and financial institutions, working with a highly **imbalanced dataset (~0.17% fraud rate)**.

The project demonstrates how to move from **basic rule-based detection → machine learning models → business insights via dashboards**.

---

## 🚀 Key Features

* Analysis of **280K+ financial transactions**
* Handling highly imbalanced fraud dataset
* Rule-based fraud detection system
* Machine Learning model (Logistic Regression)
* Feature engineering for anomaly detection
* Model evaluation using real-world metrics
* Interactive Power BI dashboard for business insights

---

## 📊 Dataset Information

* 📦 Total Transactions: **284,807**
* 🚨 Fraud Cases: **492 (~0.17%)**
* 📍 Source: Kaggle Credit Card Fraud Dataset

⚠️ Dataset not included due to size limitations
👉 Download: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---

## 🎯 Business Objective

This project helps financial institutions to:

* Identify suspicious transaction patterns
* Detect fraudulent activities early
* Reduce financial losses
* Improve fraud monitoring systems
* Support data-driven risk strategies

---

## 🛠️ Tools & Technologies

* Python (Pandas, NumPy)
* Scikit-learn (Logistic Regression)
* Power BI (Dashboard)
* VS Code
* Git & GitHub

---

## ⚙️ Feature Engineering

To simulate real-world fraud detection logic, the following features were created:

* 🔹 High Transaction Flag (Top 5% transactions)
* 🔹 Hour of Transaction (time-based behavior)
* 🔹 Night Transaction Indicator (0–6 AM risk window)
* 🔹 Z-score for transaction amount (anomaly detection)
* 🔹 Extreme Transaction Flag (outliers)

---

## 🔍 Rule-Based Model

A business-driven risk scoring system was implemented:

* High transaction amount → higher risk
* Night transactions → moderate risk
* Extreme values → strong anomaly signal

📊 Results:

* Detected limited fraud cases
* High number of false positives
* Highlights limitations of static rule-based systems

---

## 🤖 Machine Learning Model

* Model Used: **Logistic Regression**

⚙️ Key Improvement:

* Applied `class_weight = 'balanced'` to handle class imbalance

📊 Results:

* Fraud Detection Recall: **~34%**
* Significant improvement from baseline (~0%)
* Trade-off: Increased false positives

---

## 📈 Model Evaluation Insights

* Accuracy is misleading in imbalanced datasets
* Recall is the most critical metric for fraud detection
* Precision vs Recall trade-off is unavoidable
* Model reflects real-world fraud detection challenges

---

## 📊 Power BI Dashboard

### 🔹 Overview Page

* Total Transactions
* Fraud Count
* Fraud Percentage

### 🔹 Fraud Analysis

* High amount vs fraud correlation
* Time-based fraud patterns
* Night transaction risk analysis

### 🔹 Model Performance

* Fraud detected vs missed
* Confusion matrix visualization

---

## 📸 Dashboard Preview

![Dashboard](images/fraud_dashboard.png)

---



## 📥 How to Run the Project

### 1️⃣ Data Setup

* Download dataset from Kaggle
* Load into Python environment

### 2️⃣ Model Building

* Perform feature engineering
* Train Logistic Regression model
* Evaluate performance metrics

### 3️⃣ Power BI Dashboard

* Load processed data
* Create visuals and KPIs
* Analyze fraud patterns

---

## 📈 Business Value

This project helps organizations to:

* Detect high-risk transactions
* Improve fraud monitoring systems
* Understand limitations of rule-based detection
* Implement ML-based fraud detection strategies

---

## 💡 Key Learnings

* Handling imbalanced datasets is critical
* Accuracy alone is not a reliable metric
* Feature engineering plays a major role
* Real-world models require trade-offs

---

## 🔮 Future Improvements

* Apply advanced models (Random Forest, XGBoost)
* Use SMOTE for class imbalance handling
* Optimize model thresholds
* Improve precision-recall balance
* Deploy real-time fraud detection pipeline

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📬 Contact
Adnan 

LinkedIn: https://www.linkedin.com/in/adnanhrc/  
Email: mohammadnan88@gmail.com

---

## 💡 Why This Project Matters

* Demonstrates **end-to-end data science workflow (EDA → Feature Engineering → ML → BI)**
* Solves a **real-world financial fraud problem**
* Handles **highly imbalanced datasets**
* Strong project for **data analyst, risk analyst, and fintech roles**

---

⭐ If you found this project useful, consider giving it a star!
