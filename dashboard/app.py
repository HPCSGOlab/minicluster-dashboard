import dash
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
from dash_extensions.enrich import html, dcc, Output, Input, DashProxy
from navbar import create_navbar

#create the nav bar for the application
navbar = create_navbar()
FA621 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"


#This app is multiple pages that work together to create the dashboard and an about page

#create the dash app
app = DashProxy(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.DARKLY,  FA621],
    use_pages=True,
)
app.title = 'Minicluster Dashboard'

#thid is the composition of the app
app.layout = [html.Div(children=[
                       html.Div([navbar, dash.page_container]),
                       ])]



#this runs the app with debug mode on
if __name__ == '__main__':
    app.run_server(debug=True)