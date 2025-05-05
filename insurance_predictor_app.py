
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("insurance_claim_model.pkl")

st.title("🏥 Insurance Claim Cost Predictor")

st.write("Fill in the information below to predict the insurance charges:")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=5, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Encode inputs
sex_male = 1 if sex == "male" else 0
smoker_yes = 1 if smoker == "yes" else 0
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# DataFrame for prediction
input_data = pd.DataFrame([{
    'age': age,
    'bmi': bmi,
    'children': children,
    'sex_male': sex_male,
    'smoker_yes': smoker_yes,
    'region_northwest': region_northwest,
    'region_southeast': region_southeast,
    'region_southwest': region_southwest
}])

# Predict
if st.button("Predict Charges"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Insurance Charges: ${prediction:.2f}")
