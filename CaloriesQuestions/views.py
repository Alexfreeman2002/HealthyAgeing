from flask import render_template, Blueprint, redirect, url_for, request
from CaloriesQuestions.forms import QuestionOne, QuestionTwo, QuestionThree, QuestionFour, QuestionFive

calorie_blueprint = Blueprint('calorie', __name__, template_folder='templates/features/calories')

values = []
@calorie_blueprint.route('/calorie', methods=['get','post'])
def calories():
    form = QuestionOne()
    if form.yes.data:
        return redirect("/ctwo")
    if form.no.data:
        return redirect("/")

    return render_template("features/calories/question1.html", form=form, alert_message=request.args.get('alert'))

def height_inch(Height, choice):
    if choice == "cm":
        #returns height in inches
        return Height/2.54
    elif choice == "feet":
        #returns height in inches
        return Height*12


def weight_lbs(Weight, choice):
    if choice == "kg":
        # returns weight in lbs
        return Weight*2.205
    elif choice == "lbs":
        # returns weight in lbs
        return Weight

@calorie_blueprint.route('/ctwo', methods=['get','post'])
def Q2():
    values.clear()
    form = QuestionTwo()
    if form.validate_on_submit():
        # gets the units for the height and weight from the form
        h_choice = form.hoptions.data
        w_choice = form.woptions.data

        # gets the value for the height and weight from the form, making them a float type
        H = float(form.height.data)
        W = float(form.weight.data)

        weight = weight_lbs(W, w_choice)
        if h_choice == 'feet':
            inches = float(form.inches.data)
            height = height_inch(H, h_choice) + inches
        else:
            height = height_inch(H, h_choice)
        # adds the values to the list
        values.insert(0,weight)
        values.insert(1,height)
        return redirect('cthree')


    return render_template("features/calories/question2.html", form=form)

@calorie_blueprint.route('/cthree', methods=['get','post'])
def Q3():
    form = QuestionThree()
    if form.validate_on_submit():
        # adds activity level to list
        values.insert(2, form.options.data)
        return redirect("/cfour")
    return render_template("features/calories/question3.html", form=form)

@calorie_blueprint.route('/cfour', methods=['get','post'])
def Q4():
    form = QuestionFour()
    if form.validate_on_submit():
        #adds gender to list
        values.insert(3, form.options.data)
        return redirect("/cfive")
    return render_template("features/calories/question4.html", form=form)

@calorie_blueprint.route('/cfive', methods=['get','post'])
def Q5():
    form = QuestionFive()
    if form.validate_on_submit():
        values.insert(4, form.age.data)
        return redirect("/cresult")
    return render_template("features/calories/question5.html", form=form)

def calulate_TDEE(weight, height, age, gender, activity):
    if gender == 'm':
        BMR =  (66 + 6.3*float(weight) + 12.9*float(height) - 6.8*float(age))
    elif gender == 'f':
        BMR = (655 + 4.3 * float(weight) + 4.7 * float(height) - 4.7 * float(age))
    else:
        m = (66 + 6.3 * float(weight) + 12.9 * float(height) - 6.8 * float(age))
        f = (655 + 4.3 * float(weight) + 4.7 * float(height) - 4.7 * float(age))
        BMR = (m+f)/2
    cals = BMR * float(activity)
    deficit = round(cals) * 0.8
    gain = round(cals) * 1.2
    return round(cals), round(deficit), round(gain)

@calorie_blueprint.route('/cresult', methods=['get', 'post'])
def calorie_result():
    if len(values) != 5:
        return redirect(url_for('calorie.calories', alert='Please press ok to restart the set of questions'))
    cals, deficit, gain = calulate_TDEE(values[0], values[1], values[4], values[3], values[2])
    return render_template("features/calories/result.html", calories=cals, deficit=deficit, gain=gain)

