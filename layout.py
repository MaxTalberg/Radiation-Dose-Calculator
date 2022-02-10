from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd

from header import get_header
# from app import server

EDF_BLUE = '#103579'
EDF_ORANGE = '#ff5716'

def get_dashboard_layout(app):
    layout = html.Div([

        get_header(app=app),

        html.Div(
            [
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.H3('Web App Communicating Radiation Risk')
                    ], width=10),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.B(['1. '], style={'display': 'inline-block'}),
                        html.H6(['How many Xrays have you had in the last year?'], style={'display': 'inline-block'})
                    ], width=6),
                    dbc.Col([
                    ], width=1),
                    dbc.Col([
                        html.Img(id="xray-logo",
                                 src=app.get_asset_url('xray.svg'),
                                 height=80,
                                 width=80,
                                 style={'align-items': 'center'})
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-1-Q'),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.Div([
                            html.I('Dental Xrays'),
                            dcc.Dropdown(id='Q-1a-ddown',
                                         options=[
                                             {"label": value, "value": value} for value in range(100)
                                         ])
                        ])
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.I('Wrist Xrays'),
                            dcc.Dropdown(id='Q-1b-ddown',
                                         options=[
                                             {"label": value, "value": value} for value in range(100)
                                         ])
                        ])
                    ], width=3),
                    dbc.Col([
                    ], width=4),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-1-A'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.I('Question')
                    ], width=7),
                    dbc.Col([
                        html.I('Picture')
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-2-Q'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.I('Answer')
                    ], width=7),
                    dbc.Col([
                        html.I('Picture')
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-2-A'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.I('Question')
                    ], width=7),
                    dbc.Col([
                        html.I('Picture')
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-3-Q'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.I('Answer')
                    ], width=7),
                    dbc.Col([
                        html.I('Picture')
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-3-A'),
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
