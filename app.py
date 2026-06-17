import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Heart Disease Risk Predictor", layout="centered")
st.title("10-Year Heart Disease Risk Predictor")
st.write("Enter the patient's clinical data below to assess their 10-year cardiovascular disease risk using our Machine Learning model.")

# 2. Load the trained model
@st.cache_resource
def load_model():
    return joblib.load('heart_disease_model.pkl')

model = load_model()

# The optimal threshold found via Youden's J statistic
OPTIMAL_THRESHOLD = 0.45 

# 3. Sidebar for Patient Input
st.sidebar.header("Patient Information")

age = st.sidebar.number_input("Age", min_value=30, max_value=100, value=50)
is_male = st.sidebar.selectbox("Gender", options=[("Male", 1), ("Female", 0)], format_func=lambda x: x[0])[1]
cigsPerDay = st.sidebar.number_input("Cigarettes per Day", min_value=0, max_value=60, value=0)
sysBP = st.sidebar.number_input("Systolic BP (sysBP)", min_value=80, max_value=250, value=120)
diaBP = st.sidebar.number_input("Diastolic BP (diaBP)", min_value=50, max_value=150, value=80)
totChol = st.sidebar.number_input("Total Cholesterol", min_value=100, max_value=500, value=200)
glucose = st.sidebar.number_input("Glucose Level", min_value=40, max_value=400, value=80)


input_data = {
    'is_male': is_male, 'age': age, 'education': 1.0, 'currentSmoker': 1 if cigsPerDay > 0 else 0,
    'cigsPerDay': cigsPerDay, 'BPMeds': 0.0, 'prevalentStroke': 0, 'prevalentHyp': 0,
    'diabetes': 0, 'totChol': totChol, 'sysBP': sysBP, 'diaBP': diaBP,
    'BMI': 25.0, 'heartRate': 75.0, 'glucose': glucose
}

# 4. Prediction Logic
if st.button("🔍 Predict Risk", type="primary"):

    df_input = pd.DataFrame([input_data])
    

    df_input['PulsePressure'] = df_input['sysBP'] - df_input['diaBP']
    df_input['Age_Cigs_Risk'] = df_input['age'] * df_input['cigsPerDay']
    

    probability = model.predict_proba(df_input)[0][1]
    
    # Display Results
    st.markdown("---")
    st.subheader("Assessment Report")
    
    if probability >= OPTIMAL_THRESHOLD:
        st.error(f"**HIGH RISK DETECTED** (Probability: {probability:.1%})")
        st.write("> The model indicates a significant risk of developing Coronary Heart Disease (CHD) within the next 10 years. Immediate medical consultation and further clinical screenings are strongly advised.")
    else:
        st.success(f"**LOW RISK** (Probability: {probability:.1%})")
        st.write("> The patient is currently at a lower risk for cardiovascular issues. It is recommended to maintain a healthy lifestyle and routine check-ups.")