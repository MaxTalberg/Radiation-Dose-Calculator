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
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.Button('Submit', id='submit-val', n_clicks=0)
                    ], width=7),
                    dbc.Col([
                        html.I('Picture')
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-4-Button'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.Div(id='tabs-graph'),
                        html.Div(id='tabs-content')
                    ], width=7),
                    dbc.Col([
                        html.I('hallloooo0oo'),
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-5-Output'),
        ])

    ])

    @app.callback(
        Output(component_id='tabs-graph', component_property='children'),
        [Input(component_id='submit-val', component_property='n_clicks')]
    )
    def update_output(n_clicks):
        while n_clicks != 0:
            return html.H6('Output Demo'),\
                   html.Div([dcc.Tabs(id='tab-graph', value='tab-graph-value', children=[
                       dcc.Tab(label='Tab One', value='tab-1'),
                       dcc.Tab(label='Tab Two', value='tab-2')
                   ]),
                             ])

    @app.callback(
        Output(component_id='tabs-content', component_property='children'),
        [Input(component_id='tab-graph', component_property='value')]
    )
    def render_content(tab):
        if tab == 'tab-1':
            return html.Div([
                html.H3('Tab content 1'),
                dcc.Graph(
                    id='graph-1-tabs',
                    figure={
                        'data': [{
                            'x': [1, 2, 3],
                            'y': [3, 1, 2],
                            'type': 'bar'
                        }]
                    }
                )
            ])
        elif tab == 'tab-2':
            return html.Div([
                html.H3('Tab content 2'),
                dcc.Graph(
                    id='graph-2-tabs',
                    figure={
                        'data': [{
                            'x': [1, 2, 3],
                            'y': [5, 10, 6],
                            'type': 'bar'
                        }]
                    }
                )
            ])

    return layout
