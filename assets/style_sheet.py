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

update_layout1 = dict(
    title_x=0.5,
    font_size=13,
    font_family='Rockwell',
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
    font_family='Rockwell',
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
