from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout
card_content = [
    dbc.CardHeader(
        html.Div([
            html.H5(['1. '], style={'display': 'inline-block'}),
            html.H5(['How many xrays do you eat a week?'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='question-1'),
            dbc.Tooltip(
                html.Div(["X-rays subject the patient to small doses of radiation"
                          "Effective Dose: 0.005 mSv (dental x-ray) and 0.001 mSv (wrist x-ray)"
                          "This is the same dose as eating 1/2 and 1/10 of a banana"]),
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

image = html.Div([
    html.Img(id="xray-logo",
             src='/assets/xray.png',
             height=80,
             width=80,
             style={'align-items': 'center'})
])

def get_question1(app):
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

'''
            #Card
            dbc.Col([
                html.H5(['1. '], style={'display': 'inline-block'}),
                html.H5(['How many xrays do you eat a week?'], style={'display': 'inline-block'}),
                html.Div([
                    html.I(className="fa fa-info-circle")
                ], style={'display': 'inline-block',
                          'margin-left': '10px'},
                    id='question-1'),

                dbc.Tooltip(
                    html.Div(["X-rays subject the patient to small doses of radiation"
                              "Effective Dose: 0.005 mSv (dental x-ray) and 0.001 mSv (wrist x-ray)"
                              "This is the same dose as eating 1/2 and 1/10 of a banana"]),
                    target='question-1',
                    placement='right'
                )
            ], width=6),

            #Image
            dbc.Col([

            ], width=1),
                    dbc.Col([
                        html.Img(id="xray-logo",
                                 src='/assets/xray.png',
                                 height=80,
                                 width=80,
                                 style={'align-items': 'center'})
                    ], width=3),


            dbc.Col([
                html.I('margin')
            ], width=1)
        ], id='row-1-Q')

    )'''