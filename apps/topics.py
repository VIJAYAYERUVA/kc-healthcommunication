import dash_bootstrap_components as dbc
import dash_html_components as html

layout = dbc.Container([
    dbc.Row(id='title',
            children=[
                dbc.Col([
                    html.H2("Explore the Topics", className='text-center font-weight-bold ml-4 mr-4 mt-4 mb-4')
                ],
                    xs=12, sm=12, md=12, lg=12, xl=12),
            ],
            justify='center',
            align='center',
            # className='mb-4'
            ),
    dbc.Row(id='pyLDA',
            children=[
                dbc.Col([
                    html.H3('pyLDA Visualization of Topics'),
                    html.ObjectEl(
                        # To my recollection you need to put your static files in the 'assets' folder
                        data='../assets/pyLDAtopics.html',
                        type="application/pdf",
                        style={"width": "80vw", "height": "100vh"},
                    ),
                ],
                    xs=12, sm=12, md=12, lg=12, xl=12),
            ],
            justify='center',
            align='center',
            className='mb-4'
            ),
    dbc.Row(id='wordcloud_title',
            children=[
                dbc.Col([
                    html.H3("Word clouds of Topics", className='text-center font-weight-bold ml-4 mr-4 mt-4 mb-4')
                ],
                    xs=12, sm=12, md=12, lg=12, xl=12),
            ],
            justify='center',
            align='center',
            # className='mb-4'
            ),
    dbc.Row(id='wordcloud_row1',
            children=[
                dbc.Col([
                    html.H6('Topic 1'),
                    html.Img(src='../assets/Topic3_wordcloud.png'),

                ],
                    xs=12, sm=12, md=12, lg=6, xl=6),
                dbc.Col([
                    html.H6('Topic 2'),
                    html.Img(src='../assets/Topic1_wordcloud.png'),

                ],
                    xs=12, sm=12, md=12, lg=6, xl=6),
            ],
            justify='center',
            align='center',
            className='mb-4'
            ),
    dbc.Row(id='wordcloud_row2',
            children=[
                dbc.Col([
                    html.H6('Topic 3'),
                    html.Img(src='../assets/Topic0_wordcloud.png'),

                ],
                    xs=12, sm=12, md=12, lg=6, xl=6),
                dbc.Col([
                    html.H6('Topic 4'),
                    html.Img(src='../assets/Topic2_wordcloud.png'),

                ],
                    xs=12, sm=12, md=12, lg=6, xl=6),
            ],
            justify='center',
            align='center',
            className='mb-4'
            ),

],
    fluid=True)
