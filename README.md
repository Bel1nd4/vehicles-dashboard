# vehicles-dashboard
# Dashboard de Vehículos Usados

Esta es una aplicación web interactiva desarrollada con Streamlit para explorar un conjunto de datos de anuncios de venta de coches en Estados Unidos.

## 📊 Funcionalidades principales

- Visualización de una tabla con los primeros registros del dataset.
- Histograma del kilometraje (`odometer`) de los vehículos.
- Gráfico de dispersión entre `odometer` y `price` para analizar la relación entre kilometraje y precio.
- Interacción a través de casillas de verificación que permiten activar/desactivar cada gráfico.

## ⚙️ Herramientas utilizadas

- Python
- Streamlit
- pandas
- plotly-express

## 📁 Cómo ejecutar

1. Clona el repositorio.
2. Asegúrate de tener un entorno virtual activo con los siguientes paquetes instalados:

```bash
pandas
plotly-express
streamlit



3. Ejecuta la aplicación con:

```bash
streamlit run app.py


4. Abre el navegador en la URL que Streamlit indique (por ejemplo: `http://localhost:8501`).

## 📁 Dataset

El archivo `vehicles_us.csv` contiene información sobre vehículos usados publicados para la venta, incluyendo:

- Precio
- Año del modelo
- Kilometraje (`odometer`)
- Transmisión
- Tipo de combustible
- Condición del vehículo
- Marca y modelo

## 🌐 Enlace a la aplicación desplegada

[Haz clic aquí para ver la aplicación en Render](https://vehicles-dashboard-fn8o.onrender.com)
