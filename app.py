import pandas as pd
import streamlit as st 
import plotly.express as px 

data_vehicle = pd.read_csv('vehicles_us.csv')

st.header('my aplicacion web')

his_button = st.button('construir un histograma')



if his_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    table = data_vehicle.pivot_table(index='type',columns='condition', values='model_year')
    fig = px.histogram(table)
    st.plotly_chart(fig, use_container_width=True)

his_button2 = st.button('construir un grafica de dispercion')

if his_button2:
    st.write('grafica de dispercion creado')
    table = data_vehicle.pivot_table(index='model_year',columns='condition', values='price')
    fig2 = px.scatter(table)
    st.plotly_chart(fig2, use_container_width=True)
