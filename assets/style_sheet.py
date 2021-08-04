# colors
tweets_color = {
    'NoOfTweets': '#83c5be'
}
cities_color = {
    'Kansas City,MO': '#264653',
    'Long Beach,CA': '#2a9d8f',
    'Omaha,NE': '#f4a261',
    'Raleigh,NC': '#e76f51'
}
sentiment_color = {
    'positive': '#2a9d8f',
    'negative': '#e76f51',
    'neutral': '#f4a261'
}
emotions_color = {
    'anger': '#e76f51',
    'joy': '#2a9d8f',
    'optimism': '#f4a261',
    'sadness': '#264653'
}
topics_color = {'Topic 1': '#e76f51',
                'Topic 2': '#2a9d8f',
                'Topic 3': '#f4a261',
                'Topic 4': '#264653'
                }

# labels
labels = {
    "city": "City, State",
    'VADER_Sentiment': 'VADER Sentiment',
    'BERT_Emotion': 'BERT Emotion',
    "NoOfTweets": "#Tweets",
    'positive': 'Positive',
    'negative': 'Negative',
    'neutral': 'Neutral'
}

# order
emotions_order = {
    "BERT_Emotion": ["anger", 'joy', 'optimism', 'sadness']
}

sentiment_order = {
    "VADER_Sentiment": ["positive", 'neutral', "negative"]
}
topic_order = {
    "Dominant_Topic": ["Topic 1", 'Topic 2', "Topic 3", 'Topic 4']
}

# config
config = {
    'displayModeBar': False
}

# layouts
update_layout1 = dict(
    title_x=0.5,
    font_size=13,
    font_family='sans-serif',
    margin=dict(l=0, r=0, b=0),
    hoverlabel=dict(
        font_size=16,
        font_family="Rockwell"),
    autotypenumbers="strict",
    template="simple_white",
    hoverlabel_align='right',
    xaxis=dict(tickmode='linear'),
)
update_layout2 = dict(
    title_x=0.5,
    font_size=13,
    font_family='sans-serif',
    margin=dict(l=0, r=0, b=0),
    hoverlabel=dict(
        font_size=16,
        font_family="Rockwell"),
    autotypenumbers="strict",
    template="simple_white",
    hoverlabel_align='right',
    legend=dict(
        orientation="h",
    ),
)
