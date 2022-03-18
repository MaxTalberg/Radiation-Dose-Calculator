from dash import dcc, html
import dash_bootstrap_components as dbc

arrow_image = html.Div([
    html.Img(id="banana-logo",
             src='/assets/arrow_test.png',
             height=100,
             width=100,
             style={'align-items': 'center'})
])


def get_button(app):
    layout = html.Div(
        dbc.Row([
            dbc.Col([
                html.I('')
            ], width=1),
        dbc.Col([
            dbc.Button('Calculate', id='submit-val', n_clicks=0, style={'textTransform': 'none'}),
            dcc.Loading(
                id="loading-1",
                type="default",
                children=html.Div(id="loading-output-1")
            ),
        ], width=10),
            dbc.Col([
                html.I('')
            ], width=1)
        ], id='calculate-row'))
    return layout
