import streamlit as st
import plotly.express as px
import matplotlib
from matplotlib.backends.backend_agg import RendererAgg
import requests
import seaborn as sns
import pandas as pd

st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache_data
def load_data(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    mijson = r.json()
    listado = mijson['JuegosVideo']
    df = pd.DataFrame.from_records(listado)
    return df

df_sales = load_data('http://fastapi:8000/retrieve_data')

if df_sales is not None and not df_sales.empty:
    df_sales['Global_Sales'] = df_sales['Global_Sales'].astype(float)

    registros = str(df_sales.shape[0])
    juegos_unicos = str(len(df_sales.Name.unique()))
    plataformas_unicas = str(len(df_sales.Platform.unique()))
    años_unicos = str(len(df_sales.Year.unique()))
    generos_unicos = str(len(df_sales.Genre.unique()))
    publicadores_unicos = str(len(df_sales.Publisher.unique()))
    ventas_globales_medias = str(round(df_sales.Global_Sales.mean(), 2))

    # Configuración de estilo

    def info_box(texto, color=None):
        st.markdown(
            f'<div style = "background-color:#4EBAE1;opacity:70%"><p style="text-align:center;color:white;font-size:30px;">{texto}</p></div>',
            unsafe_allow_html=True)
    lock = RendererAgg.lock
    matplotlib.use("agg")
    sns.set_palette("pastel")

    # Crear la aplicación Streamlit
    st.header("Información de Ventas de Videojuegos")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader('# Registros')
        info_box(registros)
    with col2:
        st.subheader('# Juegos Únicos')
        info_box(juegos_unicos)
    with col3:
        st.subheader('# Plataformas Únicas')
        info_box(plataformas_unicas)

    # Otras columnas y cálculos ...

    # Adicionalmente, puedes mostrar alguna visualización, por ejemplo, la distribución de las ventas globales
    st.header("Distribución de Ventas Globales")
    sns.histplot(df_sales.Global_Sales, kde=True)
    st.pyplot()

    # Gráficos sobre ventas de videojuegos
    tab1, tab2 = st.columns(2)

    # Gráfico de histograma y KDE de ventas globales
    fig1 = px.histogram(df_sales, x='Global_Sales', nbins=30, labels={'Global_Sales': 'Ventas Globales'})
    fig1.update_layout(showlegend=False)

    # Gráfico de barras de ventas por plataforma
    fig2 = px.bar(df_sales.groupby('Platform').Global_Sales.sum().reset_index(), x='Platform', y='Global_Sales',
                  labels={'Platform': 'Plataforma', 'Global_Sales': 'Ventas Globales'},
                  title='Ventas Globales por Plataforma')

    with tab1:
        st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

    with tab2:
        st.plotly_chart(fig2, theme=None, use_container_width=True)

else:
    st.error("No se pudieron cargar los datos. Verifica la URL y la conexión.")
