import streamlit as st
import numpy as np
import joblib

# Charger le modèle et le scaler
model = joblib.load("meilleur_modele.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Prédiction Maladie Cardiaque", layout="centered")

st.title("Prédiction de Maladie Cardiaque")
st.markdown("Entrez les informations du patient pour prédire s’il est à risque.")

# Champs d'entrée utilisateur
age = st.slider("Âge", 20, 100, 50)
sex = st.radio("Sexe", ["Homme", "Femme"])
sex = 1 if sex == "Homme" else 0

cp = st.selectbox("Type de douleur thoracique", [0, 1, 2, 3])
trestbps = st.number_input("Pression artérielle au repos", 80, 200, 120)
chol = st.number_input("Taux de cholestérol (mg/dl)", 100, 600, 250)
fbs = st.radio("Glycémie à jeun > 120 mg/dl", ["Oui", "Non"])
fbs = 1 if fbs == "Oui" else 0

restecg = st.selectbox("Résultats électrocardiographiques", [0, 1, 2])
thalach = st.number_input("Fréquence cardiaque maximale", 70, 220, 150)
exang = st.radio("Angine induite par l'exercice", ["Oui", "Non"])
exang = 1 if exang == "Oui" else 0

oldpeak = st.number_input("Oldpeak (ST depression)", 0.0, 10.0, 1.0)
slope = st.selectbox("Pente du segment ST", [0, 1, 2])
ca = st.selectbox("Nbre de vaisseaux colorés", [0, 1, 2, 3])
thal = st.selectbox("Thalassémie", [3, 6, 7])

# Prédiction
if st.button("Prédire"):
    # Créer un vecteur de caractéristiques
    user_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                           restecg, thalach, exang, oldpeak, slope, ca, thal]])

    user_data_scaled = scaler.transform(user_data)
    prediction = model.predict(user_data_scaled)

    if prediction[0] == 1:
        st.error("⚠️ Risque de **maladie cardiaque** détecté !")
    else:
        st.success("✅ Pas de signe de maladie cardiaque détecté.")
