import pandas as pd
import joblib

# Load models and scalers
model_young = joblib.load("artifacts/model_young.joblib")
model_rest = joblib.load("artifacts/model_rest.joblib")
scaler_young = joblib.load("artifacts/scaler_young.joblib")
scaler_rest = joblib.load("artifacts/scaler_rest_.joblib")

def calculate_normalized_risk(medical_history):
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }
    diseases = medical_history.lower().split(" & ")
    total_risk_score = sum(risk_scores.get(disease.strip(), 0) for disease in diseases)

    max_score = 14
    normalized_risk_score = (total_risk_score) / max_score
    return normalized_risk_score

def preprocess_input(input_dict):
    # Normalize keys to lowercase for consistency
    input_dict = {k.strip().lower(): v for k, v in input_dict.items()}

    expected_columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk', 'normalized_risk_score',
        'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
        'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    insurance_plan_encoding = {'bronze': 1, 'silver': 2, 'gold': 3}
    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    # Binary/categorical encoding
    if input_dict.get('gender') == 'Male':
        df['gender_Male'] = 1

    region_map = {
        'northwest': 'region_Northwest',
        'southeast': 'region_Southeast',
        'southwest': 'region_Southwest'
    }
    region_col = region_map.get(input_dict.get('region', '').lower())
    if region_col:
        df[region_col] = 1

    if input_dict.get('marital status') == 'Unmarried':
        df['marital_status_Unmarried'] = 1

    bmi_map = {
        'obesity': 'bmi_category_Obesity',
        'overweight': 'bmi_category_Overweight',
        'underweight': 'bmi_category_Underweight'
    }
    bmi_col = bmi_map.get(input_dict.get('bmi category', '').lower())
    if bmi_col:
        df[bmi_col] = 1

    smoking_map = {
        'occasional': 'smoking_status_Occasional',
        'regular': 'smoking_status_Regular'
    }
    smoking_col = smoking_map.get(input_dict.get('smoking status', '').lower())
    if smoking_col:
        df[smoking_col] = 1

    employment_map = {
        'salaried': 'employment_status_Salaried',
        'self-employed': 'employment_status_Self-Employed'
    }
    employment_col = employment_map.get(input_dict.get('employment status', '').lower())
    if employment_col:
        df[employment_col] = 1

    df['insurance_plan'] = insurance_plan_encoding.get(input_dict.get('insurance plan', '').lower(), 1)

    # Assign numerical values
    df['age'] = input_dict.get('age', 0)
    df['number_of_dependants'] = input_dict.get('number of dependants', 0)
    df['income_lakhs'] = input_dict.get('income in lakhs', 0)
    df['genetical_risk'] = input_dict.get('genetical risk', 0)

    df['normalized_risk_score'] = calculate_normalized_risk(input_dict.get('medical history', 'no disease'))

    df = handle_scaling(df['age'].values[0], df)
    return df

def handle_scaling(age, df):
    scaler_object = scaler_young if age <= 25 else scaler_rest

    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']

    df['income_level'] = 0  # temporary placeholder
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df.drop('income_level', axis=1, inplace=True)

    return df

def predict(input_dict):
    processed_df = preprocess_input(input_dict)
    age = input_dict.get('age') or input_dict.get('Age')  # fallback in case main.py didn't lowercase

    model = model_young if age <= 25 else model_rest
    prediction = model.predict(processed_df)

    return {
        "predicted_cost": int(prediction[0]),
        "model_used": "young" if age <= 25 else "rest"
    }
