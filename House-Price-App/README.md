# 🏠 House Price Prediction App

A Machine Learning powered web application that predicts house prices based on various housing features.

---

## Live Demo

🔗 Streamlit App: https://house-price-predictor-saurav.streamlit.app/

---

## 📌 Project Overview

This project uses a Machine Learning Regression model to estimate house prices using real housing data.

The application is built using:

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

The trained Machine Learning model is deployed on Streamlit Cloud for real-time predictions through an interactive web application.

---

## ⚙️ Features Used

The model predicts house prices based on the following housing features:

- 📐 Living Area
- 🛏 Bedrooms
- 🛁 Bathrooms
- 🚗 Garage Area
- ⭐ Overall Quality
- 🏗 Year Built
- 🧱 Basement Area

---

## 🧠 Machine Learning Model

### Algorithm Used
- Random Forest Regressor

### Evaluation Metric
- R² Score

### Model Accuracy
- 0.87 R² Score

---

## 📸 Application Preview

### 🏠 Main Application Interface

![House Price Prediction App](images/output.png)

> Replace `output.png` with your actual screenshot file name if different.

---

## 📂 Project Structure

```bash
House-Price-App/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── data/
│   └── train.csv
│
├── images/
│   └── output.png
│
├── model/
│   └── model.pkl
│
├── notebook/
│   └── model.py
│
└── README.md
```

---

## ▶️ Run Project Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Saurav-Pandit2005/ML-Projects.git
```

---

### 2️⃣ Navigate to Project Folder

```bash
cd ML-Projects/House-Price-App
```

---

### 3️⃣ Install Required Dependencies

```bash
pip install -r app/requirements.txt
```

---

### 4️⃣ Run Streamlit Application

```bash
streamlit run app/app.py
```

---
