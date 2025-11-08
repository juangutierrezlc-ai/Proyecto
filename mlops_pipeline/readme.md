# Proyecto Final Machine Learning — Predicción de precios de vehículos

## 🎯 Caso de negocio
La empresa busca predecir el precio de venta de vehículos usados para optimizar sus estrategias de compra y venta.

## 📁 Estructura del proyecto
- `comprension_eda.ipynb`: Exploración de datos
- `ft_engineering.py`: Ingeniería de características
- `model_training_evaluation.py`: Entrenamiento y evaluación
- `model_monitoring.py`: Monitoreo de drift
- `model_deploy.py`: Despliegue del modelo
- `app.py`: Visualización en Streamlit

## 📊 Principales hallazgos
- Alta correlación entre `Present_Price` y `Selling_Price`
- `Fuel_Type` y `Transmission` influyen en el precio
- El modelo seleccionado fue `GradientBoostingRegressor` con R² de 0.91

## 🔍 Monitoreo
Se implementaron métricas de drift como KS test, PSI, JS divergence y Chi-cuadrado. La app en Streamlit permite visualizar alertas y evolución temporal.

## 🚀 Ejecución
```bash
streamlit run app.py
