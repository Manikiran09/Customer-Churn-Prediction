Customer Churn Prediction
Customer churn is one of the biggest challenges faced by businesses that rely on subscription-based services. Losing customers not only reduces immediate revenue but can also negatively impact brand loyalty and future growth. Identifying customers who are likely to leave — and understanding why they leave — can help companies take proactive steps to improve customer satisfaction and retention.  
In this project, we build a machine learning-based system to predict customer churn using a real-world dataset.  
The dataset contains detailed information about 10,000 customers, including features such as:  
Demographics: Age, Gender, Geography  
Financial information: Balance, Credit Score, Estimated Salary  
Account activity: Number of products, Active membership status, Tenure (years with bank)  
# 🎯 Objective:
Analyze and understand the key factors influencing customer churn.  
Develop an accurate machine learning model to predict churn.  
Visualize important relationships between features and customer behavior.  
The dataset underwent several important preprocessing steps:  
Removal of irrelevant columns (RowNumber, CustomerId, Surname) to avoid data leakage.  
Encoding categorical variables (Gender with Label Encoding, Geography with One-Hot Encoding).  
Splitting the data into training and testing sets (80% training, 20% testing).  
Balancing the classes using StratifiedSplit to maintain distribution.  
No missing values were present in the dataset.  
Provide actionable insights based on feature importance and customer patterns.  
# ⚙️ How to Run  
1:Clone the repository:  
git clone https://github.com/your-username/customer-churn-prediction.git.  
cd customer-churn-prediction.  
2:Create a virtual Environment:  
python -m venv venv  
venv\Scripts\activate          #Windows
or    
source venv/bin/activate        # Mac/Linux
3:Install Dependencies:  
pip install -r requirements.txt  
4:Run Code:  
python 1_EDA.py  
python 2_modeling.py  
# 🧠 Model Details  
Model Used: Random Forest Classifier  
Performance Metrics:  
Accuracy  
Precision  
Recall  
F1-Score  
Confusion Matrix  
# 📊 Visualizations  
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
