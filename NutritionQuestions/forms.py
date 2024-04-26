from flask_wtf import FlaskForm
from wtforms import SubmitField


class QuestionOne(FlaskForm):
    yes = SubmitField('Continue')
    no = SubmitField('Home Page')

class QuestionTwo(FlaskForm):
    submit = SubmitField('Submit')

class QuestionThree(FlaskForm):
    submit = SubmitField("Submit")


