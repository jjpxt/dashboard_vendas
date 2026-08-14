import plotly.express as px
from utils import df_receita_estado, df_receita_mensal

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
