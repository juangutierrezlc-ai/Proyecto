import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

st.set_page_config(page_title="Monitoreo de Drift", layout="wide")
st.title("📈 Monitoreo de Drift del Modelo")

# Cargar métricas actuales
try:
    df_drift = pd.read_csv(os.path.join("scr", "reports", "drift_metrics.csv"), index_col=0)
except FileNotFoundError:
    st.error("No se encontró el archivo de métricas. Ejecuta model_monitoring.py primero.")
    st.stop()

# Mostrar tabla de métricas
st.subheader("📊 Métricas por variable")
st.dataframe(df_drift)

# Alertas visuales por variable
st.subheader("🚨 Alertas por variable")
for col in df_drift.index:
    st.markdown(f"### 🔍 Variable: {col}")
    for metric, value in df_drift.loc[col].items():
        if value > 0.2:
            st.error(f"{metric}: {value:.3f} ⚠️ Posible drift")
        else:
            st.success(f"{metric}: {value:.3f} ✅ Estable")

# Comparación de distribuciones
st.subheader("📊 Comparación de distribuciones")
try:
    df_actual = pd.read_csv("Base_de_datos.csv")
    df_historico = pd.read_csv("scr/data/historico.csv")
    df_actual["Vehicle_Age"] = 2025 - df_actual["Year"]
    df_historico["Vehicle_Age"] = 2025 - df_historico["Year"]
except:
    st.warning("No se pudieron cargar los datos actuales e históricos para graficar.")
else:
    for col in df_drift.index:
        if col in df_actual.columns and col in df_historico.columns:
            fig, ax = plt.subplots()
            if df_actual[col].dtype != "object":
                sns.kdeplot(df_historico[col], label="Histórico", ax=ax)
                sns.kdeplot(df_actual[col], label="Actual", ax=ax)
            else:
                hist_counts = df_historico[col].value_counts(normalize=True)
                actual_counts = df_actual[col].value_counts(normalize=True)
                df_plot = pd.DataFrame({"Histórico": hist_counts, "Actual": actual_counts}).fillna(0)
                df_plot.plot(kind="bar", ax=ax)
            ax.set_title(f"Distribución: {col}")
            ax.legend()
            st.pyplot(fig)

# Evolución temporal del drift
st.subheader("📈 Evolución temporal del drift")
drift_files = sorted(glob.glob("scr/reports/drift_metrics.csv"))
if drift_files:
    drift_history = []
    for file in drift_files:
        date = os.path.basename(file).split("_")[-1].replace(".csv", "")
        df = pd.read_csv(file, index_col=0)
        df["fecha"] = date
        drift_history.append(df.reset_index())
    df_evol = pd.concat(drift_history)
    variable = st.selectbox("Selecciona variable para ver evolución:", df_evol["index"].unique())
    df_var = df_evol[df_evol["index"] == variable]
    for metric in df_var.columns:
        if metric not in ["index", "fecha"]:
            fig, ax = plt.subplots()
            ax.plot(df_var["fecha"], df_var[metric], marker="o")
            ax.set_title(f"{metric} - {variable}")
            ax.set_ylabel("Valor")
            ax.set_xlabel("Fecha")
            st.pyplot(fig)
else:
    st.info("No hay historial de drift guardado. Ejecuta model_monitoring.py periódicamente con fecha.")

# Recomendaciones
st.subheader("🧠 Recomendaciones")
if (df_drift > 0.2).any().any():
    st.warning("Se detectó drift en al menos una variable. Reentrenamiento recomendado.")
else:
    st.success("El modelo se mantiene estable. No se requieren acciones inmediatas.")


