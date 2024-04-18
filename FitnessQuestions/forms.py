"""
Fitness Questions Forms

This file defines Flask forms for each question within the fitness plan creator
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, ValidationError


class QuestionOne(FlaskForm):
    yes = SubmitField('Continue')
    no = SubmitField('Home Page')

class QuestionTwo(FlaskForm):

    def check_input(self, field):
        try:
            float(field.data)
        except:
            raise ValidationError("Value must be a number")

        if float(field.data) > 50:
            raise ValidationError("Value must be between 0 and 50")
        elif float(field.data) < 0:
            raise ValidationError("Value must be between 0 and 50")

        if (float(field.data) * 10) % 1 != 0:
            raise ValidationError("Please only enter up to 1 decimal point")


    hours = StringField(validators=[DataRequired(), check_input], render_kw={"placeholder": "Enter hours"})
    submit = SubmitField('Submit')

class QuestionThree(FlaskForm):
    options = RadioField('Options', choices=[('lose', 'Lose Weight'),
                                             ('gain', 'Gain Weight'),
                                             ('maintain', 'Maintain Weight')])
    submit = SubmitField('Submit')

class QuestionFour(FlaskForm):
    submit = SubmitField('Submit')

class QuestionFive(FlaskForm):
    gym = SubmitField('Gym')
    home = SubmitField('Home')

class QuestionSix(FlaskForm):
    yes = SubmitField('Yes')
    no = SubmitField('No')
    unsure = SubmitField('Not Sure')