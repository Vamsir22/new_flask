from flask import Flask, render_template
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='79586381669048ab8d983e3112db287e')


app = Flask(__name__)
# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='india',
                                          language='en',
                                          country='in')
data = top_headlines['articles']


@app.route('/')
def home():
    return render_template('index.html', news=data)


if __name__ == "__main__":
    app.run(debug=True)
