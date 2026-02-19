❤️ Heart Disease Prediction App

A machine learning–based web application built using Streamlit that predicts the likelihood of heart disease based on user health parameters.
📌 Features

User-friendly Streamlit web interface

Predicts heart disease risk

Uses a trained Logistic Regression model

Handles categorical variables using one-hot encoding

Real-time prediction

Clean and responsive UI

🧠 Machine Learning Model

Algorithm: Logistic Regression

Preprocessing:

Feature scaling using StandardScaler

One-hot encoding for categorical features

Target Variable: Presence of heart disease (0 / 1)

📊 Input Parameters

The model uses the following inputs:

Age

Sex

Chest Pain Type

Resting Blood Pressure

Cholesterol Level

Fasting Blood Sugar

Resting ECG

Max Heart Rate

Exercise-Induced Angina

Oldpeak (ST Depression)

ST Slope

🛠 Tech Stack

Frontend: Streamlit

Backend: Python

ML Library: scikit-learn

Model Serialization: joblib

Data Handling: pandas, numpy

📂 Project Structure
heart_disease_app/
│
├── app.py
├── LR_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md

⚙️ Installation & Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/heart-disease-streamlit.git
cd heart-disease-streamlit

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py

📦 Deployment

The app is deployed using Streamlit Cloud and the source code is hosted on GitHub.

Steps:

Push code to GitHub

Connect GitHub repo to Streamlit Cloud

Select app.py as the main file

Deploy 🚀

📈 Future Improvements

Show prediction probability

Add model comparison

Improve UI design

Add data visualization

Deploy using Docker

👨‍💻 Author

Sumran Harchirkar
AI & Data Science Student
