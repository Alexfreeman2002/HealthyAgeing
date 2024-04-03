from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import ListWidget, CheckboxInput


class QuestionOne(FlaskForm):
    yes = SubmitField('Yes')
    no = SubmitField('No')

class QuestionTwo(FlaskForm):
    option1 = BooleanField('Option 1')
    option2 = BooleanField('Option 2')
    option3 = BooleanField('Option 3')
    submit = SubmitField('Submit')

class QuestionThree(FlaskForm):
    submit = SubmitField('Submit')