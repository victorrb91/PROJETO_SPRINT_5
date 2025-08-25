import pandas as pd
import streamlit as st
import plotly_express as px

st.header('Dashboard de Anúncios de Venda de Carros')

car_data = pd.read_csv('vehicles.csv')