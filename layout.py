from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from header import get_header
# from app import server

EDF_BLUE = '#103579'
EDF_ORANGE = '#ff5716'

def get_dashboard_layout(app):
    layout = html.Div([

        get_header(app=app),

        html.Div(
            [
                html.H3('Web App Communicating Radiation Risk'),
                html.Br(),
                html.I('Food and Drink'),
                html.Br(),
                html.I('Question 1?'),
                html.Br(),
                dcc.Input(id='input1', type='text', placeholder=''),
                html.Br(),
                html.I('Question 2?'),
                html.Br(),
                dcc.Input(id='input2', type='text', placeholder=''),
                html.Br(),
                html.I('Question 3?'),
                html.Br(),
                dcc.Input(id='input3', type='text', placeholder=''),
                html.Br(),
                html.Div(id='output')
        ])

    ])

    @app.callback(
        Output('output', 'children'),
        Input('input1', 'value'),
        Input('input2', 'value'),
        Input('input3', 'value'),
    )
    def update_outpute(input1, input2, input3):
        return u' Radiation dose {}, your fucked!'.format(input1)

    return layout
