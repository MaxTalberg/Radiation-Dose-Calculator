#################################################################################################################
#Date Created: 08/03/20222
#Authors: Max Talberg & Funmi Looi-Somoye (University of Bath)
#Purpose: This code pulls together separete elements to create the webpage.
#Sources of Data: database.csv (contains effective dose for each activity)
#                radon_data.csv (contains radon effective dose for each county)


#################################################################################################################


#Import Libraries
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import time
from header import get_header
from title import get_title

from questions.xray import get_question1, pplant_image
from questions.ct import get_question2, home_image
from questions.coffee import get_question3, coffee_image
from questions.banana import get_question4, banana_image
from questions.beer import get_question5, beer_image
from questions.home import get_question6
from questions.holiday import get_question7
from questions.background import get_question8
from answers.button import get_button
from answers.results_one import get_result1
from questions.answer import get_answer


#Hex Colours
EDF_BLUE = '#103579'
EDF_ORANGE = '#ff5716'
Miles_Blue = '#64c3db'
Miles_Orange = '#e3652e'

#Database
database = pd.read_csv('assets/database.csv')
location = pd.read_csv('assets/radon_data.csv')

#Quick clean
clean_location = location.drop(labels=0, axis=0)
Name = clean_location["County or Area Name"].tolist()
Dose = clean_location["Effective Dose"].tolist()


#Dashboard
def get_dashboard_layout(app):

    #Layout begins
    layout = html.Div([

        #Import Header
        get_header(app=app),

        #Import Title
        get_title(app=app),

        #Import Questions
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
        html.Br(),
        get_question8(app=app),
        html.Br(),

        #Create Calculate Button
        get_button(app=app),
        html.Br(),
        html.Div(id ='row-one-output'),
        html.Br(),
        html.Div(id='row-two-output'),

        #Create output graphs
        dbc.Row([
            dbc.Col([
                html.I('')
            ], width=1),
            dbc.Col([
                html.Div(id='total-radiation'),
                html.Div(id='tabs-graph'),
                html.Div(id='tabs-content'),
                dcc.Store(id='store-data-output')
            ], width=10),
            dbc.Col([
                html.I('')
            ], width=1)
        ], id='output-row'),

        html.Br(),
        html.Br(),
        dbc.Row(),
        dbc.Row(),

        #Footer (authors and acknowledgements)
        dbc.Row([
            dbc.Col([
                html.I('')
            ], width=1),
            dbc.Col([
                html.Div(
                         'Created by: Max Talberg & Funmi Looi-Somoye'
                ),
                html.Div([
                    html.A("Acknowledgements", href='https://github.com/MaxTalberg/PH30096/blob/master/Acknowledgements', target="_blank")
                ])
            ], width=10),
            dbc.Col([
                html.I('')
            ], width=1)
        ], id='contact-row'),

        html.Br()

    ])





# Data store callback
    @app.callback(
        Output(component_id='store-data-output', component_property='data'),
        [Input(component_id='Q-1a-ddown', component_property='value'),
         Input(component_id='Q-1b-ddown', component_property='value'),
         Input(component_id='Q-2a-ddown', component_property='value'),
         Input(component_id='Q-2b-ddown', component_property='value'),
         Input(component_id='Q-2c-ddown', component_property='value'),
         Input(component_id='Q-3a-ddown', component_property='value'),
         Input(component_id='Q-4a-ddown', component_property='value'),
         Input(component_id='Q-5a-ddown', component_property='value'),
         Input(component_id='Q-6a-ddown', component_property='value'),
         Input(component_id='Q-7a-ddown', component_property='value'),
         Input(component_id='Q-7b-ddown', component_property='value'),
         Input(component_id='Q-7c-ddown', component_property='value')

         ]
    )
    def organise_data(dental, wrist, head, chest, abdomen, coffee, bananas, beer, location, long, short, days):
        count = 0
        if location is None:
            location = 0
        else:
            location = float(Dose[(Name.index(location))])
        weeks = 52.1429
        values = dental, wrist, head, chest, abdomen, coffee, bananas, beer, location, long, short, days
        conv = lambda i: i or 0
        res = [conv(i) for i in values]
        values = res[:]

        q1 = (values[0]*database['Dental'][0]) + (values[1]*database['Wrist'][0])
        q2 = (values[2]*database['CT_head'][0]) + (values[3]*database['CT_chest'][0]) + (values[4]*database['CT_abdomen'][0])
        q3 = (values[5]*database['Coffee'][0]) * weeks #For an annual dose
        q4 = (values[6]*database['Banana'][0]) * weeks
        q5 = (values[7]*database['Pint'][0]) * weeks
        q6 = (values[8])
        q7 = (values[9]*database['Plane'][0]) + (values[10]*database['long_flight'][0]) + (values[11]*(database['Cornwall'][0])) # MADE CHANGES CHECK!!!
        Total_ED = q1 + q2 + q3 + q4 + q5 + q6 + q7 + database['Cosmic'][0]
        data_output = [Total_ED, q1, q2, q3, q4, q5, q6, q7]
        return data_output

# Load button
    @app.callback(
        Output(component_id='loading-output-1', component_property='children'),
        [Input(component_id='submit-val', component_property='n_clicks')]
    )
    def load_sign(n_clicks):
        time.sleep(1)
        return
# Result row 1
    @app.callback(
        Output(component_id='row-one-output', component_property='children'),
        [Input(component_id='submit-val', component_property='n_clicks'),
         Input(component_id='store-data-output', component_property='data')]
    )
    def update_row1(n_clicks, data):
        time.sleep(1.1)
        total = data[0]
        # Effective dose card
        card_content_one = [
            dbc.CardHeader(children=[
                html.H5(children=['Your Total Effective Dose'], style={'display': 'inline-block'}),
                html.Div(children=[
                    html.I(className="fa fa-info-circle")
                ], style={'display': 'inline-block',
                          'margin-left': '10px'},
                    id='result-1'),
                dbc.Tooltip(
                    html.Div([
                        "Did you know Funmi is the best project partner in the world!"
                    ]),
                    target='result-1',
                    placement='right'
                )
            ]),
            dbc.CardBody(
                html.H5('{:,} mSv'.format(round(total, 2)).replace(',', ' ,'))
            )
        ]
        # Output content and image card
        card_content_two = [
            dbc.CardBody(children=[
                html.Div(
                    dbc.Row([
                        dbc.Col(children=[
                            html.Div(id='radio-content')
                        ], width=8),
                        dbc.Col(children=[
                            html.Div(id='radio-image')
                        ], width=4)
                    ]),
                ),
            ])
        ]
        # Select an option card
        card_content_three = [
            dbc.CardHeader(
                html.H5(children=['Select an option'], style={'display': 'inline-block'})
            ),
            dbc.CardBody(
                html.Div(id='radio-items')
            ),
        ]
        # Result row one layout
        layout = html.Div(
            dbc.Row([

                # Margin 1
                dbc.Col([
                    html.I('')
                ], width=1),

                dbc.Col([
                    dbc.Card(card_content_one, color="warning", outline=True),
                    html.Br(),
                    dbc.Card(card_content_three, color="warning", outline=True)
                ], width=3),

                dbc.Col([
                    dbc.Card(card_content_two, color="warning", outline=True)
                ], width=7),

                dbc.Col([
                    html.I('')
                ], width=1)
            ]),
        )

        while n_clicks != 0:
            return layout
# Results row 2
    @app.callback(
        Output(component_id='row-two-output', component_property='children'),
        [Input(component_id='submit-val', component_property='n_clicks'),
         Input(component_id='store-data-output', component_property='data')]
    )
    def update_row2(n_clicks, data):
        time.sleep(1.11)
        tabs = html.Div([
            dbc.Row([

                # Margin 1
                dbc.Col([
                    html.I('')
                ], width=1),

                dbc.Col([html.Div(
                    dcc.Tabs(id='tab-graph', value='tab-graph-value', children=[
                        dcc.Tab(label='Results', value='tab-1'),
                        dcc.Tab(label='Compare to Nuclear Powerplants', value='tab-2')
                    ])
                ),

                ], width=10),

                dbc.Col([
                    html.I('')
                ], width=1)
            ]),
        ])
        while n_clicks != 0:
            return tabs

# Update tabs
    @app.callback(
        Output(component_id='tabs-content', component_property='children'),
        [Input(component_id='tab-graph', component_property='value'),
         Input(component_id='store-data-output', component_property='data')]
    )
    def render_content(tab, data):
        # [Total_ED, q1, q2, q3, q4, q5, q6, q7]
        xrays = data[1]
        ct = data[2]
        coffee = data[3]
        banana = data[4]
        pint = data[5]
        home = data[6]
        travel = data[7]
        background = database['Cosmic'][0]
        total = data[0]
        medical_scans= xrays+ct
        food_drink = coffee + banana + pint

        if tab == 'tab-1':
            return html.Div([
                html.Br(),
                html.H5('How your exposure compares to living near a nuclear power station or working in a nuclear power station'),
                dcc.Graph(
                    id='graph-1-tabs',
                    figure={
                        'data': [
                            {'x': ["Total Effective Dose"], 'y': [total], 'type': 'bar','name': 'Total effective dose', 'marker' : {"color": '#eb9628'} },
                            {'x': ["Living Near a Plant"], 'y': [database['living_plant'][0]], 'type': 'bar', 'name': 'Living 50 miles from a nuclear powerplant', 'marker' : {"color": '#15bccf'}},
                            {'x': ["Nuclear Plant Worker"], 'y': [database['nuclear_worker'][0]], 'type': 'bar', 'name': u'Working in a nuclear plant', 'marker' : {"color": '#3864d1'}},
                            {'x': ["Total Effective Dose", "Living Near a Plant", "Nuclear Plant Worker"], 'y': [database['uk_limit'][0], database['uk_limit'][0],database['uk_limit'][0]],
                             'type': 'line', 'name': 'UK Limit for Occupational Workers'},
                        ],
                        'layout': {
                            'xaxis': {
                                'title': 'Comparisons'
                            },
                            'yaxis': {
                                'title': 'Effective Dose [mSv]'
                            },
                        }
                    }
                )
            ])
        if tab == 'tab-2':
            fig_data = [
                {'values': [background, medical_scans, food_drink, home, travel],
                 'labels': ["Cosmic Background Radiation", "Medical Scans", "Food and Drink","Home Location",
                            "Holidays"],
                 'color': ['#3bdb66', '#6cc6f0', '#c8f06c', '#1f3e78', '#723db8'],
                 'type': 'pie',
                 },
            ]
            return html.Div([
                html.Br(),
                html.H5('Summary of your sources of radiation exposure'),
                dcc.Graph(
                    id='graph-2-tabs',
                    figure={
                        'data': fig_data,
                    }
                )
            ])

# Update option card
    @app.callback(
        Output(component_id='radio-items', component_property='children'),
        [Input(component_id='submit-val', component_property='n_clicks')]
    )
    def render_items(n_clicks):
        while n_clicks != 0:
            radio_items = html.Div([
                dcc.RadioItems(id='radio-items',
                               options=[
                                   {'label': 'Living near a nuclear power station', 'value': 'living'},
                                   {'label': 'Working in a nuclear power station', 'value': 'power-plant'},
                                   ], labelStyle={'display': 'block'})
            ])
            return radio_items
# Update results card
    @app.callback(
        Output(component_id='radio-content', component_property='children'),
        Output(component_id='radio-image', component_property='children'),
        [Input(component_id='radio-items', component_property='value'),
         Input(component_id='store-data-output', component_property='data')]
    )
    def render_output(value, data_output):
        Total_ED = data_output[0]
        living_near = Total_ED/database['living_plant'][0]
        pplant = Total_ED/database['nuclear_worker'][0]
        if value == 'living':
            out = html.Div([
                html.Br(),
                html.Div([
                    html.H4('Your activities across a year expose you to the same radiation as')
                ], style={"textAlign": "center"}),
                html.Br(),
                html.Div([
                    html.H1('{:,}'.format(round(living_near)).replace(',', ' ,'))
                ], style={"textAlign": "center"}),
                html.Br(),
                html.Div([
                    html.H4('years living near a nuclear power station!')
                ], style={"textAlign": "center"})
            ])
            image = html.Div([
                html.Br(),
                html.Br(),
                home_image])
        elif value == 'power-plant':
            out = html.Div([
                html.Br(),
                html.Div([
                    html.H4('Your activities across a year expose you to the same radiation as')
                ], style={"textAlign": "center"}),
                html.Br(),
                html.Div([
                    html.H1('{:,}'.format(round(pplant)).replace(',', ' ,'))
                ], style={"textAlign": "center"}),
                html.Br(),
                html.Div([
                    html.H4('years working in a nuclear power station!')
                ], style={"textAlign": "center"})
            ])
            image = html.Div([
                html.Br(),
                html.Br(),
                pplant_image])
        else:
            out = html.Div([
                html.I('Select an option to find out what your effective dose means...')
            ], style={"textAlign": "center"}),
            image = html.Div([
            ])
        return out, image

    return layout
