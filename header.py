#################################################################################################################
#Date Created: 08/03/20222
#Authors: Max Talberg & Funmi Looi-Somoye (University of Bath)
#Purpose: This code creates the header of the webpage
#################################################################################################################



#Import
from dash import dcc, html
import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output


def get_button_header(id, label, active=False, visible=True, disabled=False, style=None):
    if not style:
        style = {'color': '#e3652e', 'font-size': '110%', 'outline': 'none', 'border': '2px solid black'}
        if active:
            style['background-color'] = '#e3652e'
        else:
            style['background-color'] = '#e3652e'
        if not visible:
            style['display'] = 'none'

    kwargs = dict(
        id=id,
        children=html.B(label),
        n_clicks=0,
        style=style,
        disabled=disabled
    )

    return html.Button(**kwargs)

# App layout

def get_header(app):
    layout = html.Div(

    id='page-header',

    children=[
        dbc.Row([
            dbc.Col([

            ], width=1),


            dbc.Col([
                html.Div([
                    html.Img(src='/assets/uob.png',
                             height='117', width='249',
                             style={'textAlign': 'left'}
                             ),
                ]),
            ], width=1),


            dbc.Col(
                children=[
                    html.Div([
                        #html.Img(id="logo",
                        #         src='/assets/uob.png',
                        #         height='64', width = '232',
                        #         style={'textAlign': 'center'}),
                    ]),
                ],width=8,
                className="align-middle d-flex justify-content-center"),

            dbc.Col([

            ], width=1),


            dbc.Col([
                html.Div([
                    #html.Img(src='/assets/edf-logo.svg',
                    #         height='70', width='70',
                    #         style={'textAlign': 'right'}
                    #         )
                ])
            ], width=1),



        ])
    ],
    className='divSticky',
    style={
        #'border-bottom': '2px solid #BEBEBE',
           'backgroundColor': '#F4F0F0'
    },
    )

    return layout
