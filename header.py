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

            dbc.Col(
                    children=[
                        html.Img(id="logo",
                                 src=app.get_asset_url('1.png'),
                                 style={'textAlign': 'center', 'height': '10', 'width':'30'}),
                    ],
                    className="align-middle d-flex justify-content-center"),

        ])
    ],
    className='divSticky',
    style={'border-bottom': '2px solid #BEBEBE'}, )

    return layout
