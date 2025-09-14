import streamlit as st
import pandas as pd
import joblib

# Load full pipelines
model = joblib.load("hybrid_model.pkl")

st.title("Heart Disease Prediction")
st.markdown("""
### Feature Descriptions
- **age**: Age of the patient (in years)  
- **sex**: Gender (1 = male, 0 = female)  
- **cp**: Chest pain type (0–3)  
- **trestbps**: Resting blood pressure (mm Hg)  
- **chol**: Serum cholesterol (mg/dl)  
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)  
- **restecg**: Resting electrocardiographic results (0–2)  
- **thalach**: Maximum heart rate achieved  
- **exang**: Exercise induced angina (1 = yes, 0 = no)  
- **oldpeak**: ST depression induced by exercise (float)  
- **slope**: Slope of the peak exercise ST segment (0–2)  
- **ca**: Number of major vessels (0–3) colored by fluoroscopy  
- **thal**: Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect)  
""")
raw_features = ["age", "sex", "cp", "trestbps", "chol", "fbs",
                "restecg", "thalach", "exang", "oldpeak", "slope",
                "ca", "thal"]

st.sidebar.header("Enter Patient Details")
user_input = {}
for col in raw_features:
    if col == "oldpeak":
        user_input[col] = st.sidebar.number_input(f"{col}", value=0.0, format="%.1f")
    else:
        user_input[col] = st.sidebar.number_input(f"{col}", value=0, step=1)

# Converting to DataFrame
input_data = pd.DataFrame([user_input], columns=raw_features)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Heart Disease Present")
    else:
        st.success("No Heart Disease")




