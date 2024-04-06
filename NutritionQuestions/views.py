from flask import render_template, Blueprint, redirect, url_for, request
from NutritionQuestions.forms import QuestionOne, QuestionTwo, QuestionThree, QuestionFour, QuestionFive, QuestionSix, QuestionSeven

meal_blueprint = Blueprint('meal', __name__, template_folder='templates/features/nutritionQs')

choices = []

@meal_blueprint.route('/meal', methods=['get','post'])
def meal_plan():
    form = QuestionOne()
    if form.yes.data:
        return redirect("/mtwo")
    if form.no.data:
        return redirect("/")

    return render_template("features/nutritionQs/question1.html", form=form)

@meal_blueprint.route('/mtwo', methods=['get','post'])
def Q2():
    form = QuestionThree()
    choices.clear()
    if request.method == 'POST':
        choices.append(request.form.getlist("fr"))
        return redirect("/mthree")
    return render_template("features/nutritionQs/question2.html", form=form)

@meal_blueprint.route('/mthree', methods=['get','post'])
def Q3():
    form = QuestionTwo()
    if request.method == 'POST':
        value = request.form['sliderValue']
        choices.insert(0, value)
        return redirect("/mresult")
    return render_template("features/nutritionQs/question3.html", form=form)

@meal_blueprint.route('/mresult', methods=['get', 'post'])
def meal_result():
    if len(choices) != 2:
        return redirect("/meal")
    if choices[0] <= "3":
        pass
    else:
        pass
    return render_template("features/nutritionQs/result.html")