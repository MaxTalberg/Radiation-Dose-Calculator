from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout

def get_title(app):
    layout = html.Div(
        dbc.Container(
            [
                html.H1("Radiation Dose Calculator", className="display-3"),
                html.P(
                    "Discover your radiation exposure from everyday activities!",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "Radiation is part of our everyday life and this has a very small impact on our health.",
                ),
                html.P(
                    "Did you know, your normal day-to-day activities expose you to more radiation than someone working in a nuclear power plant for a year?",
                ),
                html.P(

                    "To understand more, test out the tool below and discover your everyday radioactive activities by pressing calculate.",
                ),
                html.P(
                    "Check out our fact sheet below to discover more:"
                ),

                html.P(
                    dbc.Button("Link to inforgraphics", color="primary", style={'textTransform': 'none'}), className="lead"
                ),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-light rounded-3",
    )

    return layout