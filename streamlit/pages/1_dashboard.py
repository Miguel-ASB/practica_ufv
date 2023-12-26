import pandas as pd
import streamlit as st
import plotly.express as px
import requests

@st.cache_data
def load_data(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    mijson = r.json()
    listado = mijson['video_games']
    df = pd.DataFrame.from_records(listado)
    return df

df = load_data('http://fastapi:8000/retrieve_data')

def info_box(texto):
    st.markdown(f'<p style="background-color:#4EBAE1; color:black; padding:10px; border-radius:5px; text-align:center; font-size:30px; margin:0;">{texto}</p>', unsafe_allow_html=True)

# Verifica si df es None antes de intentar acceder a sus atributos
if df is not None:
    registros = str(df.shape[0])
    adjudicatarios = str(df['Publisher'].nunique())
    centro = str(df['Developer'].nunique())
    tipologia = str(df['Genre'].nunique())
    presupuesto_medio = str(round(df['Global_Sales'].mean(), 2))
    adjudicado_medio = str(round(df['Critic_Score'].mean(), 2))
else:
    st.warning("No se pudo cargar el DataFrame. Verifica los errores anteriores.")

# Mostrar información en columnas
col1, col2, col3 = st.columns(3)
col1.subheader('# videojuegos')
col1.info(registros)

col2.subheader('# Publishers')
col2.info(adjudicatarios)

col3.subheader('# Plataformas')
col3.info(df['Platform'].nunique())

col4, col5, col6 = st.columns(3)
col4.subheader('# Géneros')
col4.info(tipologia)

col5.subheader('Ventas Medias Globales')
col5.info(presupuesto_medio)

# Tabs para gráficos
tab1, tab2, tab3, tab4 = st.columns(4)

# Distribución de Ventas en America
with tab1:
    st.subheader("Distribución de Ventas en America")
    fig1 = px.box(df, y='NA_Sales', points="all")
    st.plotly_chart(fig1, use_container_width=True)

# Distribución de Ventas en Europa
with tab2:
    st.subheader("Distribución de Ventas en Europa")
    fig1 = px.box(df, y='EU_Sales', points="all")
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico interactivo: Ventas Globales vs Critic Score por Género
# Rellenar NaN con valores predeterminados
df_filled = df.fillna(0)

# Gráfico interactivo: Ventas America vs Europa
with tab3:
    st.subheader("Ventas America vs Europa")
    if 'NA_Sales' in df_filled.columns and 'EU_Sales' in df_filled.columns and 'Genre' in df_filled.columns:
        fig3 = px.scatter(df_filled, x='NA_Sales', y='EU_Sales', color='Genre', marginal_y="violin", marginal_x="box", title='Ventas Globales vs Critic Score por Género')
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.error("Alguna de las columnas necesarias no está presente en el DataFrame modificado.")

# Gráfico interactivo: User Score vs Ventas America por Plataforma
# Rellenar NaN con valores predeterminados
df_filled_platform = df.fillna({'Platform': 'Desconocido'})

# Gráfico interactivo: User Score vs Ventas America por Plataforma
with tab4:
    st.subheader("User Score vs Ventas de Europa por Plataforma")
    if 'Platform' in df_filled_platform.columns and 'EU_Sales' in df_filled_platform.columns:
        fig4 = px.scatter(df_filled_platform, x='Platform', y='EU_Sales', color='Platform', title='User Score vs Ventas Globales por Plataforma')
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.error("Alguna de las columnas necesarias no está presente en el DataFrame modificado.")
