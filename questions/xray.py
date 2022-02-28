from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout
card_content = [
    dbc.CardHeader(
        html.Div([
            html.H5(['How many x-rays have you had this year?'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='question-1'),
            dbc.Tooltip(
                html.Div(["X-rays subject the patient to small amount of x-ray radiation.", html.Br(),
                          "X-rays are useful because they can penetrate through the body, allowing doctors to see organs and bones", html.Br(),
                          "Effective Dose: 0.005 mSv (dental x-ray) and 0.001 mSv (wrist x-ray)", html.Br(), html.Br(),
                          html.I("(This is the same dose as eating 1/2 and 1/10 of a banana)"),
                          ]),
                target='question-1',
                placement='right'
                )
        ])
    ),

    dbc.CardBody(
        [
            dbc.Row([

                dbc.Col([
                    html.Div([
                        html.I('Dental X Ray'),
                        dcc.Dropdown(
                            id='Q-1a-ddown',
                            options=[
                                {"label": value, "value": value} for value in range(6)])
                    ], style={"width": "50%", 'align-items': 'center'})
                ], width=5),

                dbc.Col([
                    html.Div([])
                ], width=2),

                dbc.Col([
                    html.Div([
                        html.I('Wrist X Ray'),
                        dcc.Dropdown(id='Q-1b-ddown',
                                     options=[
                                         {"label": value, "value": value} for value in range(5)])
                    ], style={"width": "50%",'align-items': 'center'})
                ], width=5)
            ])

        ]
    )
]

xray_image = html.Div([
    html.Img(id="xray-logo",
             src='/assets/xray_black.png',
             height=100,
             width=100,
             style={'align-items': 'center'})

])

pplant_image = html.Div([
    html.Img(id="pplant-logo",
             src='/assets/pplant_black.png',
             height=100,
             width=100,
             style={'align-items': 'center'})
])

def get_question1(app):
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
                xray_image
            ], width=3),

            dbc.Col([
                html.I('')
            ], width=1)
        ]),
    )

    return layout