from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

#Created a navbar function that sets the navbar for each page of the web app
def create_navbar():
    navbar = dbc.NavbarSimple(
        brand='Minicluster Dashboard', 
        brand_href="/",
        brand_style={'fontSize' : '37px', 'marginRight' : '35px', 'marginLeft' : '20px'},
        color="light",
        light=True,
        style={'width' : '100%', 'display' : 'grid', 'textAlign' : 'left'},
        children=[
            dbc.NavItem(),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                style={'textAlign' : 'right', 'fontSize' : '20px'},
                align_end=True,
                children=[
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("About", href='/about'),
                ],
            ),
        ]
    )

    return navbar