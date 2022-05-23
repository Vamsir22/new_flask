from newsapi import NewsApiClient
# Init
newsapi = NewsApiClient(api_key='79586381669048ab8d983e3112db287e')


# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='india',
                                          language='en',
                                          country='in')


data = top_headlines['articles']

for each in data:
    print(each['title'])
