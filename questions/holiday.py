#################################################################################################################
#Date Created: 08/03/20222
#Authors: Max Talberg & Funmi Looi-Somoye (University of Bath)
#Purpose: This code creates the flights and cornwall holiday question
#Images: holiday_black.png
#################################################################################################################


from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout
card_content = [
    dbc.CardHeader(
        html.Div([
            html.H5(['Have you been on holiday this year?'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='question-7'),
            dbc.Tooltip(
                html.Div(["Travelling in planes, at high altitude expose you to greater amounts of cosmic radiation fron the sun.", html.Br(),
                          "At higher altitudes, the air becomes thinner resulting in a lesser shielding effect from the air molecules ", html.Br(),html.Br(),
                          "Effective Dose: 0.065 mSv for a long haul flight to (London to Melbourne), and 0.0015 mSv for a short haul flight (London to Ibiza)",html.Br(),html.Br(),
                          html.I("(This is the same radiation dose as 650 and 15 bananas.)")
                          ]),
                target='question-7',
                placement='right'
                )
        ])
    ),

    dbc.CardBody(
        [
            #Secondary Questions
            dbc.Row([
                    dbc.Col([
                        html.H6(['How many flights have you taken?'], style={'display': 'inline-block'})
                ], id='row-7-extra'),

                ]),

            #Primary Drop Down

            dbc.Row([

                dbc.Col([
                    html.Div([
                        html.I('Long Haul'),
                        html.Div([
                            dcc.Dropdown(id='Q-7a-ddown',
                                         options=[
                                             {"label": value, "value": value} for value in range(11)])
                        ], style={"width": "5"}),
                    ])
                ], width=5),

                dbc.Col([
                    html.Div([
                        html.I('Short Haul'),
                        html.Div([
                            dcc.Dropdown(id='Q-7b-ddown',
                                         options=[
                                             {"label": value, "value": value} for value in range(11)])
                        ], style={"width": "5"}),
                    ])
                ], width=5),

                ]),

            dbc.Row([
                html.H5(""),
            ]),

            html.Br(),

            dbc.Row([
                html.Br(),
                html.Div([
                    html.H6('How many days have you spent on a holiday to Cornwall?', id='cornwall_qu'),
                    html.Div([

                        dcc.Dropdown(id='Q-7c-ddown',
                                     options=[
                                         {"label": value, "value": value} for value in range(11)])
                    ], style={"width": "5"}),

                    dbc.Tooltip(
                        html.Div(["Cornwall is known for having higher level of natural radioactive radon gas compared to other locations in the UK", html.Br(),
                          "The levels of radon are of course safe, and are always monitored by the government", html.Br(),
                          "To compare the average cornish person recieves 6.9 mSv/year and the average person in the UK recieves 1.3 mSv/year",html.Br(),html.Br(),
                        html.I("(This is the same as eating 69,000 bananas in a year vs 13,000 bananas in a year.)"),
                          ]),
                        target='cornwall_qu',
                        placement='right'
                )
                ]),
            ]),
        ]
    )
]

image = html.Div([
    html.Img(id="holiday-logo",
             src='/assets/holiday_black.png',
             height=110,
             width=110,
             style={'align-items': 'center',
                    "padding": "30"
                    })
])

def get_question7(app):
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