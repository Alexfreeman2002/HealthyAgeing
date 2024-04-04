from flask import render_template, Blueprint, redirect, url_for, request
from NutritionQuestions.forms import QuestionOne, QuestionTwo, QuestionThree, QuestionFour, QuestionFive, QuestionSix, QuestionSeven

meal_blueprint = Blueprint('meal', __name__, template_folder='templates/features/nutritionQs')

route = []
diet_req = []

@meal_blueprint.route('/meal', methods=['get','post'])
def meal_plan():
    route.clear()
    form = QuestionOne()
    if form.yes.data:
        return redirect("/mtwo")
    if form.no.data:
        return redirect("/")

    return render_template("features/nutritionQs/question1.html", form=form)

@meal_blueprint.route('/mtwo', methods=['get','post'])
def Q2():
    form = QuestionTwo()
    if request.method == 'POST':
        value = request.form['sliderValue']
        route.insert(0, value)
        return redirect("/mthree")
    return render_template("features/nutritionQs/question2.html", form=form)

@meal_blueprint.route('/mthree', methods=['get','post'])
def Q3():
    form = QuestionThree()
    diet_req.clear()
    if request.method == 'POST':
        diet_req.append(request.form.getlist("fr"))
        print(diet_req)
        return redirect("/mfour")
    return render_template("features/nutritionQs/question3.html", form=form)

@meal_blueprint.route('/mfour', methods=['get','post'])
def Q4():
    form = QuestionFour()
    if form.validate_on_submit():
        route.insert(1, form.options.data)
        return redirect("/mfive")
    return render_template("features/nutritionQs/question4.html", form=form)

@meal_blueprint.route('/mfive', methods=['get','post'])
def Q5():
    form = QuestionFive()
    if form.validate_on_submit():
        if form.small.data:
            route.insert(2, "s")
        if form.medium.data:
            route.insert(2, "m")
        if form.large.data:
            route.insert(2, "l")
        return redirect("/msix")

    return render_template("features/nutritionQs/question5.html", form=form)


@meal_blueprint.route('/msix', methods=['get', 'post'])
def Q6():
    form = QuestionSix()
    if request.method == 'POST':
        value = request.form['sliderValue']
        route.insert(3, value)
        return redirect("/mseven")

    return render_template("features/nutritionQs/question6.html", form=form)

@meal_blueprint.route('/mseven', methods=['get', 'post'])
def Q7():
    form = QuestionSeven()
    if form.validate_on_submit():
        route.insert(4, form.hours.data)
        return redirect("/")

    return render_template("features/nutritionQs/question7.html", form=form)


def final_plan():
    """
    form = QuestionOne
    if form.validate_on_submit():
        if form.Yes.data:
    """
    pass