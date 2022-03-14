from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout
card_content_one = [
    dbc.CardHeader(
        html.Div([
            html.H5(['Total Effective Dose'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='result-1'),
            dbc.Tooltip(
                html.Div([
                    "Did you know, we all experience radiation coming from space?", html.Br(),
                    "X-rays travel through our atmosphere and arrive on the Earth's surface", html.Br(), html.Br(),
                    "The amount of radiation varies with your altitude but typically, in the UK we experience 2.3mSv a year",
                    html.Br(),
                    html.Br(),
                    html.I("(This is the same as 23,000 bananas)")]),
                target='result-1',
                placement='right'
                )
        ])
    ),

    dbc.CardBody(
        [
            dbc.Row([
                dbc.Col([
                    html.Div([
                        #html.H5('{:,} mSv'.format(round(total, 2)).replace(',', ' ,')),
                        "NOoOOn"

                    ], style={"width": "50%"}),
                ], width=5),
            ])

        ]
    )
]

card_content_two = [
    dbc.CardHeader(),
    dbc.CardBody()
]


def get_result1(app):
    layout = html.Div(
        dbc.Row([

            #Margin 1
            dbc.Col([
                html.I('')
            ], width=1),

            dbc.Col([
                dbc.Card(card_content_one, color="warning", outline=True)
            ], width=6),

            dbc.Col([
                dbc.Card(card_content_two, color="warning", outline=True)
            ], width=3),

            dbc.Col([
                html.I('')
            ], width=1),

            dbc.Col([
                html.I('')
            ], width=1)
        ]),
    )

    return layout

'''    def update_row1(n_clicks, data):
        time.sleep(1.1)
        total = data[0]
        card_content_one = [
            dbc.CardHeader(
                html.Div([
                    html.H5(['Total Effective Dose'], style={'display': 'inline-block'}),
                    html.Div([
                        html.I(className="fa fa-info-circle")
                    ], style={'display': 'inline-block',
                              'margin-left': '10px'},
                        id='result-1'),
                    dbc.Tooltip(
                        html.Div([
                            "Did you know, we all experience radiation coming from space?", html.Br(),
                            "X-rays travel through our atmosphere and arrive on the Earth's surface", html.Br(),
                            html.Br(),
                            "The amount of radiation varies with your altitude but typically, in the UK we experience 2.3mSv a year",
                            html.Br(),
                            html.Br(),
                            html.I("(This is the same as 23,000 bananas)")]),
                        target='result-1',
                        placement='right'
                    )
                ])
            ),
            dbc.CardBody(
                [
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H5('{:,} mSv'.format(round(total, 2)).replace(',', ' ,')),
                            ], style={"width": "50%"}),
                        ], width=5),
                    ])

                ]
            )
        ],
        card_content_two = [
            dbc.CardHeader(),
            dbc.CardBody()
        ]
        layout = html.Div(
            dbc.Row([

                # Margin 1
                dbc.Col([
                    html.I('')
                ], width=1),

                dbc.Col([
                    dbc.Card(card_content_one, color="warning", outline=True)
                ], width=6),

                dbc.Col([
                    dbc.Card(card_content_two, color="warning", outline=True)
                ], width=3),

                dbc.Col([
                    html.I('')
                ], width=1),

                dbc.Col([
                    html.I('')
                ], width=1)
            ]),
        )

        return layout'''