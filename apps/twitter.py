import pathlib

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

from app import app
from assets import style_sheet

pd.options.mode.chained_assignment = None

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# ---------- Import and clean data (importing csv into pandas)
data = pd.read_csv(DATA_PATH.joinpath("Tweets.csv"))

city_list = data['city'].value_counts().index.tolist()

layout = html.Div([
    html.H1("Twitter Data", style={'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Label('Select year to check number of tweets'),
            dcc.Dropdown(id="slct_year1",
                         options=[{'label': year, 'value': year} for year in ['2020 & 2021', 2020, 2021]],
                         multi=False,
                         value='2020 & 2021',
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
                         options=[{'label': year, 'value': year} for year in ['2020 & 2021', 2020, 2021]],
                         multi=False,
                         value='2020 & 2021',
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
                         options=[{'label': year, 'value': year} for year in ['2020 & 2021', 2020, 2021]],
                         multi=False,
                         value='2020 & 2021',
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
                         options=[{'label': year, 'value': year} for year in ['2020 & 2021', 2020, 2021]],
                         multi=False,
                         value='2020 & 2021',
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
                             options=[{'label': y, 'value': y} for y in ['2020 & 2021', 2020, 2021]],
                             multi=False,
                             value='2020 & 2021',
                             style={'width': "100%"}
                             ),
                html.Div(id='output_container5', children=[])
            ],
                style={'width': '49%', 'display': 'inline-block'}),

            html.Div([
                html.Label('Select City'),
                dcc.Dropdown(id="slct_city1",
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
    ),
    html.Div([
        html.Div([

            html.Div([
                html.Label('Select Year'),
                dcc.Dropdown(id="slct_year6",
                             options=[{'label': y, 'value': y} for y in ['2020 & 2021', 2020, 2021]],
                             multi=False,
                             value='2020 & 2021',
                             style={'width': "100%"}
                             ),
                html.Div(id='output_container7', children=[])
            ],
                style={'width': '49%', 'display': 'inline-block'}),

            html.Div([
                html.Label('Select City'),
                dcc.Dropdown(id="slct_city2",
                             options=[{'label': c, 'value': c} for c in sorted(city_list)],
                             multi=False,
                             value='Kansas City,MO',
                             style={'width': "100%"}
                             ),
                html.Div(id='output_container8', children=[])
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
            dcc.Graph(id='tweets_emotion_month', figure={}),
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

    if slct_year1 == '2020 & 2021':
        df1 = (count.groupby(['city']).size()).reset_index()
        df1.rename(columns={0: 'NoOfTweets'}, inplace=True)

        # Plotly Express
        fig1 = px.bar(df1,
                      x="city",
                      y="NoOfTweets",
                      color='city',
                      labels=style_sheet.labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=style_sheet.cities,
                      text=df1['NoOfTweets']
                      )

        fig1.update_xaxes(title_text="")

        fig1.update_layout(
            title='<b>#Tweets from high minority population cities</b>',
            legend_title_text='City, State',
        )
        fig1.update_layout(style_sheet.update_layout2)
    else:
        df1 = count[count['Year'] == slct_year1]
        df1 = (df1.groupby(['Year', 'city']).size()).reset_index()
        df1.rename(columns={0: 'NoOfTweets'}, inplace=True)

        # Plotly Express
        fig1 = px.bar(df1,
                      x="city",
                      y="NoOfTweets",
                      color='city',
                      labels=style_sheet.labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=style_sheet.cities,
                      text=df1['NoOfTweets']
                      )

        fig1.update_xaxes(title_text="")

        fig1.update_layout(
            title='<b>#Tweets from high minority population cities in ' + str(slct_year1) + ' </b>',
            legend_title_text='City, State',
        )
        fig1.update_layout(style_sheet.update_layout2)

    senti = data.copy()

    print('Selected Year', slct_year2)
    container2 = "The year chosen by user was: {}".format(slct_year2)

    if slct_year2 == '2020 & 2021':
        df2 = (senti.groupby(['city', 'VADER_Sentiment']).size()).reset_index()
        df2.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig2 = px.bar(df2,
                      x="city",
                      y="NoOfTweets",
                      color="VADER_Sentiment",
                      # barmode='group',
                      labels=style_sheet.labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=style_sheet.sentiment,
                      category_orders=style_sheet.sentiment_order,
                      text=df2['NoOfTweets'],
                      )

        fig2.update_xaxes(title_text="")

        fig2.update_layout(
            title='<b>#Tweets from high minority population cities with VADER Sentiment</b>',
            legend_title_text='VADER Sentiment',
        )
        fig2.update_layout(style_sheet.update_layout2)

    else:
        df2 = senti[senti['Year'] == slct_year2]
        df2 = (df2.groupby(['Year', 'city', 'VADER_Sentiment']).size()).reset_index()
        df2.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig2 = px.bar(df2,
                      x="city",
                      y="NoOfTweets",
                      color="VADER_Sentiment",
                      labels=style_sheet.labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=style_sheet.sentiment,
                      category_orders=style_sheet.sentiment_order,
                      text=df2['NoOfTweets'],
                      )

        fig2.update_xaxes(title_text="")

        fig2.update_layout(
            title='<b>#Tweets from high minority population cities in ' + str(slct_year2) + ' with VADER Sentiment</b>',
            legend_title_text='VADER Sentiment',
        )
        fig2.update_layout(style_sheet.update_layout2)

    emotion = data.copy()

    print('Selected Year', slct_year3)
    container3 = "The year chosen by user was: {}".format(slct_year3)

    if slct_year3 == '2020 & 2021':
        df3 = (emotion.groupby(['city', 'BERT_Emotion']).size()).reset_index()
        df3.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig3 = px.bar(df3,
                      x="city",
                      y="NoOfTweets",
                      color="BERT_Emotion",
                      # barmode='group',
                      labels=style_sheet.labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=style_sheet.emotions,
                      category_orders=style_sheet.emotions_order,
                      text=df3['NoOfTweets'],
                      )

        fig3.update_xaxes(title_text="")

        fig3.update_layout(
            title='<b>#Tweets from high minority population cities with BERT Emotion</b>',
            legend_title_text='BERT Emotion',
        )
        fig3.update_layout(style_sheet.update_layout2)

    else:
        df3 = emotion[emotion['Year'] == slct_year3]
        df3 = (df3.groupby(['Year', 'city', 'BERT_Emotion']).size()).reset_index()
        df3.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig3 = px.bar(df3,
                      x="city",
                      y="NoOfTweets",
                      color="BERT_Emotion",
                      labels=style_sheet.labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=style_sheet.emotions,
                      category_orders=style_sheet.emotions_order,
                      text=df3['NoOfTweets'],
                      )

        fig3.update_xaxes(title_text="")

        fig3.update_layout(
            title='<b>#Tweets from high minority population cities in ' + str(slct_year3) + ' with BERT Emotion</b>',
            legend_title_text='BERT Emotion',
        )
        fig3.update_layout(style_sheet.update_layout2)

    topic = data.copy()

    print('Selected Year', slct_year4)
    container4 = "The year chosen by user was: {}".format(slct_year4)

    if slct_year4 == '2020 & 2021':
        df4 = (topic.groupby(['city', 'Dominant_Topic']).size()).reset_index()
        df4.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig4 = px.bar(df4,
                      x="city",
                      y="NoOfTweets",
                      color="Dominant_Topic",
                      labels=style_sheet.labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=style_sheet.sentiment,
                      category_orders=style_sheet.topic_order,
                      text=df4['NoOfTweets'],
                      )

        fig4.update_xaxes(title_text="")

        fig4.update_layout(
            title='<b>#Tweets from high minority population cities with Dominant Topic</b>',
            legend_title_text='Dominant Topic',
        )
        fig4.update_layout(style_sheet.update_layout2)

    else:
        df4 = topic[topic['Year'] == slct_year4]
        df4 = (df4.groupby(['Year', 'city', 'Dominant_Topic']).size()).reset_index()
        df4.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig4 = px.bar(df4,
                      x="city",
                      y="NoOfTweets",
                      color="Dominant_Topic",
                      # barmode='group',
                      labels=style_sheet.labels,
                      hover_name='city',
                      hover_data={
                          "city": False,
                          "NoOfTweets": True
                      },
                      color_discrete_map=style_sheet.sentiment,
                      category_orders=style_sheet.topic_order,
                      text=df4['NoOfTweets'],
                      )

        fig4.update_xaxes(title_text="")

        fig4.update_layout(
            title='<b>#Tweets from high minority population cities in ' + str(
                slct_year4) + ' with Dominant Topic</b>',
            legend_title_text='Dominant Topic',
        )
        fig4.update_layout(style_sheet.update_layout2)

    return container1, fig1, container2, fig2, container3, fig3, container4, fig4


@app.callback(
    [Output(component_id='output_container5', component_property='children'),
     Output(component_id='output_container6', component_property='children'),
     Output(component_id='tweets_count_month', component_property='figure')],
    [Input(component_id='slct_year5', component_property='value'),
     Input(component_id='slct_city1', component_property='value')]
)
def update_graph_2(slct_year5, slct_city1):
    dff1 = data.copy()
    print('Selected Year', slct_year5)
    container5 = "The year chosen by user was: {}".format(slct_year5)

    print('Selected City', slct_city1)
    container6 = "The year chosen by user was: {}".format(slct_city1)
    if slct_year5 == '2020 & 2021':
        df5 = dff1[dff1['city'] == slct_city1]
        df5['Time'] = df5['Month'].map(str) + '/' + df5['Year'].map(str)
        df5['Time'] = pd.to_datetime(df5['Time'])
        df5 = (df5.groupby(['Time']).size()).reset_index()
        df5.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig5 = px.bar(df5,
                      x="Time",
                      y="NoOfTweets",
                      labels=style_sheet.labels,
                      hover_data={
                          "Time": False,
                      },
                      text=df5['NoOfTweets']
                      )
        fig5.update_xaxes(dtick="M1",
                          )
        fig5.update_layout(
            title='<b>#Tweets from ' + slct_city1 + ' in ' + str(slct_year5) + '</b>',
            hoverlabel_align='right',
            xaxis=dict(tickmode='linear')
        )
        fig5.update_layout(style_sheet.update_layout1)

    else:
        df5 = dff1[(dff1['Year'] == slct_year5) & (dff1['city'] == slct_city1)]
        df5 = (df5.groupby(['Year', 'Month']).size()).reset_index()
        df5.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig5 = px.bar(df5,
                      x="Month",
                      y="NoOfTweets",
                      labels=style_sheet.labels,
                      hover_name='Month',
                      hover_data={
                          "Month": False,
                      },
                      text=df5['NoOfTweets']
                      )
        fig5.update_layout(
            title='<b>#Tweets from ' + slct_city1 + ' in ' + str(slct_year5) + '</b>',
            hoverlabel_align='right',
            xaxis=dict(tickmode='linear')
        )
        fig5.update_layout(style_sheet.update_layout1)

    return container5, container6, fig5


@app.callback(
    [Output(component_id='output_container7', component_property='children'),
     Output(component_id='output_container8', component_property='children'),
     Output(component_id='tweets_emotion_month', component_property='figure')],
    [Input(component_id='slct_year6', component_property='value'),
     Input(component_id='slct_city2', component_property='value')]
)
def update_graph_3(slct_year6, slct_city2):
    dff1 = data.copy()
    print('Selected Year', slct_year6)
    container7 = "The year chosen by user was: {}".format(slct_year6)

    print('Selected City', slct_city2)
    container8 = "The year chosen by user was: {}".format(slct_city2)
    if slct_year6 == '2020 & 2021':
        df5 = dff1[dff1['city'] == slct_city2]
        df5['Time'] = df5['Month'].map(str) + '/' + df5['Year'].map(str)
        df5['Time'] = pd.to_datetime(df5['Time'])
        df5 = (df5.groupby(['Time', 'BERT_Emotion']).size()).reset_index()
        df5.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig6 = px.bar(df5,
                      x="Time",
                      y="NoOfTweets",
                      color='BERT_Emotion',
                      color_discrete_map=style_sheet.emotions,
                      labels=style_sheet.labels,
                      hover_data={
                          "Time": False,
                      },
                      text=df5['NoOfTweets']
                      )
        fig6.update_xaxes(dtick="M1",
                          )
        fig6.update_layout(
            title='<b>#Tweets from ' + slct_city2 + ' in ' + str(slct_year6) + ' including BERT Emotions</b>',
            hoverlabel_align='right',
            legend_title_text='BERT Emotion',
            xaxis=dict(tickmode='linear')
        )
        fig6.update_layout(style_sheet.update_layout2)

    else:
        df5 = dff1[(dff1['Year'] == slct_year6) & (dff1['city'] == slct_city2)]
        df5 = (df5.groupby(['Year', 'Month', 'BERT_Emotion']).size()).reset_index()
        df5.rename(columns={0: 'NoOfTweets'}, inplace=True)

        fig6 = px.bar(df5,
                      x="Month",
                      y="NoOfTweets",
                      color='BERT_Emotion',
                      color_discrete_map=style_sheet.emotions,
                      labels=style_sheet.labels,
                      hover_name='Month',
                      hover_data={
                          "Month": False,
                      },
                      text=df5['NoOfTweets']
                      )
        fig6.update_layout(
            title='<b>#Tweets from ' + slct_city2 + ' in ' + str(slct_year6) + ' including BERT Emotions</b>',
            hoverlabel_align='right',
            legend_title_text='BERT Emotion',
            xaxis=dict(tickmode='linear')
        )
        fig6.update_layout(style_sheet.update_layout1)

    return container7, container8, fig6
