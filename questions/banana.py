from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout
card_content = [
    dbc.CardHeader(
        html.Div([
            html.H5(['How many bananas do you eat a week?'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='question-4'),
            dbc.Tooltip(
                html.Div([
                    "Bananas are famous for containing radioactive nuclide potassium-40.", html.Br(),
                    "When you eat a banana you ingest a small dose of this nuclide.", html.Br(), html.Br(),
                    "Effective Dose: 0.01 mSv (per banana)"
                          ]),
                target='question-4',
                placement='right'
                )
        ])
    ),

    dbc.CardBody(
        [
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Dropdown(id='Q-4a-ddown',
                                     options=[
                                         {"label": value, "value": value} for value in range(21)])
                    ], style={"width": "50%"}),
                ], width=5),
            ])

        ]
    )
]

banana_image = html.Div([
    html.Img(id="banana-logo",
             src='/assets/banana_black.png',
             height=100,
             width=100,
             style={'align-items': 'center'})
])

def get_question4(app):
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
                banana_image
            ], width=3),

            dbc.Col([
                html.I('margin')
            ], width=1)
        ]),
    )

    return layout