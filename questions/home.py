from dash import dcc, html
import dash_bootstrap_components as dbc

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
                        dcc.Dropdown(id='Q-6a-ddown',
                                     options=[
                                         {"label": 'Sheffield', "value": 'london'},
                                         {"label": 'Rest of UK', "value": 'rest'}])
                    ], style={"width": "5"}),
                ], width=3),
            ])

        ]
    )
]

image = html.Div([
    html.Img(id="live-logo",
             src='/assets/xray.png',
             height=80,
             width=80,
             style={'align-items': 'center'})
])

def get_question6(app):
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