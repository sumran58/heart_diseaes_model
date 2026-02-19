import pandas as pd
import streamlit as st
import joblib
#lets do unpickling of all the files that we have stored using joblib
model=joblib.load(r"C:\Users\windows\Desktop\projects\heart_disease\LR_heart.pkl")
scaler=joblib.load(r"C:\Users\windows\Desktop\projects\heart_disease\scaler.pkl")
columns=joblib.load(r"C:\Users\windows\Desktop\projects\heart_disease\columns.pkl")

#win+ . is for emoji 
st.title("Heart stoke Prediction❤️")
st.markdown("Provide the following details")
age=st.slider("Age",18,100,40)
sex = st.selectbox("Sex", ["M", "F"])

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "TA", "ASY"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=200,
    value=120
)

cholesterol = st.number_input(
    "Cholesterol (mg/dL)",
    min_value=100,
    max_value=600,
    value=200
)

fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dL",
    [0, 1]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.slider(
    "Max Heart Rate",
    60,
    220,
    150
)

exercise_angina = st.selectbox(
    "Exercise-Induced Angina",
    ["Y", "N"]
)

oldpeak = st.slider(
    "Oldpeak (ST Depression)",
    0.0,
    6.0,
    1.0
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)
if st.button("Predict"):
    raw_input = {
        # Numerical features (used directly)
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,

        # One-hot encoded categorical features
        "Sex_M": 1 if sex == "M" else 0,
        "Sex_F": 1 if sex == "F" else 0,

        "ChestPainType_ATA": 1 if chest_pain == "ATA" else 0,
        "ChestPainType_NAP": 1 if chest_pain == "NAP" else 0,
        "ChestPainType_TA": 1 if chest_pain == "TA" else 0,
        "ChestPainType_ASY": 1 if chest_pain == "ASY" else 0,

        "RestingECG_Normal": 1 if resting_ecg == "Normal" else 0,
        "RestingECG_ST": 1 if resting_ecg == "ST" else 0,
        "RestingECG_LVH": 1 if resting_ecg == "LVH" else 0,

        "ExerciseAngina_Y": 1 if exercise_angina == "Y" else 0,
        "ExerciseAngina_N": 1 if exercise_angina == "N" else 0,

        "ST_Slope_Up": 1 if st_slope == "Up" else 0,
        "ST_Slope_Flat": 1 if st_slope == "Flat" else 0,
        "ST_Slope_Down": 1 if st_slope == "Down" else 0
    }

    # Convert dictionary to DataFrame
    input_df = pd.DataFrame([raw_input])

    st.write("Model Input Data")
    st.dataframe(input_df)
        # Align columns with training 
        #reindex(columns=columns, fill_value=0) ensures that the input data has the same features and order as the training data, filling missing one-hot encoded columns with zero to avoid prediction errors.
    input_df = input_df.reindex(columns=columns, fill_value=0)

    # Scale the input
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0][1]

    # Display result
    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Disease\n\nProbability: {probability:.2%}")
    else:
        st.success(f"✅ Low Risk of Heart Disease\n\nProbability: {probability:.2%}")
