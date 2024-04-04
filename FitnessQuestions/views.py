from flask import render_template, Blueprint, redirect, url_for, request, flash
from FitnessQuestions.forms import QuestionOne, QuestionTwo, QuestionThree, QuestionFour, QuestionFive, QuestionSix

fitness_blueprint = Blueprint('fitness', __name__, template_folder='templates/features/fitnessQs')

route = []

@fitness_blueprint.route('/fitness', methods=['get','post'])
def fitness_plan():
    route.clear()
    form = QuestionOne()
    if form.yes.data:
        return redirect("/two")
    if form.no.data:
        return redirect("/")

    return render_template("features/fitnessQs/question1.html", form=form)

@fitness_blueprint.route('/two', methods=['get','post'])
def Q2():
    form = QuestionTwo()
    if form.validate_on_submit():
        route.insert(0, form.hours.data)
        return redirect("/three")
    return render_template("features/fitnessQs/question2.html", form=form)

@fitness_blueprint.route('/three', methods=['get','post'])
def Q3():
    form = QuestionThree()
    if form.validate_on_submit():
        route.insert(1, form.options.data)
        return redirect("/four")
    return render_template("features/fitnessQs/question3.html", form=form)

@fitness_blueprint.route('/four', methods=['get','post'])
def Q4():
    form = QuestionFour()
    if request.method == 'POST':
        value = request.form['sliderValue']
        route.insert(2, value)
        return redirect("/five")
    return render_template("features/fitnessQs/question4.html", form=form)

@fitness_blueprint.route('/five', methods=['get','post'])
def Q5():
    form = QuestionFive()
    if form.validate_on_submit():
        if form.gym.data:
            route.insert(3, "gym")
        if form.home.data:
            route.insert(3, "home")
        return redirect("/six")

    return render_template("features/fitnessQs/question5.html", form=form)


@fitness_blueprint.route('/six', methods=['get', 'post'])
def Q6():
    form = QuestionSix()
    if request.method == 'POST':
        if form.yes.data:
            route.insert(4, "frail")
        if form.no.data:
            route.insert(4, "notfrail")
        if form.unsure.data:
            route.insert(4, "unsure")
        print(len(route))
        return redirect("/")

    return render_template("features/fitnessQs/question6.html", form=form)


@fitness_blueprint.route('/six', methods=['get', 'post'])
def final_plan():
    form=QuestionOne
    if len(route) != 4:
        return render_template("features/fitnessQs/question1.html", form=form)
    else:

    return render_template("features/fitnessQs/result.html")