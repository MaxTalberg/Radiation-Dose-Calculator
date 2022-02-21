from dash import dcc, html, State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import time

from header import get_header
# from app import server

#Hex
EDF_BLUE = '#103579'
EDF_ORANGE = '#ff5716'
Miles_Blue = '#64c3db'
Miles_Orange = '#e3652e'

#Database
database = pd.read_csv('assets/database.csv')

def get_dashboard_layout(app):


#Layout begins
    layout = html.Div([

        get_header(app=app),


        # TITLE *************************************************************************
        html.Div(
        dbc.Container(
            [
                html.H1("Radiation Dose Calculator ", className="display-3"),
                html.P(
                    "Discover your radiation exposure by answering the questions and clicking calculate",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "Radiation is part of our everyday life. Did you know there is naturally occuring radiation in the food you eat,.."
                ),
                html.P(
                    "Want to learn more? Check out our fact sheet below"
                ),

                html.P(
                    dbc.Button("Link to inforgraphics", color="primary"), className="lead"
                ),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-light rounded-3",
    ),

#***NEED TO DELETE IDK HOW THO
        html.Div(
            [
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.H2('',

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
                        html.Div([
                            dbc.Badge("How many x-rays have you had in the last year?",
                                      pill=True,
                                      color="#e3652e",
                                      className="me-1"),
                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-1'
                            ),
                            dbc.Tooltip("Hello"
                                        "Mate",
                                        target='question-1',
                                        placement='right'
                                        )
                        ])
                    ], width=6),

                    dbc.Col([
                    ], width=1),
                    dbc.Col([
                        html.Img(id="xray-logo",
                                 src='/assets/xray.png',
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
                            html.I('Dental X Ray'),
                            dcc.Dropdown(id='Q-1a-ddown',
                                         options=[
                                             {"label": value, "value": value} for value in range(6)])
                        ], style={"width": "50%"})
                    ], width=3),

                    dbc.Col([
                        html.Div([
                            html.I('Wrist X Ray'),
                            dcc.Dropdown(id='Q-1b-ddown',
                                         options=[
                                             {"label": value, "value": value} for value in range(5)])
                        ], style={"width": "50%"})
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
                        html.Div([
                            html.H5(['2. '], style={'display': 'inline-block'}),
                            html.H5(['How many CT scans have you had in the last year?'],
                                    style={'display': 'inline-block'}),

                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-2'
                            ),
                            dbc.Tooltip("Hello"
                                        "Mate",
                                        target='question-2',
                                        placement='right'
                                        )
                        ])
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
                                             {"label": value, "value": value} for value in range(5)])
                        ], style={"width": "50%"})
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.I('Chest CT Scan'),
                            dcc.Dropdown(id='Q-2b-ddown',
                                         options=[
                                             {"label": value, "value": value} for value in range(5)])
                        ], style={"width": "50%"})
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.I('Abdomen CT Scan'),
                            dcc.Dropdown(id='Q-2c-ddown',
                                         options=[
                                                 {"label": value, "value": value} for value in range(5)])
                            ], style={"width": "50%"}),
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
                        html.Div([
                            html.H5(['3. '], style={'display': 'inline-block'}),
                            html.H5(['How many coffees do you drink a week?'], style={'display': 'inline-block'}),

                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-3'
                            ),
                            dbc.Tooltip("Hello"
                                        "Mate",
                                        target='question-3',
                                        placement='right'
                                        )
                        ])
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
                                             {"label": value, "value": value} for value in range(5)])
                        ], style={"width": "50%"}),
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
                        html.Div([
                            html.H5(['4. '], style={'display': 'inline-block'}),
                            html.H5(['How many bananas do you eat a week?'], style={'display': 'inline-block'}),

                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-4'
                            ),
                            dbc.Tooltip("Hello"
                                        "Mate",
                                        target='question-4',
                                        placement='right'
                                        )
                        ])
                    ], width=6),

                    dbc.Col([
                    ], width=1),
                    dbc.Col([
                        html.Img(id="banana-logo",
                                 src='/assets/banana.png',
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
                                             {"label": value, "value": value} for value in range(5)])
                        ], style={"width": "50%"}),
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
                        html.Div([
                            html.H5(['5. '], style={'display': 'inline-block'}),
                            html.H5(['How many beers do you drink a week?'], style={'display': 'inline-block'}),

                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-5'
                            ),
                            dbc.Tooltip("Hello"
                                        "Mate",
                                        target='question-5',
                                        placement='right'
                                        )
                        ])
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
                                             {"label": value, "value": value} for value in range(5)])
                        ], style={"width": "50%"}),
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
                        html.Div([
                            html.H5(['6. '], style={'display': 'inline-block'}),
                            html.H5(['Where do you live?'], style={'display': 'inline-block'}),

                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-6'
                            ),
                            dbc.Tooltip("Hello"
                                        "Mate",
                                        target='question-6',
                                        placement='right'
                                        )
                        ])
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
                                             {"label": 'London', "value": 'london'},
                                             {"label": 'Rest of UK', "value": 'rest'}])
                        ], style={"width": "50%"}),
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
                        html.Div([
                            html.H5(['7. '], style={'display': 'inline-block'}),
                            html.H5(['Have you been on holiday this year?'], style={'display': 'inline-block'}),

                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-7'
                            ),
                            dbc.Tooltip("Hello"
                                        "Mate",
                                        target='question-7',
                                        placement='right'
                                        )
                        ])
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
                        html.H6(['How many flights have you taken?'], style={'display': 'inline-block'})
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
                        html.Div([
                            html.I('Long Haul'),
                            html.Div([
                                dcc.Dropdown(id='Q-7a-ddown',
                                             options=[
                                                 {"label": value, "value": value} for value in range(5)])
                            ], style={"width": "50%"}),
                        ])
                    ], width=3),

                    dbc.Col([
                        html.Div([
                            html.I('Short Haul'),
                            html.Div([
                                dcc.Dropdown(id='Q-7b-ddown',
                                             options=[
                                                 {"label": value, "value": value} for value in range(5)])
                            ], style={"width": "50%"}),
                        ])
                    ], width=3),
                    dbc.Col([
                    ], width=4),
                    dbc.Col([
                        html.I('margin')
                    ], width=1)
                ], id='row-7-A'),

                html.Br(),


                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),

                    dbc.Col([
                        dbc.Checklist(
                            options=[
                                {'label': '3-Day Holiday to Cornwall', 'value': 'c'},
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
                    ], width=7),
                    dbc.Col([
                        html.I('Picture')
                    ], width=3),
                    dbc.Col([
                    ], width=1)
                ], id='row-99-A'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        dbc.Button('Calculate', id='submit-val', n_clicks=0, style={'textTransform': 'none'}),
                        dcc.Loading(
                            id="loading-1",
                            type="default",
                            children=html.Div(id="loading-output-1")
                        ),
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
        Output(component_id='data', component_property='children'),
        [Input(component_id='Q-1a-ddown', component_property='value'),
         Input(component_id='Q-1b-ddown', component_property='value')]
    )
    def organise_data(dental, wrist):
        q1 = (dental*database['Dental'][0]) + (wrist*database['Wrist'][0])
        return q1
    @app.callback(
        Output(component_id='loading-output-1', component_property='children'),
        [Input(component_id='submit-val', component_property='n_clicks')]
    )
    def load_sign(n_clicks):
        time.sleep(1)
        return
    @app.callback(
        Output(component_id='tabs-graph', component_property='children'),
        [Input(component_id='submit-val', component_property='n_clicks')]
    )
    def update_output(n_clicks):
        time.sleep(1.5)
        while n_clicks != 0:
            return html.Div([
                dcc.Tabs(id='tab-graph', value='tab-graph-value', children=[
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
        time.sleep(1.5)
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
            return html.H3('Your annual does of'),\
                   html.H3('radiation is equivalent to '),\
                   html.H2('XXX'),\
                   html.H3('pints of beer!')
        elif value == 'banana':
            return html.H3('Your annual does of'),\
                   html.H3('radiation is equivalent to '),\
                   html.H2('XXX'), \
                   html.H3('bananas!')
        elif value == 'power-plant':
            return html.H3('Your annual does of'),\
                   html.H3('radiation is equivalent to '),\
                   html.H2(id='data'),\
                   html.H3('years working in a nuclear power plant!')
        elif value == 'coffee':
            return html.H3('Your annual does of'),\
                   html.H3('radiation is equivalent to '),\
                   html.H2(id='data'), \
                   html.H3('coffees!')

    return layout
