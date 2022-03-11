#################################################################################################################
#Date Created: 08/03/20222
#Authors: Max Talberg & Funmi Looi-Somoye (University of Bath)
#Purpose: This code creates the title of the webpage)
#################################################################################################################



#Imports
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
                    "Radiation is part of our everyday life. It is even present in the food we eat!",
                ),
                html.P(
                    "Did you know, your normal day-to-day activities expose you to more radiation than someone working in a nuclear power plant for a year?",
                ),
                html.P(

                    "To understand more, test out the tool below and discover your everyday radioactive activities by pressing calculate.",
                ),
                html.P(
                    "Check out our fact sheet below to learn more:"
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