from flask_wtf import FlaskForm
from wtforms import widgets, StringField, SelectField, SubmitField, SelectMultipleField, BooleanField, RadioField, FloatField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import ListWidget, CheckboxInput


class QuestionOne(FlaskForm):
    yes = SubmitField('Continue')
    no = SubmitField('Home Page')

class QuestionTwo(FlaskForm):

    #makes sure the input is a float field and gives an error message if not
    def check_input(self, field):
        try:
            float(field.data)
        except:
            raise ValidationError("Value must be a float or integer")

    #makes sure the units for the height is correct
    def check_h_choice(self, field):
        h_choice = field.data
        while h_choice.upper() != "CM" and h_choice.upper() != "FEET":
            raise ValidationError("Value must be either cm or feet")

    #makes sure the units for the weight is correct
    def check_w_choice(self, field):
        w_choice = field.data
        while w_choice.upper() != "KG" and w_choice.upper() != "LBS":
            raise ValidationError("Value must be either kg or lbs")

    # declaration and validation for each input field
    height = StringField(validators=[DataRequired(), check_input])
    h_units = StringField(validators=[DataRequired(), check_h_choice])
    weight = StringField(validators=[DataRequired(), check_input])
    w_units = StringField(validators=[DataRequired(), check_w_choice])
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
    # makes sure the input is a float field and gives an error message if not
    def check_input(self, field):
        try:
            int(field.data)
        except:
            raise ValidationError("Value must be an integer")

    age = StringField(validators=[DataRequired(), check_input])
    submit = SubmitField('Submit')