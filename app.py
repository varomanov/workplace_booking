from dash import Dash, callback, html, Output, Input, dcc
from db.operations import get_places_by_floor
from components import TabButton
import dash_bootstrap_components as dbc
import json

ds = get_places_by_floor(8)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

app.layout = [
    html.Div([
        html.Div([
            html.Header([
                    dbc.NavbarSimple(className='navbar navbar-dark bg-primary', children=[
                        dbc.NavItem(html.Span(['SURKOV Aleksandr', dbc.Button('Выйти', className='btn btn-outline-light ms-3')], className='navbar-text')),
                        dbc.NavItem(dbc.NavLink('Сообщить об ошибке', href='#'))
                    ],
                    brand='БРОНЬ',
                    brand_href='#',
                    color='primary',
                    dark=True,
                    expand=False)
                ], id='app-container', className='container p-0'),

            html.Div([
                    dbc.Container([
                        dbc.Button('Себе', className='col-5 btn-lg btn-block m-3'),
                        dbc.Button('Другому', className='col-5 btn-lg btn-block m-3', color='outline-primary'),
                    ], fluid=True),


                ], id='app-content'),

            html.Footer([html.Div([
                TabButton('Бронь', 'btn-book','fa-file-pen'),
                TabButton('Журнал', 'btn-journal','fa-table-list'),
                TabButton('Этажи', 'btn-book','fa-building'),
                TabButton('КИР', 'btn-book','fa-person-shelter'),
            ], className='fixed-bottom d-flex justify-content-between m-3')])

        ], id='wrapper', className='vh-100 bg-white overflow-hidden m-auto position-relative', style={'maxWidth': '430px', 'transform': 'translate(0)'}),

    ], id = 'background', className='bg-secondary'),
    ]

if __name__ == '__main__':
    app.run(debug=True)



