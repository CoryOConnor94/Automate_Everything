import requests

API_KEY = ''


def get_news_by_topic(topic, from_date, to_date, language='en', api_key=API_KEY):
    url = (f'https://newsapi.org/v2/everything?q={topic}&'
           f'from={from_date}&to={to_date}sortBy=popularity&language={language}&apiKey={API_KEY}')

    response = requests.get(url)
    content = response.json()
    articles = content['articles']
    results = []

    for article in articles:
        results.append(f"TITLE\n', {article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results


def get_news_by_country(country, api_key=API_KEY):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'

    response = requests.get(url)
    content = response.json()
    articles = content['articles']
    results = []

    for article in articles:
        results.append(f"TITLE\n', {article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results


# print(get_news_by_topic(topic='space', from_date='2024-12-20', to_date='2024-01-12', api_key=API_KEY))
print(get_news_by_country(country='US', api_key=API_KEY))
