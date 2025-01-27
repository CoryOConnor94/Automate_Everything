import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

text = 'Hey, what a beautiful day!, How amazing is this'
text_two = 'This weather is not so good'
sentiment = analyzer.polarity_scores(text_two)
print(sentiment)

if sentiment['compound'] > 0:
    print('This text is positive')
else:
    print('This text is negative')