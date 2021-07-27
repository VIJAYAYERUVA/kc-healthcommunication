import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server
# Connect to your app pages
from apps import twitter, topics

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Twitter Data|', href='/apps/twitter'),
        dcc.Link('Topics', href='/apps/topics'),
    ], className="row"),
    html.Div(id='page-content',
             children=[])
],
    style={'font-family': 'Rockwell',
           })


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/twitter':
        return twitter.layout
    if pathname == '/apps/topics':
        return topics.layout
    else:
        return "Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)
