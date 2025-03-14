import datarobot as dr
import pandas as pd

# 🔹 Conectar con DataRobot
API_KEY = "git remote set-url origin https://github.com/jasaavedra00/agente_estrategico.git"
dr.Client(token=API_KEY, endpoint="https://app.datarobot.com/api/v2")

# 🔹 Cargar los datos de tendencias de marketing
data = {
    "Fecha": ["2024-01-01", "2024-01-02", "2024-01-03"],
    "Engagement_BTL": [87, 90, 85],
    "ROI_Trade": [1.2, 1.5, 1.1],
    "CTR_Digital": [0.05, 0.07, 0.06],
}
df = pd.DataFrame(data)
df.to_csv("datos.csv", index=False)

# 🔹 Subir los datos a DataRobot
dataset = dr.Dataset.create_from_file("datos.csv")
print("📊 Datos subidos correctamente a DataRobot")

# 🔹 Crear y entrenar un modelo
project = dr.Project.create(dataset.id, project_name="Agente Estrategico Marketing")
project.set_target(target="CTR_Digital")
project.wait_for_autopilot()

# 🔹 Seleccionar el mejor modelo
best_model = project.get_models()[0]

# 🔹 Hacer predicciones con nuevos datos
nuevos_datos = pd.DataFrame({"Engagement_BTL": [88], "ROI_Trade": [1.3], "CTR_Digital": [0.06]})
predictions = best_model.predict(nuevos_datos)
print(f"📈 Predicción de CTR Digital: {predictions}")


