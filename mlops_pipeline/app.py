import streamlit as st
import pandas as pd

st.set_page_config(page_title="Monitoreo de Drift", layout="wide")

st.title("🚦 Monitoreo de Drift del Modelo")

# Cargar métricas
try:
    df_drift = pd.read_csv("reports/drift_metrics.csv", index_col=0)
except FileNotFoundError:
    st.error("No se encontró el archivo de métricas. Ejecuta model_monitoring.py primero.")
    st.stop()

# Mostrar tabla
st.subheader("📊 Métricas por variable")
st.dataframe(df_drift)

# Alertas visuales
for col in df_drift.index:
    st.markdown(f"### 🔍 Variable: `{col}`")
    for metric, value in df_drift.loc[col].items():
        if value > 0.2:
            st.error(f"{metric}: {value:.3f} ⚠️ Posible drift")
        else:
            st.success(f"{metric}: {value:.3f} ✅ Estable")

