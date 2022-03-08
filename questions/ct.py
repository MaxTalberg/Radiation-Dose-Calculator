#################################################################################################################
#Date Created: 08/03/20222
#Authors: Max Talberg & Funmi Looi-Somoye (University of Bath)
#Purpose: This code creates the ct scan question
#Images: ct_black.png
#################################################################################################################



from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout
card_content = [
    dbc.CardHeader(
        html.Div([
            html.H5(['How many CT scans have you had this year?'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='question-2'),
            dbc.Tooltip(
                html.Div(["CT Scans form images of your body using many x-rays. X-rays subject your body to a amount of radiation", html.Br(),
                          "Effective Dose: 1.4mSv (Head CT Scan), 6.6mSv (Chest CT Scan) and  10mSv (Abdomen CT Scan)", html.Br(), html.Br(),
                          html.I("(This is the same dose as eating 14,000 , 66,000 and 100,000 bananas)"),
                          ]),
                target='question-2',
                placement='right'
                )
        ])
    ),

    dbc.CardBody(
        [
            dbc.Row([
                #Drop down 1
                dbc.Col([
                    html.Div([
                        html.I('Head CT Scan'),
                        dcc.Dropdown(id='Q-2a-ddown',
                                     options=[
                                         {"label": value, "value": value} for value in range(5)])
                    ], style={"width": "2.5"})
                    ], width=3),

                dbc.Col([
                    html.Div([])
                ], width=1),

                dbc.Col([
                    html.Div([
                        html.I('Chest CT Scan'),
                        dcc.Dropdown(id='Q-2b-ddown',
                                     options=[
                                         {"label": value, "value": value} for value in range(5)])
                    ], style={"width": "2.5"})
                ], width=3),

                dbc.Col([
                    html.Div([
                        html.I('Abdomen CT Scan'),
                        dcc.Dropdown(id='Q-2c-ddown',
                                     options=[
                                         {"label": value, "value": value} for value in range(5)])
                    ], style={"width": "2.5"}),
                    ], width=3),

                dbc.Col([
                    html.Div([])
                ], width=2),
            ])

        ]
    )
]

image = html.Div([
    html.Img(id="ct-logo",
             src='/assets/ct_black.png',
             height=100,
             width=100,
             style={'align-items': 'center'})
])

home_image = html.Div([
    html.Img(id="home-logo",
             src='/assets/home_black.png',
             height=100,
             width=100,
             style={'align-items': 'center'})
])

def get_question2(app):
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