#Import Libraries
from dash import dcc, html, State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import time
from header import get_header
from title import get_title

from questions.xray import get_question1
from questions.ct import get_question2
from questions.coffee import get_question3
from questions.banana import get_question4
from questions.beer import get_question5
from questions.live import get_question6
from questions.holiday import get_question7



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

        #Header
        get_header(app=app),
        #Title
        get_title(app=app),

        #Questions
        get_question1(app=app),

        html.Br(),

        get_question2(app=app),

        html.Br(),

        get_question3(app=app),

        html.Br(),

        get_question4(app=app),

        html.Br(),

        get_question5(app=app),

        html.Br(),

        get_question6(app=app),

        html.Br(),

        get_question7(app=app),

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
            return html.H3('Your annual dose of'),\
                   html.H3('radiation is equivalent to '),\
                   html.H2('XXX'),\
                   html.H3('pints of beer!')
        elif value == 'banana':
            return html.H3('Your annual dose of'),\
                   html.H3('radiation is equivalent to '),\
                   html.H2('XXX'), \
                   html.H3('bananas!')
        elif value == 'power-plant':
            return html.H3('Your annual dose of'),\
                   html.H3('radiation is equivalent to '),\
                   html.H2(id='data'),\
                   html.H3('years working in a nuclear power plant!')
        elif value == 'coffee':
            return html.H3('Your annual dose of'),\
                   html.H3('radiation is equivalent to '),\
                   html.H2(id='data'), \
                   html.H3('coffees!')

    return layout
