from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import uvicorn

app = FastAPI(title="API de Predicción de Precio de Vehículos")

# Cargar modelo
model = joblib.load("scr/models/best_model.pkl")

# Definir estructura de entrada
class Vehicle(BaseModel):
    Present_Price: float
    Kms_Driven: int
    Fuel_Type: str
    Seller_Type: str
    Transmission: str
    Owner: int
    Year: int

# Endpoint de predicción
@app.post("/predict")
def predict_batch(data: list[Vehicle]):
    df = pd.DataFrame([d.dict() for d in data])
    df["Vehicle_Age"] = 2025 - df["Year"]
    df.drop(columns=["Year"], inplace=True)

    # Preprocesamiento (simplificado)
    df_encoded = pd.get_dummies(df)
    model_features = model.feature_names_in_
    for col in model_features:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[model_features]

    predictions = model.predict(df_encoded)
    return {"predictions": predictions.tolist()}

if __name__ == "__main__":
    uvicorn.run("model_deploy:app", host="0.0.0.0", port=8000, reload=True)