import dash_bootstrap_components as dbc
# import dash_core_components as dcc
import dash_html_components as html

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Twitter COVID-19 Data", style={'text-align': 'center'}),
            html.P('This dashboard is to help navigating Twitter COVID-19 Data from minority cities')
        ])
    ])

])
