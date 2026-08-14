import plotly.express as px
from utils import df_receita_estado, df_receita_mensal, df_receita_categoria, df_vendedores


grafico_map_estado = px.scatter_mapbox(
    df_receita_estado,
    lat='lat',
    lon='lon',
    size='Preço',
    color='Preço',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False},
    title='Receita por Estado',
    zoom=3,
    center={"lat": -14.2350, "lon": -51.9253},
    mapbox_style="open-street-map"
)

grafico_map_estado.update_layout(
    coloraxis_showscale=False,
    margin={"r": 0, "t": 40, "l": 0, "b": 0},
    height=500
)

grafico_receita_mensal = px.line(
    df_receita_mensal,
    x='Mes',
    y='Preço',
    markers=True,
    range_y=(0, df_receita_mensal.max()),
    color='Ano',
    line_dash='Ano',
    title='Receita Mensal'
)

grafico_receita_mensal.update_layout(yaxis_title='Receita')

grafico_receita_estado = px.bar(
    df_receita_estado.head(7),
    x='Local da compra',
    y='Preço',
    text_auto=True,
    title='Top receita por estado'
)

grafico_receita_categoria = px.bar(
    df_receita_categoria.head(7),
    text_auto=True,
    title='Top 7 Categorias com maior receita'
)


top_vendedores = df_vendedores.sort_values('sum', ascending=False).head(7)

grafico_receita_vendedores = px.bar(
    top_vendedores,
    x='sum',
    y=top_vendedores.index,
    text_auto=True,
    title='Top 7 vendedores por receita'
)
