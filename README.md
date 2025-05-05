
# 🏥 Insurance Claim Cost Predictor

A **Streamlit web app** that predicts medical insurance charges based on user input using a machine learning model trained on the `insurance.csv` dataset.

## 🔍 Features
- Predicts charges in **USD** using age, sex, BMI, smoker status, number of children, and region
- Uses a trained **Random Forest Regressor** or **Linear Regression** model
- Fully interactive web UI powered by **Streamlit**

## 🚀 How to Run Locally

1. Clone the repository or download the files
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
streamlit run insurance_predictor_app.py
```

## 🧠 Model
The model (`insurance_claim_model.pkl`) is trained using scikit-learn on the features:
- Age
- BMI
- Number of children
- Encoded categorical features (sex, smoker, region)

## 📦 Files Included
- `insurance_predictor_app.py` – Streamlit web app
- `insurance_claim_model.pkl` – Trained model
- `requirements.txt` – Python dependencies
- `README.md` – This file

## 📡 Optional: Deploy on Streamlit Cloud
- Upload this repo to GitHub
- Go to [streamlit.io/cloud](https://streamlit.io/cloud)
- Connect your GitHub repo and deploy the app!

---
