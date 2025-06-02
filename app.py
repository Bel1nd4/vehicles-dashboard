import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de vehículos usados")

# Leer datos
df = pd.read_csv('vehicles_us.csv')

# Vista previa
st.write("Vista previa del dataset:")
st.write(df.head())

# Gráfico de dispersión
fig1 = px.scatter(df, x="odometer", y="price", title="Precio vs Kilometraje")
st.plotly_chart(fig1)

# Histograma
fig2 = px.histogram(df, x="odometer", nbins=50, title="Distribución del Kilometraje")
st.plotly_chart(fig2)

import streamlit as st
import pandas as pd
import plotly.express as px

# Título principal
st.title("Dashboard de vehículos usados")

# Encabezado de sección
st.header("Exploración interactiva de datos")

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Vista previa rápida
st.write("Vista previa del dataset:")
st.write(car_data.head())

# Botón para construir el histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para el kilometraje de los vehículos")
    
    # Crear el gráfico
    fig = px.histogram(car_data, x="odometer",
                       nbins=50,
                       title="Distribución del Kilometraje")
    
    # Mostrar el gráfico (con clave única para evitar errores)
    st.plotly_chart(fig, use_container_width=True, key="histograma_kilometraje")

# Botón para construir gráfico de dispersión
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión entre precio y kilometraje")

    fig2 = px.scatter(car_data, x="odometer", y="price",
                      title="Precio vs Kilometraje",
                      labels={"odometer": "Kilometraje", "price": "Precio (USD)"})
    
    st.plotly_chart(fig2, use_container_width=True, key="scatter_plot")


