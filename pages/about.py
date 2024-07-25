from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='About',
    top_nav=True,
    path='/about'
)


def layout():
    layout = html.Div(style={'marginLeft': '20px'}, children=[
        html.H3('About this dashboard...', style={'marginTop': '20px'}),
        html.H4('NVIDIA Jetson Orin Nanos...', style={'marginTop': '20px'})
    ])
    return layout