from flask import render_template
import feedparser
from flask import Blueprint
from datetime import datetime

news_blueprint = Blueprint('news', __name__, template_folder='templates/features')


@news_blueprint.route('/features/news', methods=['get'])
def news():
    feed = feedparser.parse('https://www.england.nhs.uk/feed/')
    articles = feed.entries[:10]

    for article in articles:
        # Parse the date string
        published_datetime = datetime.strptime(article.published, '%a, %d %b %Y %H:%M:%S %z')
        # Format the date string without the timezone offset
        article.published = published_datetime.strftime('%a, %d %b %Y %H:%M:%S')

    return render_template('features/news.html', articles=articles)
