import pandas as pd
import streamlit as st 
import plotly.express as px 

data_vehicle = pd.read_csv('vehicles_us.csv')

st.header('analisis de precio de modelos de autos')

his_button = st.button('construir un histograma')



if his_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(data_vehicle, x='price', color='model')
    fig.show()
    st.plotly_chart(fig, use_container_width=True)

his_button2 = st.button('construir un grafica de dispercion')

if his_button2:
    st.write('creacion de grafica de dispercion para entre odommetros y años de los modelos')
    fig2 = px.scatter(data_vehicle, x='odometer', y='model_year', color='model')
    fig2.show()

    st.plotly_chart(fig2, use_container_width=True)