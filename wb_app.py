from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR])
app.layout = dbc.Container([
    # заголовок
    html.H5('Бронирование', 
            className='text-center fw-bold w-100 m-0 p-0', 
            style={'backgroundColor': 'rgba(255, 255, 255, .5)', 'height': '30px'}),

    # кнопки для выбора кому бронировать
    dbc.Row([
        dbc.Col(dbc.Button('Для меня', className='w-100')),
        dbc.Col(dbc.Button('Для другого человека', className='w-100 border-1 border', outline=True)),
    ], class_name='p-4 '),

    # выбор даты
    # dcc.DatePickerSingle(id= placeholder='Выберите дату', className='w-100 ps-4', style={'width': '100%'})
    dbc.Row([
        dbc.Col(dbc.Select(options=['2025-10-09', "2025-10-15", "2025-10-12"], value=['2025-10-09'])),
        dbc.Col(dbc.Select(options=['Целый день', "Первая половина", "вторая половина"], value='Целый день'))
    ], class_name='p-4'),
    
], style={'backgroundColor': 'rgba(240, 240, 240, .5)', 'max-width': '500px'}, className='vh-100 ps-0 pe-0')

if __name__ == '__main__':
    app.run(debug=True)