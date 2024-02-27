import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_talisman import Talisman

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO') == 'true'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'true'

# Initialize database
db = SQLAlchemy(app)

talisman = Talisman(app)

@app.route('/')
def index():
    """Home page view"""
    return render_template('main/index.html')

@app.errorhandler(400)
def internal_error(error):
    return render_template('400.html'), 400

@app.errorhandler(403)
def internal_error(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.errorhandler(503)
def internal_error(error):
    return render_template('503.html'), 503

if __name__ == "__main__":
    app.run()