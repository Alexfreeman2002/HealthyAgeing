from flask import render_template, Blueprint, redirect, url_for, request
from FitnessQuestions.forms import QuestionOne, QuestionTwo, QuestionThree

fitness_blueprint = Blueprint('fitness', __name__, template_folder='templates/features/fitnessQs')

@fitness_blueprint.route('/fitness', methods=['get','post'])
def fitness_plan():
    route = []
    form1 = QuestionOne()
    if form1.yes.data:
        route.append("y")
        return redirect("/two")
    if form1.no.data:
        route.append("n")
        return render_template('main/index.html')

    return render_template("features/fitnessQs/question1.html", form1=form1)

@fitness_blueprint.route('/two', methods=['get','post'])
def Q2():
    form2 = QuestionTwo()
    if form2.validate_on_submit():
        selected_options = []
        if form2.option1.data:
            selected_options.append('Option 1')
            print("1")
        if form2.option2.data:
            selected_options.append('Option 2')
            print("2")
        if form2.option3.data:
            selected_options.append('Option 3')
            print("3")
        return redirect("/three")
    return render_template("features/fitnessQs/question2.html", form2=form2)

@fitness_blueprint.route('/three', methods=['get','post'])
def Q3():
    form = QuestionThree()
    if request.method == 'POST':
        value = request.form['sliderValue']
    return render_template("features/fitnessQs/question3.html", form=form)



def final_plan():
    """
    form = QuestionOne
    if form.validate_on_submit():
        if form.Yes.data:
    """
    pass