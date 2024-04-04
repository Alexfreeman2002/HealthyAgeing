from flask_wtf import FlaskForm
from wtforms import widgets, StringField, SelectField, SubmitField, SelectMultipleField, BooleanField, RadioField, FloatField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import ListWidget, CheckboxInput


class QuestionOne(FlaskForm):
    yes = SubmitField('Continue')
    no = SubmitField('Home Page')

class QuestionTwo(FlaskForm):
    submit = SubmitField('Submit')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class QuestionThree(FlaskForm):
    submit = SubmitField("Submit")

class QuestionFour(FlaskForm):
    options = RadioField('Options', choices=[('lose', 'Lose Weight'),
                                             ('gain', 'Gain Weight'),
                                             ('maintain', 'Maintain Weight')])
    submit = SubmitField('Submit')

class QuestionFive(FlaskForm):
    small = SubmitField('Small')
    medium = SubmitField('Medium')
    large = SubmitField('Large')

class QuestionSix(FlaskForm):
    submit = SubmitField('Submit')

class QuestionSeven(FlaskForm):
    def check_input(self, field):
        try:
            float(field.data)
        except:
            raise ValidationError("Value must be a number")

        if float(field.data) > 5:
            raise ValidationError("Value must be between 0 and 5")
        elif float(field.data) < 0:
            raise ValidationError("Value must be between 0 and 5")

        if (float(field.data) * 10) % 1 != 0:
            raise ValidationError("Please only enter up to 1 decimal point")


    hours = StringField(validators=[DataRequired(), check_input])
    submit = SubmitField('Submit')