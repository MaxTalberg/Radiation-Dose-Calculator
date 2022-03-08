#################################################################################################################
#Date Created: 08/03/20222
#Authors: Max Talberg & Funmi Looi-Somoye (University of Bath)
#Purpose: This code creates the cosmic background radtion question
#Images: sun_black.png
#################################################################################################################


from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout
card_content = [
    dbc.CardHeader(
        html.Div([
            html.H5(['Cosmic Background Radiation'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='question-8'),
            dbc.Tooltip(
                html.Div([
                    "Did you know, we all experience radiation coming from space?", html.Br(),
                    "X-rays travel through our atmosphere and arrive on the Earth's surface", html.Br(), html.Br(),
                    "The amount of radiation varies with your altitude but typically, in the UK we experience 2.3mSv a year"
                     ,html.Br(), html.Br(),
                    html.I("(This is the same as 23,000 bananas)")]),
                target='question-8',
                placement='right'
                )
        ])
    ),

    dbc.CardBody(
        [
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H5(' 2.3 mSv'),

                    ], style={"width": "50%"}),
                ], width=5),
            ])

        ]
    )
]

banana_image = html.Div([
    html.Img(id="no_logo",
             src='/assets/sun_black.png',
             height=100,
             width=100,
             style={'align-items': 'center'})
])

def get_question8(app):
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
                banana_image
            ], width=3),

            dbc.Col([
                html.I('')
            ], width=1)
        ]),
    )

    return layout