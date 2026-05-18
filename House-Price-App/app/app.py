import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Page config
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

# Load model
model = joblib.load("../model/model.pkl")

# Title
st.title("🏠 House Price Prediction App")
st.markdown("Predict house prices using a Machine Learning model.")

st.divider()

# Sidebar
st.sidebar.header("📌 About This App")

st.sidebar.markdown("""
### 🏠 House Price Prediction

This application predicts house prices using a Machine Learning model trained on real housing data.

---

### ⚙️ Features Used
- 📐 Living Area  
- 🛏 Bedrooms  
- 🛁 Bathrooms  
- 🚗 Garage Area  
- ⭐ Overall Quality  
- 🏗 Year Built  
- 🧱 Basement Area  
---

### 🎯 Purpose
This project demonstrates how Machine Learning can be used to solve real-world regression problems and deliver predictions through an interactive web interface.
""")

# Input Section
st.header("Enter House Details")

col1, col2 = st.columns(2)

with col1:
    area = st.slider("Living Area (sq ft)", 300, 5000, 1500)
    bedrooms = st.slider("Bedrooms", 1, 10, 3)
    bathrooms = st.slider("Bathrooms", 1, 5, 2)
    year = st.slider("Year Built", 1900, 2025, 2000)

with col2:
    garage = st.slider("Garage Area", 0, 1000, 400)
    quality = st.slider("Overall Quality (1-10)", 1, 10, 5)
    basement = st.slider("Basement Area", 0, 2000, 500)  

st.divider()

st.write("Click the button to predict house price")

# Prediction
if st.button("Predict Price"):

    if area <= 0:
        st.error("Area must be greater than 0")

    else:
        # Feature names (must match training)
        features = ["GrLivArea","BedroomAbvGr","FullBath","GarageArea","OverallQual","YearBuilt","TotalBsmtSF"]

        # Convert to DataFrame
        input_data = pd.DataFrame(
            [[area, bedrooms, bathrooms, garage, quality, year, basement]],
            columns=features
        )

        # Prediction
        prediction = np.expm1(model.predict(input_data))
        price = prediction[0]

        # Output
        st.success(f"💰 Estimated Price: ₹ {price:,.0f}")

        # Price Category
        if price < 150000:
            st.warning("💸 Budget House")
        elif price < 300000:
            st.info("🏡 Mid-range House")
        else:
            st.success("🏰 Luxury House")

        # Input Summary
        summary_df = pd.DataFrame({
            "Feature": [
                "Living Area",
                "Bedrooms",
                "Bathrooms",
                "Garage Area",
                "Quality",
                "Year Built",
                "Basement Area"
            ],
            "Value": [
                area,
                bedrooms,
                bathrooms,
                garage,
                quality,
                year,
                basement
            ]
        })

        st.subheader("Input Summary")
        st.table(summary_df)

        # Feature Importance (safe)
        if hasattr(model, "feature_importances_"):
            importance = model.feature_importances_

            st.subheader("Feature Importance")

            st.bar_chart(
                pd.DataFrame(
                    importance,
                    index=features,
                    columns=["Importance"]
                )
            )
        else:
            st.warning("Feature importance not available for this model.")
