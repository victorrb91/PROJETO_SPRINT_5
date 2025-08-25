import pandas as pd
import streamlit as st
import plotly_express as px

st.header('Dashboard de Anúncios de Venda de Carros')

car_data = pd.read_csv('vehicles.csv')

hist_button = st.button('Criar histograma de odômetro')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de carros')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de carros')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)