import streamlit as st
import pandas as pd
import numpy as np
import joblib
import random

model = joblib.load("pipeline.pkl") 

st.title("Depression Predictor")
st.write("Answer the questions below to get a prediction.")

random_id = random.randint(1000, 9999)

gender = st.selectbox("Gender", ['Male', 'Female'])

age = st.selectbox("Age Range", ['31-35', '21-25', '26-30', '>35', '16-20'])

city_list = [
    "Delhi", "Mumbai", "Bengaluru", "Hyderabad", "Ahmedabad", "Chennai", 
    "Kolkata", "Pune", "Jaipur", "Lucknow", "Surat", "Kanpur", "Nagpur", 
    "Indore", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Chandigarh"
]
city = st.selectbox("City", city_list)

acad_pressure = st.slider("Academic Pressure", 0, 5, 2)

work_pressure = st.slider("Work Pressure", 0, 5, 2)

cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.01, format="%.2f")

study_satisfaction = st.slider("Study Satisfaction", 0, 5, 3)

job_satisfaction = st.slider("Job Satisfaction", 0, 5, 3)

sleep_duration = st.selectbox("Sleep Duration", ['5-6 hours', 'Less than 5 hours', '7-8 hours', 'More than 8 hours'])

dietary_habits = st.selectbox("Dietary Habits", ['Healthy', 'Moderate', 'Unhealthy', 'Others'])

degree_list = [
    'B.Pharm', 'BSc', 'BA', 'BCA', 'M.Tech', 'PhD', 'B.Ed', 'LLB', 'BE', 'M.Ed', 
    'MSc', 'BHM', 'M.Pharm', 'MCA', 'MA', 'B.Com', 'MD', 'MBA', 'MBBS', 'M.Com', 
    'B.Arch', 'LLM', 'B.Tech', 'BBA', 'ME', 'MHM'
]
degree = st.selectbox("Degree", degree_list)

suicidal_thoughts = st.selectbox("Suicidal Thoughts", ['Yes', 'No'])

study_hours = st.number_input("Study Hours per day", min_value=0, max_value=24, step=1)

financial_stress = st.slider("Financial Stress", 0, 5, 2)

family_history_mental_illness = st.selectbox("Family History of Mental Illness", ['Yes', 'No'])

if st.button("Predict"):
    input_data = pd.DataFrame([[
        random_id, gender, age, city, acad_pressure, work_pressure, cgpa, 
        study_satisfaction, job_satisfaction, sleep_duration, dietary_habits, 
        degree, suicidal_thoughts, study_hours, financial_stress, 
        family_history_mental_illness
    ]], columns=[
        "id","gender", "age", "city", "acad_pressure", "work_pressure", 
        "cgpa", "study_satisfaction", "job_satisfaction", "sleep_duration", 
        "dietary_habits", "degree", "suicidal_thoughts", "study_hours", 
        "financial_stress", "family_history_mental_illness"
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("You might have depression.")
    else:
        st.success("You probably do not have depression.")
