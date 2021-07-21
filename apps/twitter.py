import pathlib

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# colors
cities = {
    'Kansas City,MO': '#264653',
    'Long Beach,CA': '#2a9d8f',
    'Omaha,NE': '#f4a261',
    'Raleigh,NC': '#e76f51'
}
sentiment = {
    'positive': '#7197cf',
    'negative': '#e76d59',
    'neutral': '#c7cdd5'
}
emotions = {
    'anger': '#ff6700',
    'joy': '#ffd400',
    'optimism': '#820263',
    'sadness': '#004e98'
}
topics = {'Topic 1': '#4573a7',
          'Topic 2': '#aa4644',
          'Topic 3': '#89a54e',
          'Topic 4': '#71588f'
          }

# labels
labels = {
    "city": "City, State",
    'VADER_Sentiment': 'VADER Sentiment',
    "NoOfTweets": "#Tweets",
    'positive': 'Positive',
    'negative': 'Negative',
    'neutral': 'Neutral'
}

# ---------- Import and clean data (importing csv into pandas)
data = pd.read_csv(DATA_PATH.joinpath("Tweets.csv"))

city_list = data['city'].value_counts().index.tolist()

layout = html.Div([
    html.H1("Twitter Data", style={'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Label('Select year to check number of tweets'),
            dcc.Dropdown(id="slct_year1",
                         options=[{'label': year, 'value': year} for year in ['Both', 2020, 2021]],
                         multi=False,
                         value='Both',
                         style={'width': "100%"}
                         ),
            html.Div(id='output_container1', children=[])
        ]),
        html.Div([
            dcc.Graph(id='tweets_count', figure={}),
        ]),
    ],
        style={
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px',
            'font_family': 'Rockwell',
            'width': '49%',
            'display': 'inline-block'
        }
    ),
    html.Div([
        html.Div([
            html.Label('Select year to check VADER Sentiment in tweets'),
            dcc.Dropdown(id="slct_year2",
                         options=[{'label': year, 'value': year} for year in ['Both', 2020, 2021]],
                         multi=False,
                         value='Both',
                         style={'width': "100%"}
                         ),
            html.Div(id='output_container2', children=[])
        ]),

        html.Div([
            dcc.Graph(id='tweets_sentiment', figure={}),
        ])

    ],
        style={
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px',
            'font_family': 'Rockwell',
            'width': '49%',
            'float': 'right',
            'display': 'inline-block'
        }
    ),
    html.Div([
        html.Div([
            html.Label('Select year to check BERT Emotion in tweets'),
            dcc.Dropdown(id="slct_year3",
                         options=[{'label': year, 'value': year} for year in ['Both', 2020, 2021]],
                         multi=False,
                         value='Both',
                         style={'width': "100%"}
                         ),
            html.Div(id='output_container3', children=[])
        ]),

        html.Div([
            dcc.Graph(id='tweets_emotion', figure={}),
        ])
    ],
        style={
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px',
            'font_family': 'Rockwell',
            'width': '49%',
            'display': 'inline-block'
        }
    ),
    html.Div([
        html.Div([
            html.Label('Select year to check Topics in tweets'),
            dcc.Dropdown(id="slct_year4",
                         options=[{'label': year, 'value': year} for year in ['Both', 2020, 2021]],
                         multi=False,
                         value='Both',
                         style={'width': "100%"}
                         ),
            html.Div(id='output_container4', children=[])
        ]),

        html.Div([
            dcc.Graph(id='tweets_topic', figure={}),
        ])
    ],
        style={
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px',
            'font_family': 'Rockwell',
            'width': '49%',
            'float': 'right',
            'display': 'inline-block'
        }
    ),
    html.Div([
        html.Div([

            html.Div([
                html.Label('Select Year'),
                dcc.Dropdown(id="slct_year5",
                             options=[{'label': y, 'value': y} for y in [2020, 2021]],
                             multi=False,
                             value=2020,
                             style={'width': "100%"}
                             ),
                html.Div(id='output_container5', children=[])
            ],
                style={'width': '49%', 'display': 'inline-block'}),

            html.Div([
                html.Label('Select City'),
                dcc.Dropdown(id="slct_city",
                             options=[{'label': c, 'value': c} for c in sorted(city_list)],
                             multi=False,
                             value='Kansas City,MO',
                             style={'width': "100%"}
                             ),
                html.Div(id='output_container6', children=[])
            ],
                style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
        ],
            style={
                'borderBottom': 'thin lightgrey solid',
                'backgroundColor': 'rgb(250, 250, 250)',
                'padding': '10px 5px',
                'font_family': 'Rockwell'
            }),

        html.Div([
            dcc.Graph(id='tweets_count_month', figure={}),
        ])
    ],
        style={
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px',
            'font_family': 'Rockwell'
        }
    )
], style={'font-family': 'Rockwell'})


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container1', component_property='children'),
     Output(component_id='tweets_count', component_property='figure'),
     Output(component_id='output_container2', component_property='children'),
     Output(component_id='tweets_sentiment', component_property='figure'),
     Output(component_id='output_container3', component_property='children'),
     Output(component_id='tweets_emotion', component_property='figure'),
     Output(component_id='output_container4', component_property='children'),
     Output(component_id='tweets_topic', component_property='figure')],
    [Input(component_id='slct_year1', component_property='value'),
     Input(component_id='slct_year2', component_property='value'),
     Input(component_id='slct_year3', component_property='value'),
     Input(component_id='slct_year4', component_property='value')]
)
def update_graph_1(slct_year1, slct_year2, slct_year3, slct_year4):
    count = data.copy()

    print('Selected Year', slct_year1)
    container1 = "The year chosen by user was: {}".format(slct_year1)

    if slct_year1 == 'Both':
        df1 = (count.groupby(['city']).size()).reset_index()
        df1.rename(columns={0: 'NoOfTweets'}, inplace=True)

        # Plotly Express
        fig1 = px.bar(df1,
                      x="city",
                      y="NoOfTweets",
                      color='city',
                      labels=labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=cities,
                      text=df1['NoOfTweets']
                      )

        fig1.update_xaxes(title_text="")

        fig1.update_layout(
            title='<b>#Tweets from high minority population cities</b>',
            title_x=0.5,
            font_size=13,
            font_family='Rockwell',
            margin=dict(l=0, r=0, b=0),
            hoverlabel=dict(
                # bgcolor="white",
                font_size=16,
                font_family="Rockwell"),
            legend_title_text='City, State',
            autotypenumbers="strict",
            hoverlabel_align='right',
            legend=dict(
                orientation="h",
            )

        )
    else:
        df1 = count[count['Year'] == slct_year1]
        df1 = (df1.groupby(['Year', 'city']).size()).reset_index()
        df1.rename(columns={0: 'NoOfTweets'}, inplace=True)

        # Plotly Express
        fig1 = px.bar(df1,
                      x="city",
                      y="NoOfTweets",
                      color='city',
                      labels=labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=cities,
                      text=df1['NoOfTweets']
                      )

        fig1.update_xaxes(title_text="")

        fig1.update_layout(
            title='<b>#Tweets from high minority population cities in ' + str(slct_year1) + ' </b>',
            title_x=0.5,
            font_size=13,
            font_family='Rockwell',
            margin=dict(l=0, r=0, b=0),
            hoverlabel=dict(
                # bgcolor="white",
                font_size=16,
                font_family="Rockwell"),
            legend_title_text='City, State',
            autotypenumbers="strict",
            hoverlabel_align='right',
            legend=dict(
                orientation="h",
            )
        )

    senti = data.copy()

    print('Selected Year', slct_year2)
    container2 = "The year chosen by user was: {}".format(slct_year2)

    if slct_year2 == 'Both':
        df2 = (senti.groupby(['city', 'VADER_Sentiment']).size()).reset_index()
        df2.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig2 = px.bar(df2,
                      x="city",
                      y="NoOfTweets",
                      color="VADER_Sentiment",
                      # barmode='group',
                      labels=labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=sentiment,
                      category_orders={
                          "VADER_Sentiment": ["positive", 'neutral', "negative"]
                      },
                      text=df2['NoOfTweets'],
                      )

        fig2.update_xaxes(title_text="")

        fig2.update_layout(
            title='<b>#Tweets from high minority population cities with VADER Sentiment</b>',
            title_x=0.5,
            font_size=13,
            font_family='Rockwell',
            margin=dict(l=0, r=0, b=0),
            hoverlabel=dict(
                # bgcolor="white",
                font_size=16,
                font_family="Rockwell"),
            legend_title_text='VADER Sentiment',
            autotypenumbers="strict",
            hoverlabel_align='right',
            legend=dict(
                orientation="h",
            )
        )

    else:
        df2 = senti[senti['Year'] == slct_year2]
        df2 = (df2.groupby(['Year', 'city', 'VADER_Sentiment']).size()).reset_index()
        df2.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig2 = px.bar(df2,
                      x="city",
                      y="NoOfTweets",
                      color="VADER_Sentiment",
                      # barmode='group',
                      labels=labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=sentiment,
                      category_orders={
                          "VADER_Sentiment": ["positive", 'neutral', "negative"]
                      },
                      text=df2['NoOfTweets'],
                      )

        fig2.update_xaxes(title_text="")

        fig2.update_layout(
            title='<b>#Tweets from high minority population cities in ' + str(slct_year2) + ' with VADER Sentiment</b>',
            title_x=0.5,
            font_size=13,
            font_family='Rockwell',
            margin=dict(l=0, r=0, b=0),
            hoverlabel=dict(
                # bgcolor="white",
                font_size=16,
                font_family="Rockwell"),
            legend_title_text='VADER Sentiment',
            autotypenumbers="strict",
            hoverlabel_align='right',
            legend=dict(
                orientation="h",
            )
        )

    emotion = data.copy()

    print('Selected Year', slct_year3)
    container3 = "The year chosen by user was: {}".format(slct_year3)

    if slct_year3 == 'Both':
        df3 = (emotion.groupby(['city', 'BERT_Emotion']).size()).reset_index()
        df3.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig3 = px.bar(df3,
                      x="city",
                      y="NoOfTweets",
                      color="BERT_Emotion",
                      # barmode='group',
                      labels=labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=emotions,
                      category_orders={
                          "BERT_Emotion": ["anger", 'joy', 'optimism', 'sadness']
                      },
                      text=df3['NoOfTweets'],
                      )

        fig3.update_xaxes(title_text="")

        fig3.update_layout(
            title='<b>#Tweets from high minority population cities with BERT Emotion</b>',
            title_x=0.5,
            font_size=13,
            font_family='Rockwell',
            margin=dict(l=0, r=0, b=0),
            hoverlabel=dict(
                # bgcolor="white",
                font_size=16,
                font_family="Rockwell"),
            legend_title_text='BERT Emotion',
            autotypenumbers="strict",
            hoverlabel_align='right',
            legend=dict(
                orientation="h",
            )
        )

    else:
        df3 = emotion[emotion['Year'] == slct_year3]
        df3 = (df3.groupby(['Year', 'city', 'BERT_Emotion']).size()).reset_index()
        df3.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig3 = px.bar(df3,
                      x="city",
                      y="NoOfTweets",
                      color="BERT_Emotion",
                      # barmode='group',
                      labels=labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=emotions,
                      category_orders={
                          "BERT_Emotion": ["anger", 'joy', 'optimism', 'sadness']
                      },
                      text=df3['NoOfTweets'],
                      )

        fig3.update_xaxes(title_text="")

        fig3.update_layout(
            title='<b>#Tweets from high minority population cities in ' + str(slct_year3) + ' with BERT Emotion</b>',
            title_x=0.5,
            font_size=13,
            font_family='Rockwell',
            margin=dict(l=0, r=0, b=0),
            hoverlabel=dict(
                # bgcolor="white",
                font_size=16,
                font_family="Rockwell"),
            legend_title_text='BERT Emotion',
            autotypenumbers="strict",
            hoverlabel_align='right',
            legend=dict(
                orientation="h",
            )
        )

    topic = data.copy()

    print('Selected Year', slct_year4)
    container4 = "The year chosen by user was: {}".format(slct_year4)

    if slct_year4 == 'Both':
        df4 = (topic.groupby(['city', 'Dominant_Topic']).size()).reset_index()
        df4.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig4 = px.bar(df4,
                      x="city",
                      y="NoOfTweets",
                      color="Dominant_Topic",
                      # barmode='group',
                      labels=labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=sentiment,
                      category_orders={
                          "Dominant_Topic": ["Topic 1", 'Topic 2', "Topic 3", 'Topic 4']
                      },
                      text=df4['NoOfTweets'],
                      )

        fig4.update_xaxes(title_text="")

        fig4.update_layout(
            title='<b>#Tweets from high minority population cities with Dominant Topic</b>',
            title_x=0.5,
            font_size=13,
            font_family='Rockwell',
            margin=dict(l=0, r=0, b=0),
            hoverlabel=dict(
                # bgcolor="white",
                font_size=16,
                font_family="Rockwell"),
            legend_title_text='Dominant Topic',
            autotypenumbers="strict",
            hoverlabel_align='right',
            legend=dict(
                orientation="h",
            )
        )

    else:
        df4 = topic[topic['Year'] == slct_year4]
        df4 = (df4.groupby(['Year', 'city', 'Dominant_Topic']).size()).reset_index()
        df4.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig4 = px.bar(df4,
                      x="city",
                      y="NoOfTweets",
                      color="Dominant_Topic",
                      # barmode='group',
                      labels=labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=sentiment,
                      category_orders={
                          "Dominant_Topic": ["Topic 1", 'Topic 2', "Topic 3", 'Topic 4']
                      },
                      text=df4['NoOfTweets'],
                      )

        fig4.update_xaxes(title_text="")

        fig4.update_layout(
            title='<b>#Tweets from high minority population cities in ' + str(
                slct_year4) + ' with Dominant Topic</b>',
            title_x=0.5,
            font_size=13,
            font_family='Rockwell',
            margin=dict(l=0, r=0, b=0),
            hoverlabel=dict(
                # bgcolor="white",
                font_size=16,
                font_family="Rockwell"),
            legend_title_text='Dominant Topic',
            autotypenumbers="strict",
            hoverlabel_align='right',
            legend=dict(
                orientation="h",
            )
        )

    return container1, fig1, container2, fig2, container3, fig3, container4, fig4


@app.callback(
    [Output(component_id='output_container5', component_property='children'),
     Output(component_id='output_container6', component_property='children'),
     Output(component_id='tweets_count_month', component_property='figure')],
    [Input(component_id='slct_year5', component_property='value'),
     Input(component_id='slct_city', component_property='value')]
)
def update_graph_2(slct_year5, slct_city):
    dff1 = data.copy()
    print('Selected Year', slct_year5)
    container5 = "The year chosen by user was: {}".format(slct_year5)

    print('Selected City', slct_city)
    container6 = "The year chosen by user was: {}".format(slct_city)

    df5 = dff1[(dff1['Year'] == slct_year5) & (dff1['city'] == slct_city)]
    df5 = (df5.groupby(['Year', 'Month']).size()).reset_index()
    df5.rename(columns={0: 'NoOfTweets'}, inplace=True)

    fig5 = px.bar(df5,
                  x="Month",
                  y="NoOfTweets",
                  color="NoOfTweets",
                  labels=labels,
                  hover_name='Month',
                  hover_data={
                      "Month": False,
                  },
                  color_continuous_scale='Burg',
                  text=df5['NoOfTweets']
                  )

    fig5.update_layout(
        title='<b>#Tweets from ' + slct_city + ' in ' + str(slct_year5) + '</b>',
        title_x=0.5,
        font_size=13,
        font_family='Rockwell',
        margin=dict(l=0, r=0, b=0),
        hoverlabel=dict(
            # bgcolor="white",
            font_size=16,
            font_family="Rockwell"),
        legend_title_text='#Tweets',
        autotypenumbers="strict",
        hoverlabel_align='right',
        xaxis=dict(tickmode='linear')
    )

    return container5, container6, fig5
