#################################################################################################################
#Date Created: 08/03/20222
#Authors: Max Talberg & Funmi Looi-Somoye (University of Bath)
#Purpose: This code ????l
#################################################################################################################


import dash
import dash_bootstrap_components as dbc
from layout import get_dashboard_layout

# dashboard dash app
external_stylesheets = [dbc.themes.BOOTSTRAP,
                        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
                        ]

app = dash.Dash(name='radiation_app',
                suppress_callback_exceptions=True,
                external_stylesheets=external_stylesheets,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0,  maximum-scale=1.2, minimum-scale=0.5'}],
                )

theme = {
    'dark': True,
    'detail': '#103579',
    'primary': '#00EA64',
    'secondary': '#ff5716',
}

server = app.server
app.layout = get_dashboard_layout(app=app)


if __name__ == '__main__':
    app.run_server(debug=False)
