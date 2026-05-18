import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("data/train.csv")

# Select features
features = ["GrLivArea","BedroomAbvGr","FullBath","GarageArea","OverallQual","YearBuilt","TotalBsmtSF"]
target = "SalePrice"

df = df[features + [target]]

# Handle missing values
df = df.fillna(df.mean())

# Split data
X = df[features]
y = np.log1p(df["SalePrice"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_train, y_train)
# Evaluate
pred = np.expm1(model.predict(X_test))
print("R2 Score:", r2_score(np.expm1(y_test), pred))

# Save model
model = joblib.load("../model/model.pkl")
print("Model saved!")