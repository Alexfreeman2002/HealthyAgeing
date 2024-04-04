from flask import render_template, Blueprint, redirect, url_for, request
from FitnessQuestions.forms import QuestionOne, QuestionTwo, QuestionThree, QuestionFour, QuestionFive, QuestionSix

fitness_blueprint = Blueprint('fitness', __name__, template_folder='templates/features/fitnessQs')

route = []

@fitness_blueprint.route('/fitness', methods=['get','post'])
def fitness_plan():
    route.clear()
    form1 = QuestionOne()
    if form1.yes.data:
        route.append("y")
        return redirect("/two")
    if form1.no.data:
        return render_template('main/index.html')

    return render_template("features/fitnessQs/question1.html", form1=form1)

@fitness_blueprint.route('/two', methods=['get','post'])
def Q2():
    form = QuestionTwo()
    if form.validate_on_submit():
        route.append(form.hours.data)
        return redirect("/three")
    return render_template("features/fitnessQs/question2.html", form=form)

@fitness_blueprint.route('/three', methods=['get','post'])
def Q3():
    form2 = QuestionThree()
    if form2.validate_on_submit():
        route.append(form2.options.data)
        return redirect("/four")
    return render_template("features/fitnessQs/question3.html", form2=form2)

@fitness_blueprint.route('/four', methods=['get','post'])
def Q4():
    form = QuestionFour()
    if request.method == 'POST':
        value = request.form['sliderValue']
        return redirect("/five")
    return render_template("features/fitnessQs/question4.html", form=form)

@fitness_blueprint.route('/five', methods=['get','post'])
def Q5():
    form = QuestionFive()
    if form.validate_on_submit():
        if form.gym.data:
            route.append("gym")
        if form.home.data:
            route.append("home")
        return redirect("/six")

    return render_template("features/fitnessQs/question5.html", form=form)


@fitness_blueprint.route('/six', methods=['get', 'post'])
def Q6():
    form = QuestionSix()
    if form.yes.data:
        route.append("frail")
    if form.no.data:
        route.append("notfrail")
    if form.no.data:
        route.append("unsure")

    return render_template("features/fitnessQs/question6.html", form=form)
#create code to check and remove values in list

def final_plan():
    """
    form = QuestionOne
    if form.validate_on_submit():
        if form.Yes.data:
    """
    pass