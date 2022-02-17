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

        # TITLE *************************************************************************
        html.Div(
            [
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.H3('Radiation Dose Calculator',

                                style={
                                    'textAlign': 'center',
                                    'font_family': 'sans-serif'
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

                # QUESTIONS BEGIN *********************************************************************

                # (1) X-rays
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

                # (2) CT SCANS
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

                # (3) COFFEE
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

                # (4) BANANAS
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

                # (5) BEER
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

                # (6) LIVING LOCATION (Not sure about the inputs and image, you're gonna have to do that)
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

                # (7) HOLIDAY

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
                            options=[
                                {'label': 'Cornwall', 'value': 'c'},
                                {'label': 'Long Haul', 'value': 'lh'},
                                {'label': 'Short Haul', 'value': 'sh'},
                            ],labelStyle={'display': 'block'}
                        )
                    ], width=7),

                    dbc.Col([
                        html.I('Picture')
                    ], width=3),

                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-101-Q'),

                # Other
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
                        html.Br(),
                        html.Br(),
                        html.Div(id='radio-items'),
                        html.Div('radio-content'),
                        html.Br(),
                        html.Br(),
                        html.Div(id='radio-content')
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

    @app.callback(
        Output(component_id='radio-items', component_property='children'),
        [Input(component_id='submit-val', component_property='n_clicks')]
    )
    def render_items(n_clicks):
        while n_clicks != 0:
            return html.Div([
                html.H4('Select an option'),
                dcc.RadioItems(id='radio-items',
                    options=[
                        {'label': 'Pints of Beer', 'value': 'beer'},
                        {'label': 'Bananas', 'value': 'banana'},
                        {'label': 'Years working in a power plant', 'value': 'power-plant'},
                        {'label': 'Cups of Coffee', 'value': 'coffee'},
                    ], labelStyle={'display': 'block'})
            ])

    @app.callback(
        Output(component_id='radio-content', component_property='children'),
        [Input(component_id='radio-items', component_property='value')]
    )
    def render_output(value):
        if value == 'beer':
            return html.H3('This is the equivilent of '),\
                   html.H2('XXX'),\
                   html.H3('pints of beer!')
        elif value == 'banana':
            return html.H3('This is the equivilent of '), \
                   html.H2('XXX'), \
                   html.H3('bananas!')
        elif value == 'power-plant':
            return html.H3('This is the equivilent of '),\
                   html.H2('XXX'),\
                   html.H3('years working in a power plant!')
        elif value == 'coffee':
            return html.H3('This is the equivilent of '), \
                   html.H2('XXX'), \
                   html.H3('coffees!')

    return layout
