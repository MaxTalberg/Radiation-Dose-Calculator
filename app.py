import dash

import dash_bootstrap_components as dbc

from layout import get_dashboard_layout

# dashboard dash app
app = dash.Dash(name='radiation_app',
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

server = app.server
app.layout = get_dashboard_layout(app=app)

if __name__ == '__main__':
    app.run_server(debug=False)