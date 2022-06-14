from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel('worldometer_data.xlsx')
grafico = px.bar(df, x='Continent',
y='TotalCases',
color='Country/Region')

filtro_paises = list(df['Country/Region'].unique())
filtro_paises.insert(0, 'Todos os Países')

app.layout = html.Div(children=[
    html.H1(children='Casos de COVID-19 por País'),
    html.H2(children='Grafico com quantidade de casos de covid-19 em 08/2020'),
    html.Div(children=[
        dcc.Dropdown(filtro_paises, value='Todos os Países', id='listaPaises'),

    dcc.Graph(
        id='casos',
        figure=grafico
    )

    ])
])

@app.callback(
    Output('casos', 'figure'),
    Input('listaPaises', 'value')
)
def graph_pais(value):
    if value == 'Todos os Países':
        grafico = px.bar(
            df,
            x='Continent',
            y='TotalCases',
            color='Country/Region'
        )
    else:
        tab = df.loc[df['Country/Region'] == value,]
        grafico = px.bar(
            tab,
            x='Continent',
            y='TotalCases',
            color='Country/Region',
            barmode='group'
        )
    return grafico

if __name__ == '__main__':
    app.run_server(debug=True)