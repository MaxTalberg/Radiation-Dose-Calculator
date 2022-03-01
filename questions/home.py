from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
# Data
location = pd.read_csv('assets/radon_data.csv')

#Quick clean
clean_location = location.drop(labels=0, axis=0)
Name = clean_location["County or Area Name"].tolist()
Dose = clean_location["Effective Dose"].tolist()

# App layout
card_content = [
    dbc.CardHeader(
        html.Div([
            html.H5(['Where do you live?'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='question-6'),
            dbc.Tooltip(
                html.Div([
                    "The levels of naturally occurring radioactive radon vary across the UK", html.Br(),
                    "", html.Br(),
                    ""
                          ]),
                target='question-6',
                placement='right'
                )
        ])
    ),

    dbc.CardBody(
        [
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.I('Select your county'),
                        dcc.Dropdown(id='Q-6a-ddown',
                                     options=[
                                         {"label": i, "value": i} for i in Name
                                         ])
                    ], style={"width": "5"}),
                ], width=7),
            ])

        ]
    )
]

image = html.Div([
    html.Img(id="live-logo",
             src='/assets/map_black.png',
             height=130,
             width=130,
             style={'align-items': 'center'})
])

def get_question6(app):
    layout = html.Div(
        dbc.Row([

            #Margin 1
            dbc.Col([
                html.I('')
            ], width=1),

            dbc.Col([
                dbc.Card(card_content, color="warning", outline=True)
            ], width=6),

            dbc.Col([
                html.I('')
            ], width=1),

            dbc.Col([
                image
            ], width=3),

            dbc.Col([
                html.I('')
            ], width=1)
        ]),
    )

    return layout