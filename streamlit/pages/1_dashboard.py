import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def load_data(url: str):
    df = pd.read_csv('/home/mangel/repositorios/repos/practica_ufv/streamlit/pages/video_games_sales.csv', sep=',')
    return df

#prueba de que se carga bien el DF
df_merged = load_data('http://fastapi:8000/retrieve_data')
print(df_merged)

# Verificación de carga de datos
st.write("DataFrame Cargado:")
st.write(df_merged)

# Información general
st.header("Información general")

# Números generales
registros = str(df_merged.shape[0])
adjudicatarios = str(df_merged['Publisher'].nunique())
centro = str(df_merged['Developer'].nunique())
tipologia = str(df_merged['Genre'].nunique())
presupuesto_medio = str(round(df_merged['Global_Sales'].mean(), 2))
adjudicado_medio = str(round(df_merged['Critic_Score'].mean(), 2))

# Mostrar información en columnas
col1, col2, col3 = st.columns(3)
col1.subheader('# videojuegos')
col1.info(registros)

col2.subheader('# Publishers')
col2.info(adjudicatarios)

col3.subheader('# Developers')
col3.info(centro)

col4, col5, col6 = st.columns(3)
col4.subheader('# Géneros')
col4.info(tipologia)

col5.subheader('Ventas Medias Globales')
col5.info(presupuesto_medio)

col6.subheader('Critic Score Medio')
col6.info(adjudicado_medio)

# Tabs para gráficos
tab1, tab2 = st.columns(2)

# Distribución de Ventas Globales
with tab1:
    st.subheader("Distribución de Ventas Globales")
    fig1 = px.box(df_merged, y='Global_Sales', points="all")
    st.plotly_chart(fig1, use_container_width=True)

# Distribución de Critic Score
with tab2:
    st.subheader("Distribución de Critic Score")
    fig2 = px.box(df_merged, y='Critic_Score', points="all")
    st.plotly_chart(fig2, use_container_width=True)


# Gráfico interactivo:
with tab3:
    st.subheader("Ventas Globales y Critic Score por Género")
    fig3 = px.scatter(df_merged, x='Critic_Score', y='Global_Sales', color='Genre', marginal_y="violin", marginal_x="box", title='Ventas Globales vs Critic Score por Género')
    st.plotly_chart(fig3, use_container_width=True)

# Gráfico interactivo:
with tab4:
    st.subheader("User score y ventas globales
    # Puedes modificar y personalizar este gráfico según tus necesidades
    fig4 = px.scatter(df_merged, x='User_Score', y='Global_Sales', color='Platform', title='Ventas Globales vs User Score por Plataforma')
    st.plotly_chart(fig4, use_container_width=True)
