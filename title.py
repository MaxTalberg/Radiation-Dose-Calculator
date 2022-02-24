from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout

def get_title(app):
    layout = html.Div(
        dbc.Container(
            [
                html.H1("Radiation Dose Calculator", className="display-3"),
                html.P(
                    "Discover your radiation exposure from everyday activities by answering the questions and clicking calculate",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "Radiation is part of our everyday life. Did you know there is naturally occuring radiation in the food you eat,.."
                ),
                html.P(
                    "Want to learn more? Check out our fact sheet below"
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