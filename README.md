Customer Churn Prediction
Objective
The goal of this project is to predict whether a customer will discontinue a subscription-based service (churn) based on their account information and demographics.
Early identification of customers at risk can help businesses take preventive actions.
customer-churn-prediction/
│
├── data/
│   └── Churn_Modelling.csv    # Dataset
│
├── 1_EDA.py                   # Exploratory Data Analysis
├── 2_modeling.py               # Model Training and Evaluation
├── README.md                   # Project Documentation
├── requirements.txt            # Required Python packages

Dataset:
Source: Kaggle - Bank Customer Churn Prediction Dataset
Description: 10,000 customers' demographic data, credit scores, balances, and churn labels
How to Run:
1:Clone the repository:
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
2:Create a virtual Environment:
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # Mac/Linux
3:Install Dependencies:
pip install -r requirements.txt
4:Run Code:
python 1_EDA.py
python 2_modeling.py
Machine Learning Model
Model Used: Random Forest Classifier
Performance Metrics:
Accuracy
Precision
Recall
F1-Score
Confusion Matrix
Visualizations:
Churn Distribution
Churn by Gender and Geography
Correlation Heatmap
Confusion Matrix Heatmap
Top 10 Important Features (Feature Importance Plot)
Key Insights:
Age and balance significantly impact churn.
Customers in Germany showed higher churn rates.
Inactive members and those with high balance are more likely to leave.
Acknowledgements
Dataset by Shantanu Dhakad on Kaggle


