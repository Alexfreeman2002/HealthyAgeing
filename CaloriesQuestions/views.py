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

    return render_template("features/calories/question1.html", form=form)

def height_inch(Height, choice):
    #makes their input uppercase
    choice = choice.upper()
    if choice == "CM":
        #returns height in inches
        return Height/2.54
    elif choice == "FEET":
        #returns height in inches
        return Height*12


def weight_lbs(Weight, choice):
    choice = choice.upper()
    if choice == "KG":
        # returns weight in lbs
        return Weight*2.205
    elif choice == "LBS":
        # returns weight in lbs
        return Weight

@calorie_blueprint.route('/ctwo', methods=['get','post'])
def Q2():
    values.clear()
    form = QuestionTwo()
    if form.validate_on_submit():
        # gets the units for the height and weight from the form
        h_choice = form.h_units.data
        w_choice = form.w_units.data
        # gets the value for the height and weight from the form, making them a float type
        H = float(form.height.data)
        W = float(form.weight.data)
        # calls the functions to return the height in metres and weight in kg so this can be saved in the database
        weight = weight_lbs(W, w_choice)
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
        values.insert(2, form.options.data)
        return redirect("/cfour")
    return render_template("features/calories/question3.html", form=form)

@calorie_blueprint.route('/cfour', methods=['get','post'])
def Q4():
    form = QuestionFour()
    if form.validate_on_submit():
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

@calorie_blueprint.route('/cresult', methods=['get', 'post'])
def calorie_result():
    if len(values) != 5:
        return redirect('/calorie')
    if values[3] == 'm':
        BMR =  (66 + float(6.3*float(values[0])) + float(12.9*float(values[1])) - float(6.8 * float(values[4])))
        cals = BMR * float(values[2])
    elif values[3] == 'f':
        BMR = (655 + float(4.3 * float(values[0])) + float(4.7 * float(values[1])) - float(4.7 * float(values[4])))
        cals = BMR * float(values[2])
    else:
        m = (66 + float(6.3 * float(values[0])) + float(12.9 * float(values[1])) - float(6.8 * float(values[4])))
        f = (655 + float(4.3 * float(values[0])) + float(4.7 * float(values[1])) - float(4.7 * float(values[4])))
        BMR = (m+f)/2
        cals = BMR * float(values[2])
    return render_template("features/calories/result.html", calories=round(cals))