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
                html.Div(["Get miles to write", html.Br(),
                          "", html.Br(),
                          ""
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
                                             {"label": value, "value": value} for value in range(5)])
                        ], style={"width": "5"}),
                    ])
                ], width=5),

                dbc.Col([
                    html.Div([
                        html.I('Short Haul'),
                        html.Div([
                            dcc.Dropdown(id='Q-7b-ddown',
                                         options=[
                                             {"label": value, "value": value} for value in range(5)])
                        ], style={"width": "5"}),
                    ])
                ], width=5),

                ]),

            dbc.Row([
                html.H5(""),
            ]),

            dbc.Row([
                html.Br(),
                html.Div([
                    html.I('How many days have you spent on a holiday to Cornwall?'),
                    html.Div([
                        dcc.Dropdown(id='Q-7c-ddown',
                                     options=[
                                         {"label": value, "value": value} for value in range(10)])
                    ], style={"width": "5"}),
                ]),
            ]),
        ]
    )
]

image = html.Div([
    html.Img(id="holiday-logo",
             src='/assets/xray.png',
             height=80,
             width=80,
             style={'align-items': 'center'})
])

def get_question7(app):
    layout = html.Div(
        dbc.Row([

            #Margin 1
            dbc.Col([
                html.I('margin')
            ], width=1),

            dbc.Col([
                dbc.Card(card_content, color="warning", outline=True)
            ], width=6),

            dbc.Col([
                html.I('margin')
            ], width=1),

            dbc.Col([
                image
            ], width=3),

            dbc.Col([
                html.I('margin')
            ], width=1)
        ]),
    )

    return layout