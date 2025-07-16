import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Premium Predictor", layout="wide")

st.markdown("""
    <style>
        .big-font {
            font-size: 22px !important;
        }
        .result-card {
            padding: 1rem;
            border-radius: 10px;
            background-color: #f0f2f6;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            font-weight: bold;
            color: #2c3e50;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.title("Health Insurance Premium Predictor")
st.markdown("Use this tool to estimate your **health insurance cost** based on various personal and medical attributes.")

# Categorical options
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Layout with containers
with st.container():
    st.subheader("Personal & Financial Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=18, step=1, max_value=100)
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with col2:
        number_of_dependants = st.number_input('Dependants', min_value=0, step=1, max_value=20)
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
    with col3:
        income_lakhs = st.number_input('Annual Income (in Lakhs)', step=1, min_value=0, max_value=200)
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

with st.container():
    st.subheader("Health Information")
    col4, col5, col6 = st.columns(3)
    with col4:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
    with col5:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with col6:
        genetical_risk = st.number_input('Genetical Risk (0–5)', step=1, min_value=0, max_value=5)

with st.container():
    st.subheader("Additional Info")
    col7, col8, col9 = st.columns(3)
    with col7:
        region = st.selectbox('Region', categorical_options['Region'])
    with col8:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])
    with col9:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])

# Input dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Prediction Button
st.markdown("---")
if st.button("Predict Premium", use_container_width=True):
    result = predict(input_dict)
    predicted_cost = result['predicted_cost']
    st.markdown(f"<div class='result-card'>Predicted Premium: {predicted_cost}</div>", unsafe_allow_html=True)


