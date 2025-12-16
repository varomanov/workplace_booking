from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

df = px.data.gapminder()

app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
app.layout = dbc.Container([
    html.H1('Мониторинг показателей проекта'),
    html.H3('Основные метрики за текущий квартал'),
    dbc.Row([
        dbc.Col(html.P('Общая выручка')),
        dbc.Col(html.H2('1 250 000 руб.')),
    ]),
    dbc.Row([
        dbc.Col(html.Div(dcc.Graph(figure=px.scatter(data_frame=df, x='continent', y='pop'))))
    ]),
])

if __name__ == '__main__':
    app.run(debug=True)