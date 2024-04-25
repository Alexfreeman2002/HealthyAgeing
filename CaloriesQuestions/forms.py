"""
Calories Questions Forms

This file defines Flask forms for each question within the calorie calculator
"""

from flask_wtf import FlaskForm
from wtforms import widgets, StringField, SelectField, SubmitField, SelectMultipleField, BooleanField, RadioField, FloatField
from wtforms.validators import DataRequired, ValidationError
import re

class QuestionOne(FlaskForm):
    yes = SubmitField('Continue')
    no = SubmitField('Home Page')

class QuestionTwo(FlaskForm):


    #makes sure the input is a float field and within a range, gives an error message if not
    def check_height_input(self, field):
        try:
            float(field.data)
        except:
            raise ValidationError("Value must be a float or integer")

        if float(field.data) > 275:
            raise ValidationError("Value is too high.")
        elif float(field.data) < 0:
            raise ValidationError("Please enter a positive number")

    #makes sure the input is a float field and within a range, gives an error message if not
    def check_weight_input(self, field):
        try:
            float(field.data)
        except:
            raise ValidationError("You have entered a value must that is too large or it isn't a number")

        if float(field.data) > 1500:
            raise ValidationError("Value is too high.")
        elif float(field.data) < 0:
            raise ValidationError("Please enter a positive number")


    # declaration and validation for each input field
    height = StringField(validators=[DataRequired(), check_height_input])
    hoptions = RadioField('Options', choices=[('cm','Centimeters'),('feet', 'Feet')], default='cm')
    weight = StringField(validators=[DataRequired(), check_weight_input])
    woptions = RadioField('Options', choices=[('kg', 'Kilograms'),('lbs', 'Pounds')], default='kg')
    submit = SubmitField('Submit')

class QuestionThree(FlaskForm):
    options = RadioField('Options', choices=[('1.2', 'Little or no exercise'),
                                             ('1.375', 'Light activity (1-3 days per week), or a moderately active job such as beauty therapist and no exercise'),
                                             ('1.55', 'Moderate exercise (3-5 days per week), or a moderately active job with light exercise, or heavy exercise and an inactive job'),
                                             ('1.725', 'Heavy exercise (5 days a week training) or moderately active job such as policeman and moderate exercise'),
                                             ('1.9','Very heavy exercise (twice per day, extra heavy workouts) or a very active job like Personal Trainer or Factory Worker who also exercises a lot')])
    submit = SubmitField('Submit')


class QuestionFour(FlaskForm):
    options = RadioField('Options', choices=[('m', 'Male'),
                                             ('f', 'Female'),
                                             ('none', 'Prefer not to say'),
                                             ('o', 'Other')])
    submit = SubmitField('Submit')

class QuestionFive(FlaskForm):
    #makes sure the input is a float field and within a range, gives an error message if not
    def check_input(self, field):
        try:
            int(field.data)
        except:
            raise ValidationError("Value must be an integer")

        if float(field.data) > 125:
            raise ValidationError("Value is too high.")
        elif float(field.data) < 0:
            raise ValidationError("Please enter a positive number")

    age = StringField(validators=[DataRequired(), check_input], render_kw={"placeholder": "Enter your age"})
    submit = SubmitField('Submit')