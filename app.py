import pandas as pd
import streamlit as st 
import plotly.express as px 

data_vehicle = pd.read_csv('vehicles_us.csv')

st.header('my aplicacion web')

his_button = st.button('construir un histograma')

his_button2 = st.button('construir un grafica de dispercion')

if his_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

if his_button2:
    st.write('creando grafica de dispercion')

fig = px.histogram(data_vehicle, x='odometer')

st.plotly_chart(fig, use_container_width=True)