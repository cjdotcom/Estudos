# Dashboard com plotly da aula de hashtag programação, com algumas modificações 

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel('Vendas.xlsx') #database

fig = px.box(df, x="Produto", y="Quantidade", color="ID Loja") #grafico

op = list(df['ID Loja'].unique()) #lista de lojas da dropdown
op.append('Todos')

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Grafico com o faturamento de todos os produtos separados por loja.'),
    html.Div(children='''
        Obs: Esse grafico mostra a quantidade de produtos vendidos e não o faturamento.
    '''),

    #aqui termina a parte de layout
    dcc.Dropdown(op, value='Todos', id='listaLojas'),
    dcc.Graph(
        id='vendas', 
        figure=fig
    ) # aqui termina a parte de callback
])

#Decorator que atribui a função 'update' a uma nova tarefa
@app.callback(
    Output('vendas', 'figure'), #Mostra a informação filtrada
    Input('listaLojas', 'value') #seleciona a informação a ser filtrada
) 
def update(value): #Função que modifica o grafico pelo filtro de lojas
    if value == 'Todos':
        fig = px.box(df, x="Produto", y="Quantidade", color="ID Loja") #caso seja tipo 'bar', usar o barmode='group'.
    else:
        tab = df.loc[df['ID Loja'] == value, :]
        fig = px.box(tab, x="Produto", y="Quantidade", color="ID Loja")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)