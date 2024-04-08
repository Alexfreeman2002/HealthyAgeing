from flask_wtf import FlaskForm
from wtforms import widgets, StringField, SelectField, SubmitField, SelectMultipleField, BooleanField, RadioField, FloatField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import ListWidget, CheckboxInput


class QuestionOne(FlaskForm):
    yes = SubmitField('Continue')
    no = SubmitField('Home Page')

class QuestionTwo(FlaskForm):
    submit = SubmitField('Submit')


class QuestionThree(FlaskForm):
    submit = SubmitField("Submit")


