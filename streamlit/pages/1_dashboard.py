import pandas as pd
import plotly.express as px
import seaborn as sns

import streamlit as st


@st.cache_data
def load_data(url: str):
    df = pd.read_csv('/home/mangel/repositorios/repos/practica_ufv/streamlit/video_games_sales.csv', sep=',')
    return df



def info_box(texto, color=None):
    st.markdown(
        f'<div style="background-color:#4EBAE1;opacity:70%"><p style="text-align:center;color:white;font-size:30px;">{texto}</p></div>',
        unsafe_allow_html=True)


df_merged = load_data('http://fastapi:8000/retrieve_data')

registros = str(df_merged.shape[0])
adjudicatarios = str(len(df_merged.Publisher.unique()))
centro = str(len(df_merged.Developer.unique()))
tipologia = str(len(df_merged.Genre.unique()))
presupuesto_medio = str(round(df_merged.Global_Sales.mean(), 2))
adjudicado_medio = str(round(df_merged.Critic_Score.mean(), 2))

sns.set_palette("pastel")

st.header("Información general")

col1, col2, col3 = st.columns(3)

col4, col5, col6 = st.columns(3)
with col1:
    col1.subheader('# videojuegos')
    info_box(registros)
with col2:
    col2.subheader('# Publishers')
    info_box(adjudicatarios)
with col3:
    col3.subheader('# Developers')
    info_box(centro)

with col4:
    col4.subheader('# Géneros')
    info_box(tipologia)

with col5:
    col5.subheader('Ventas Medias Globales')
    info_box(presupuesto_medio, col5)

with col6:
    col6.subheader('Critic Score Medio')
    info_box(adjudicado_medio, col6)

tab1, tab2 = st.tabs(["Distribución de Ventas Globales", "Distribución de Critic Score"])

fig1 = px.box(df_merged, y='Global_Sales', points="all")
fig2 = px.box(df_merged, y='Critic_Score', points="all")

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme=None, use_container_width=True)
