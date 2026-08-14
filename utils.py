import pandas as pd
from dataset import df


def format_number(value, prefix=''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'


df_receita_estado = df.groupby('Local da compra')[['Preço']].sum()
df_receita_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(
    df_receita_estado, left_on='Local da compra', right_index=True
).sort_values('Preço', ascending=False)


df_receita_mensal = df.set_index('Data da Compra').groupby(
    pd.Grouper(freq='ME'))['Preço'].sum().reset_index()
df_receita_mensal['Ano'] = df_receita_mensal['Data da Compra'].dt.year
df_receita_mensal['Mes'] = df_receita_mensal['Data da Compra'].dt.month_name()


df_receita_categoria = df.groupby('Categoria do Produto')[
    ['Preço']].sum().sort_values('Preço', ascending=False)


df_vendedores = pd.DataFrame(df.groupby(
    'Vendedor')['Preço'].agg(['sum', 'count']))
