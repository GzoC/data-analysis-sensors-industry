import pandas as pd  # Para manipulación de datos
import streamlit as st  # Para crear el dashboard interactivo
import matplotlib.pyplot as plt  # Para gráficos

# Título del dashboard
st.title("Dashboard Interactivo: Análisis de Sensores de Máquinas")

# Descripción del proyecto
st.markdown("""
Este dashboard permite analizar los datos de sensores industriales. 
Puedes cargar un archivo CSV para visualizar las métricas y explorar los datos a través de gráficos interactivos.
""")

# Subir archivo CSV
uploaded_file = st.file_uploader("Sube un archivo CSV con los datos de sensores", type="csv")

if uploaded_file:
    # Leer el archivo CSV subido
    df = pd.read_csv(uploaded_file)
    
    # Mostrar las primeras filas del dataframe
    st.subheader("Vista Previa de los Datos")
    st.dataframe(df.head())

    # Convertir la columna de tiempo a datetime (si aplica)
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)
    
    # Mostrar estadísticas descriptivas
    st.subheader("Estadísticas Descriptivas")
    st.write(df.describe())

    # Visualización interactiva
    st.subheader("Gráficos Interactivos")
    variables = st.multiselect("Selecciona las variables a graficar", df.columns.tolist(), default=df.columns.tolist())
    
    if variables:
        st.line_chart(df[variables])
