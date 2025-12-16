from dash import Dash, callback, html, Output, Input, dcc
from db.operations import get_places_by_floor
import json

ds = get_places_by_floor(8)

app = Dash(__name__)
app.layout = [
    html.H1('Hello World'),
    dcc.Input(id='my-input', value=0, type='number'),
    html.Div(id='container-ws', children=[]),

    html.Div([html.Div(i.to_str()) for i in ds])
    ]

@callback(
Output('container-ws', 'children'),
Input('my-input', 'value')
)
def testtt(floor: int): #пока данные есть только по floor = 8
    spaces = get_places_by_floor(floor)
    return [
        html.Div(f'Input {s.number}') 
        for s in spaces
    ]

if __name__ == '__main__':
    app.run(debug=True)



