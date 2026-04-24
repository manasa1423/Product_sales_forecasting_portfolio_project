# Product_sales_forecasting_portfolio_project
# 📈 Product Sales Forecasting & Deployment (Flask API)

## 🔹 Problem Statement
Businesses invest heavily in marketing channels such as TV, Radio, and Newspaper ads.  
The goal of this project is to build a machine learning model that predicts **product sales** based on advertising spend and deploy it as a **Flask API** for real-time predictions.

---

## 🎯 Target Metric
We aimed to minimize prediction error using regression models and evaluated performance using:
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

---

## 📊 Exploratory Data Analysis (EDA)
Key insights discovered:
- Strong positive correlation between **TV advertising and Sales**
- Radio advertising also significantly impacts sales
- Newspaper advertising has weaker correlation
- Data showed linear relationships suitable for regression models

---

## 🧪 Hypothesis Testing
Hypothesis:
- H₀: Advertising has no effect on Sales  
- H₁: Advertising significantly affects Sales  

Result:  
Statistical analysis confirmed advertising spend strongly impacts sales.

---

## 🤖 Machine Learning Modelling
Models tested:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor (Final Model)

### ⭐ Final Model: Random Forest Regressor
Reason:
- Captured non-linear relationships
- Achieved best accuracy among tested models

---

## 📈 Final Model Performance
- R² Score: **~0.97**
- RMSE: **Low error**
- Model generalizes well on unseen data.

---

## 🚀 Deployment using Flask API
The trained model was deployed as a REST API.

### API Endpoint
