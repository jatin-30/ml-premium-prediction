# 💸 Health Insurance Premium Predictor

A Streamlit web application that predicts health insurance premium costs based on user inputs such as age, income, lifestyle, and medical history. It leverages machine learning models trained on structured data to provide accurate and personalized premium estimates.

---

## 🚀 Features

- 📊 Predicts health insurance premium based on personal, lifestyle, and medical inputs
- 🤖 Two separate ML models optimized for young (≤ 25) and older (> 25) individuals
- 🎛️ Intuitive and responsive web UI built with Streamlit
- 🔁 Scales input features dynamically using age-appropriate scalers
- 📦 Modular backend with clean preprocessing and prediction logic

---

## 🛠️ Tech Stack

| Component     | Tech                       |
|---------------|----------------------------|
| Frontend UI   | Streamlit                  |
| Backend Logic | Python, pandas, joblib     |
| ML Models     | scikit-learn (trained separately) |
| Deployment    | Localhost / Streamlit Cloud |

---

## 🧪 How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/jatin-30/ml-premium_prediction.git
cd premium_prediction/app

2. **Install Dependencaies**

pip install -r requirements.txt

3. **Run the streamlit app**

streamlit run main.py
