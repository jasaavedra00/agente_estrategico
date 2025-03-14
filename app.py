import streamlit as st
import datarobot as dr
import pandas as pd

# Conectar con DataRobot
API_KEY = "git remote set-url origin https://github.com/jasaavedra00/agente_estrategico.git"
dr.Client(token=API_KEY, endpoint="https://app.datarobot.com/api/v2")

# Interfaz en Streamlit
st.title("📊 Agente Estratégico de Marketing")

uploaded_file = st.file_uploader("Sube un archivo CSV con datos", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("✅ Datos cargados:")
    st.dataframe(df)

    # Predicciones con DataRobot
    project = dr.Project.list()[0]
    best_model = project.get_models()[0]
    predictions = best_model.predict(df)

    st.write("📈 Predicciones:")
    st.write(predictions)
