from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
from header import get_header
#from app import server

#EDF COLOURS
EDF_BLUE = '#103579'
EDF_ORANGE = '#ff5716'


#CREATE DASHBOARD LAYOUT
def get_dashboard_layout(app):
    layout = html.Div([

        get_header(app=app),

#TITLE *************************************************************************
        html.Div(
            [
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.H3('Radiation Dose Calculator',

                                style = {
                                    'textAlign' : 'center',
                                    'font_family':'sans-serif'
                                }
                                )
                    ], width=10),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ]),

                html.Br(),
                html.Br(),
                html.Br(),

                #QUESTIONS BEGIN *********************************************************************

                #(1) X-rays
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


                #(2) CT SCANS
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.B(['2. '], style={'display': 'inline-block'}),
                        html.H6(['How many CT scans have you had in the last year?'], style={'display': 'inline-block'})
                    ], width=6),
                    dbc.Col([
                    ], width=1),
                    dbc.Col([
                        html.Img(id="ct-logo",
                                 src=app.get_asset_url('xray.svg'),
                                 height=80,
                                 width=80,
                                 style={'align-items': 'center'})
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-2-Q'),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.Div([
                            html.I('Head CT Scan'),
                            dcc.Dropdown(id='Q-2a-ddown',
                                         options=[
                                             {"label": value, "value": value} for value in range(100)
                                         ])
                        ])
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.I('Chest CT Scan'),
                            dcc.Dropdown(id='Q-2b-ddown',
                                         options=[
                                             {"label": value, "value": value} for value in range(100)
                                         ])
                        ])
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.I('Abdomen CT Scan'),
                            dcc.Dropdown(id='Q-2c-ddown',
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
                ], id='row-2-A'),

                #(3) COFFEE
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.B(['3. '], style={'display': 'inline-block'}),
                        html.H6(['How many coffees do you drink a week?'], style={'display': 'inline-block'})
                    ], width=6),

                    dbc.Col([
                    ], width=1),
                    dbc.Col([
                        html.Img(id="coffee-logo",
                                 src=app.get_asset_url('xray.svg'),
                                 height=80,
                                 width=80,
                                 style={'align-items': 'center'})
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-3-Q'),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(id='Q-3a-ddown',
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
                ], id='row-3-A'),

                #(4) BANANAS
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.B(['4. '], style={'display': 'inline-block'}),
                        html.H6(['How many bananas do you eat a week?'], style={'display': 'inline-block'})
                    ], width=6),

                    dbc.Col([
                    ], width=1),
                    dbc.Col([
                        html.Img(id="banana-logo",
                                 src=app.get_asset_url('xray.svg'),
                                 height=80,
                                 width=80,
                                 style={'align-items': 'center'})
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-4-Q'),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(id='Q-4a-ddown',
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
                ], id='row-4-A'),

                #(5) BEER
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.B(['5. '], style={'display': 'inline-block'}),
                        html.H6(['How many beers do you drink a week?'], style={'display': 'inline-block'})
                    ], width=6),

                    dbc.Col([
                    ], width=1),
                    dbc.Col([
                        html.Img(id="beer-logo",
                                 src=app.get_asset_url('xray.svg'),
                                 height=80,
                                 width=80,
                                 style={'align-items': 'center'})
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-5-Q'),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(id='Q-5a-ddown',
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
                ], id='row-5-A'),

                #(6) LIVING LOCATION (Not sure about the inputs and image, you're gonna have to do that)
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.B(['6. '], style={'display': 'inline-block'}),
                        html.H6(['Where do you live?'], style={'display': 'inline-block'})
                    ], width=6),

                    dbc.Col([
                    ], width=1),
                    dbc.Col([
                        html.Img(id="map-logo",
                                 src=app.get_asset_url('xray.svg'),
                                 height=80,
                                 width=80,
                                 style={'align-items': 'center'})
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-6-Q'),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(id='Q-6a-ddown',
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
                ], id='row-6-A'),

                #(7) HOLIDAY

                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.B(['7. '], style={'display': 'inline-block'}),
                        html.H6(['Have you been on holiday this year?'], style={'display': 'inline-block'})
                    ], width=7),
                    dbc.Col([
                        html.I('Picture')
                    ], width=3),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-99-Q'),

                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.H6(['Pick your holiday'], style={'display': 'inline-block'})
                    ], width=7),

                    dbc.Col([
                        html.I('Picture')
                    ], width=3),

                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-100-Q'),

                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),

                    dbc.Col([
                        dcc.Checklist(
                            ['Cornwall', 'Long Haul', 'Short Haul'],
                            inline=True
                        )
                    ], width=7),

                    dbc.Col([
                        html.I('Picture')
                    ], width=3),

                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-101-Q'),


                #Other
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
                ], id='row-99-A'),
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
