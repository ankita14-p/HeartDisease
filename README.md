# ❤️ Heart Disease Prediction App

A machine learning web application built with **Streamlit** that predicts the likelihood of heart disease based on patient health parameters.

🚀 Live App: https://heartdiseaseusinghybridmodel.streamlit.app/

---

## 📌 Overview
This project uses a **stacking classifier** (ensemble of multiple models) trained on the Heart Disease dataset.  
The frontend is developed with **Streamlit** and deployed on **Streamlit Community Cloud**.

---

## ⚙️ Features
- User-friendly web interface to input patient data.
- Preprocessing pipeline: scaling, feature selection, variance threshold.
- Machine learning model: **Stacking Classifier** with base learners and meta-model.
- Prediction output:  
  - 🟢 *No Heart Disease* (0)  
  - 🚨 *Heart Disease Present* (1)

---

## 🗂️ Project Structure
heart-disease-app/
│
├── app.py # Streamlit app
├── hybrid_model.pkl # Trained stacking model (with preprocessing)
├── requirements.txt # Dependencies
└── README.md # Project description

## 🚀 How to Run Locally
1. Clone the repo
2. Install dependencies:

pip install -r requirements.txt

3.Run the app:

streamlit run app.py
