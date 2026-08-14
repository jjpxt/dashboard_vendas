import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import grafico_map_estado, grafico_receita_mensal, grafico_receita_estado, grafico_receita_categoria, grafico_receita_vendedores, grafico_vendas_vendedores


st.set_page_config(layout="wide")

st.title('Dashboard de Vendas :shopping_cart:')

st.sidebar.title('Filtro de vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique(),
)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]


aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])

with aba1:
    st.dataframe(df)

with aba2:
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
    with col2:
        st.metric('Quantidade de vendas', df.shape[0])

    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(grafico_map_estado, use_container_width=True)
    with col4:
        st.plotly_chart(grafico_receita_mensal, use_container_width=True)

    col5, col6 = st.columns(2)
    with col5:
        st.plotly_chart(grafico_receita_estado, use_container_width=True)
    with col6:
        st.plotly_chart(grafico_receita_categoria, use_container_width=True)

with aba3:
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(grafico_receita_vendedores)
    with col2:
        st.plotly_chart(grafico_vendas_vendedores)
