from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, SelectMultipleField, BooleanField, RadioField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import ListWidget, CheckboxInput


class QuestionOne(FlaskForm):
    yes = SubmitField('Continue')
    no = SubmitField('Home Page')

class QuestionTwo(FlaskForm):

    def check_input(self, field):
        try:
            float(field.data)
        except:
            raise ValidationError("Value must be a float or integer")

    hours = StringField(validators=[DataRequired(), check_input])
    submit = SubmitField('Submit')

class QuestionThree(FlaskForm):
    options = RadioField('Options', choices=[('lose', 'Lose Weight'),
                                             ('Gain', 'Gain Weight'),
                                             ('Maintain', 'Maintain Weight')])
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



    """option1 = BooleanField('Option 1')
    option2 = BooleanField('Option 2')
    option3 = BooleanField('Option 3')
    submit = SubmitField('Submit')
    <form class="form" method="post">
                {{ form2.hidden_tag() }}
                <div>
                    {{ form2.option1.label }}
                    {{ form2.option1 }}
                </div>
                <div>
                    {{ form2.option2.label }}
                    {{ form2.option2 }}
                </div>
                <div>
                    {{ form2.option3.label }}
                    {{ form2.option3 }}
                </div>
                <div>
                    {{ form2.submit }}
                </div>
            </form>"""