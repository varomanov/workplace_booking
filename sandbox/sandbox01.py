from dash import Dash, html, callback, Output, Input, State
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H3('Добавление нового пользователя', className='display-5 border-3 border-bottom pb-3 text-center'),
    dbc.Row([
        dbc.Col([
            html.P('Введите ваше имя:'),
            dbc.Input(id='name-input', placeholder='Иванов И.И.'),
            html.Hr(),
            html.P('Введите ваш email:'),
            dbc.Input(id='email-input', placeholder='some@mail.ru'),
            html.Br(),
            dbc.Button('Сохранить', id='submit-button', className='btn btn-primary'),
            html.Br(),
            html.Div(id='output-div')
        ]),
    ], className='w-50 m-auto'),
])

@callback(
    Output('output-div', 'children'),
    Input('submit-button', 'n_clicks'),
    State('name-input', 'value'),
    State('email-input', 'value'),
    prevent_initial_call = True
)
def update_info(n_clicks, name, email):
    if n_clicks:
        name = name if name else 'Вы не указали ваше имя!'
        email = email if email else 'Вы не указали ваш email!'
    return dbc.Alert(f'Данные получены от {name}, ваш email {email}')

if __name__ == '__main__':
    app.run(debug=True, port=8808)