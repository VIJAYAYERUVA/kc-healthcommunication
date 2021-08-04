import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server
# Connect to your app pages
from apps import about, topics, twitter, data

app.layout = html.Div(
    [
        dcc.Location(
            id="url",
            pathname="/apps/about",
            refresh=False),
        dbc.NavbarSimple(
            children=[
                dbc.NavLink("Home", href="/apps/about", active="exact"),
                dbc.NavLink("Twitter Analytics", href="/apps/twitter", active="exact"),
                dbc.NavLink("Topics", href="/apps/topics", active="exact"),
                dbc.NavLink("Data", href="/apps/data", active="exact"),
            ],
            brand="Healthy Eastside KC-2021",
            brand_style={
                'font-size': '25px'
            },
            color="dark",
            dark=True,
            style={
                'font-size': '20px'
            },
        ),
        dbc.Container(
            id="page-content",
            className="pt-4",
            fluid=True),
    ]
)


@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/apps/about":
        return about.layout
    if pathname == "/apps/topics":
        return topics.layout
    if pathname == "/apps/twitter":
        return twitter.layout
    if pathname == "/apps/data":
        return data.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=False)
