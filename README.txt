# Projet IFOAD IA1 - Prédiction de Maladies Cardiaques

Ce projet a été réalisé dans le cadre du module **Intelligence Artificielle & Apprentissage Automatique** (IFOAD IA1). Il s'agit d'un système intelligent capable de **prédire la présence d'une maladie cardiaque** chez un individu à partir de données médicales.

---

## Objectif du projet

Créer un modèle de **Machine Learning** permettant de **classifier** les patients comme étant **malades** ou **non malades** selon des caractéristiques cliniques, puis **déployer une application web** interactive avec **Streamlit**.

---

## Dataset utilisé

**Heart Disease UCI Dataset**  
- Lien : [UCI Repository](https://archive.ics.uci.edu/dataset/45/heart+disease)
- Colonnes principales : âge, sexe, type de douleur thoracique, tension artérielle, cholestérol, fréquence cardiaque maximale, etc.
- Variable cible : `target` (1 = maladie, 0 = pas de maladie)

---

## Technologies utilisées

- Python
- Pandas / Numpy
- Scikit-learn (Machine Learning)
- Matplotlib / Seaborn
- Streamlit (déploiement web)
- joblib (sérialisation du modèle)

---

## Algorithmes testés

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- AdaBoost

---

## Évaluation des modèles

Les modèles ont été comparés selon les métriques suivantes :

- Accuracy
- Précision
- Rappel
- F1-Score
- AUC-ROC

Le **meilleur modèle** (selon le F1-score) a été sauvegardé et intégré à l'application.

---

## Lancer l'application Streamlit

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/projet_ia_ifoad_l3.git
cd projet_ia_ifoad_l3
