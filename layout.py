#Import Libraries
from dash import dcc, html, State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import time
from header import get_header
from title import get_title

from questions.xray import get_question1


#Hex Colours
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
        get_title(app=app),

#***NEED TO DELETE IDK HOW THO
        get_question1(app=app),

        html.Br(),


                dbc.Row([

                ], id='row-1-A'),

                # (2) CT SCANS
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),
                    dbc.Col([
                        html.Div([
                            html.H4(["",dbc.Badge("How many CT scans have you had in the last year?",
                                      pill=True,
                                      color="#e3652e",
                                      className="me-1")
                                     ]),

                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-2'
                            ),
                            dbc.Tooltip(html.Div(
                                "CT Scans form images of your body using many x-rays. X-rays subject your body to a dose of radiation"
                                "Effective Dose: 2mSv (Head CT Scan), 8mSv (Chest CT Scan) and  10mSv (Abdomen CT Scan)"
                                "This is the same dose as eating 200, 800 and 1000 bananas"

                            ),

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
                                html.H4(["",dbc.Badge("How many coffees do you drink a week?",
                                      pill=True,
                                      color="#e3652e",
                                      className="me-1")
                                     ]),

                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-3'
                            ),
                            dbc.Tooltip("Coffee contains naturally occurring radioactive nuclides from"
                                        "the soil coffee plants are grown in."
                                        "When you drink a coffee you ingest a tiny amount of radiation."
                                        "Effective Dose: 0.0006 mSv (approx. one coffee)."
                                        "This is the same eating 1/17 bananas",
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
                            dbc.Tooltip("Bananas are famous for containing radioactive nuclide potassium-40."
                                        "When you eat a banana you ingest a small dose of this nuclide."
                                        "Effective Dose: 0.01 mSv (per banana)",
                                        target='question-4',
                                        placement='right'
                                        ),
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

                        html.H4(["", dbc.Badge("How many beers do you drink a week?",
                                                   pill=True,
                                                   color="#e3652e",
                                                   className="me-1"),
                                    ]),

                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-5'
                            ),
                            dbc.Tooltip("Beer contains a very small amount of radioactive nuclides sourced from the water"
                                        "used to create beer."
                                        "Effective Dose: 0.0004 mSv (per pint)"
                                        "This is the same as eating 1/25 of a banana",
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
                            html.H4(["", dbc.Badge("Where do you live?",
                                                   pill=True,
                                                   color="#e3652e",
                                                   className="me-1"),
                                     ]),
                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-6'
                            ),
                            dbc.Tooltip("COMPLETE LATER"
                                        ,
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
                                             {"label": 'Sheffield', "value": 'london'},
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
                            html.H4(["", dbc.Badge("Have you been on holiday this year?",
                                                   pill=True,
                                                   color="#e3652e",
                                                   className="me-1"),
                                    ]),
                            html.Div([
                                html.I(className="fa fa-info-circle")
                            ], style={'display': 'inline-block',
                                      'margin-left': '10px'},
                                id='question-7'
                            ),
                            dbc.Tooltip("Hello loads of phyiscs stuff that is importnt"
                                        "Mate more physics stuff that is important"
                                        "j,nm,,,m",
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

                #Holiday to Cornwall
                dbc.Row([
                    dbc.Col([
                        html.I('margin')
                    ], width=1),

                    dbc.Col([
                        html.Div([
                            html.I('How many days have you spent on a holiday to Cornwall?'),
                            html.Div([
                                dcc.Dropdown(id='Q-7c-ddown',
                                             options=[
                                                 {"label": value, "value": value} for value in range(10)])
                            ], style={"width": "50%"}),
                        ]),
                        ]),
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
    @app.callback(
        Output(component_id='data', component_property='children'),
        [Input(component_id='Q-1a-ddown', component_property='value'),
         Input(component_id='Q-1b-ddown', component_property='value'),
         Input(component_id='Q-2a-ddown', component_property='value'),
         Input(component_id='Q-2b-ddown', component_property='value'),
         Input(component_id='Q-2c-ddown', component_property='value'),
         Input(component_id='Q-3a-ddown', component_property='value'),
         Input(component_id='Q-4a-ddown', component_property='value'),
         Input(component_id='Q-5a-ddown', component_property='value'),
         Input(component_id='Q-6a-ddown', component_property='value')
         ]
    )
    def organise_data(dental, wrist, head, chest, abdomen, coffee, bananas, beer, location):
        weeks = 52.1429
        values = dental, wrist, head, chest, abdomen, coffee, bananas, beer, location
        conv = lambda i: i or 0
        res = [conv(i) for i in values]
        values = res[:]

        q1 = (values[0]*database['Dental'][0]) + (values[1]*database['Wrist'][0])
        q2 = (values[2]*database['CT_head'][0]) + (values[3]*database['CT_chest'][0]) + (values[4]*database['CT_abdomen'][0])
        q3 = (values[5]*database['Coffee'][0]) * weeks # For an annual dose
        q4 = (values[6]*database['Banana'][0]) * weeks
        q5 = (values[7]*database['Pint'][0]) * weeks
        q6 = (values[8]) # where you live ??
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
        time.sleep(1.1)
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
        time.sleep(1.1)
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
