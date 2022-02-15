from dash import dcc, html
import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output


def get_button_header(id, label, active=False, visible=True, disabled=False, style=None):
    if not style:
        style = {'color': 'white', 'font-size': '110%', 'outline': 'none', 'border': '2px solid black'}
        if active:
            style['background-color'] = 'black'
        else:
            style['background-color'] = 'rgba(102,51,153,0.2)'
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
                html.Div([
                    html.Span(id="title", children='University of Bath x Sizewell C'),
                ], style={'padding-top': '15px'})
            ],
                width=3,
                className="align-middle"),
            dbc.Col(
                ),
            dbc.Col(
                    children=[
                        html.Img(id="edf-logo",
                                 src=app.get_asset_url('edf-logo.svg'),
                                 height=80,
                                 width=80,
                                 style={'padding-right': '10px'}),
                    ],
                    width=1,
                    className="align-middle d-flex justify-content-center"),

        ])
    ],
    className='divSticky',
    style={'border-bottom': '2px solid #BEBEBE'}, )

    return layout
