import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_talisman import Talisman
import feedparser


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO') == 'true'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'true'

# Initialize database
db = SQLAlchemy(app)

# Content Security Policy (CSP) configuration
csp = {
    'script-src': [
        '\'self\'',
        '\'unsafe-inline\'',
        'https://www.england.nhs.uk/feed/',
        'https://www.google.com/recaptcha/',
        'https://www.gstatic.com/recaptcha/'
    ]
}

talisman = Talisman(app, content_security_policy=csp)

@app.route('/')
def index():
    """Home page view"""

    feed = feedparser.parse('https://www.england.nhs.uk/feed/')
    articles = feed.entries[:2]

    return render_template('main/index.html', articles=articles)

@app.route('/health')
def health():
    """Health page view"""
    return render_template('features/fitness_advice.html')


# BLUEPRINTS
from News.views import news_blueprint
from SearchDiseases.views import search_blueprint
from FitnessQuestions.views import fitness_blueprint
from NutritionQuestions.views import meal_blueprint

# Register blueprints
app.register_blueprint(news_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(fitness_blueprint)
app.register_blueprint(meal_blueprint)

# Error handlers
@app.errorhandler(400)
def bad_request_error(error):
    """Error handler for 400 - Bad Request"""
    return render_template('400.html'), 400


@app.errorhandler(403)
def forbidden_error(error):
    """Error handler for 403 - Forbidden"""
    return render_template('403.html'), 403


@app.errorhandler(404)
def not_found_error(error):
    """Error handler for 404 - Not Found"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    """Error handler for 500 - Internal Server Error"""
    return render_template('500.html'), 500


@app.errorhandler(503)
def service_unavailable_error(error):
    """Error handler for 503 - Service Unavailable"""
    return render_template('503.html'), 503


if __name__ == "__main__":
    app.run()