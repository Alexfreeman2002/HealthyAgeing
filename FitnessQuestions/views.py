from flask import render_template, Blueprint, redirect, request, url_for
from FitnessQuestions.forms import QuestionOne, QuestionTwo, QuestionThree, QuestionFour, QuestionFive, QuestionSix
import csv

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

    return render_template("features/fitnessQs/question1.html", form=form, alert_message=request.args.get('alert'))

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
        return redirect("/result")

    return render_template("features/fitnessQs/question6.html", form=form)

def read_csv(file_name):
# Open the CSV file
    with open(file_name, newline='') as csvfile:

        # Create a CSV reader
        csvreader = csv.reader(csvfile)

        # Initialize a list to store arrays for each row
        plan = []

        # Iterate over each row in the CSV file
        for row in csvreader:
            # Append the row to the arrays list
            plan.append(row)

        # ignore the first two values of each line in the csv file
        instructions = [subarray[2:] for subarray in plan]

    return plan, instructions

@fitness_blueprint.route('/result', methods=['get', 'post'])
def result():

    if len(route) != 5:
        return redirect(url_for('fitness.fitness_plan', alert='Please press ok to restart the set of questions'))
    if route[3] == 'home':
        if route[4] == 'frail':
            file = 'static/csv/beginner/h_beg.csv'
            plan, instructions = read_csv(file)
        if route[1] == 'lose':
            #more cardio
            if int(route[2]) <= 3:
                #beginner
                file = 'static/csv/beginner/h_c_beg.csv'
                plan, instructions = read_csv(file)
            elif int(route[2]) < 8:
                #intermediate
                file = 'static/csv/intermediate/h_c_int.csv'
                plan, instructions = read_csv(file)
            if int(route[2]) > 7:
                #advanced
                file = 'static/csv/advanced/h_c_adv.csv'
                plan, instructions = read_csv(file)
        elif route[1] == 'gain':
            #less cardio
            if int(route[2]) <= 3:
                #beginner
                file = 'static/csv/beginner/h_nc_beg.csv'
                plan, instructions = read_csv(file)
            elif int(route[2]) < 8:
                #intermediate
                file = 'static/csv/intermediate/h_nc_int.csv'
                plan, instructions = read_csv(file)
            if int(route[2]) > 7:
                #advanced
                file = 'static/csv/advanced/h_nc_adv.csv'
                plan, instructions = read_csv(file)
        else:
            #average cardio
            if int(route[2]) <= 3:
                #beginner
                file = 'static/csv/beginner/h_beg.csv'
                plan, instructions = read_csv(file)
            elif int(route[2]) < 8:
                #intermediate
                file = 'static/csv/intermediate/h_int.csv'
                plan, instructions = read_csv(file)
            if int(route[2]) > 7:
                #advanced
                file = 'static/csv/advanced/h_adv.csv'
                plan, instructions = read_csv(file)

    elif route[3] == 'gym':
        if route[4] == 'frail':
            file = 'static/csv/beginner/g_beg.csv'
            plan, instructions = read_csv(file)
        if route[1] == 'lose':
            #more cardio
            if int(route[2]) <= 3:
                #beginner
                file = 'static/csv/beginner/g_c_beg.csv'
                plan, instructions = read_csv(file)
            elif int(route[2]) < 8:
                #intermediate
                file = 'static/csv/intermediate/g_c_int.csv'
                plan, instructions = read_csv(file)
            if int(route[2]) > 7:
                #advanced
                file = 'static/csv/advanced/g_c_adv.csv'
                plan, instructions = read_csv(file)
        elif route[1] == 'gain':
            #less cardio
            if int(route[2]) <= 3:
                #beginner
                file = 'static/csv/beginner/g_nc_beg.csv'
                plan, instructions = read_csv(file)

            elif int(route[2]) < 8:
                #intermediate
                file = 'static/csv/intermediate/g_nc_int.csv'
                plan, instructions = read_csv(file)
            if int(route[2]) > 7:
                #advanced
                file = 'static/csv/advanced/g_nc_adv.csv'
                plan, instructions = read_csv(file)
        else:
            #average cardio
            if int(route[2]) <= 3:
                #beginner
                file = 'static/csv/beginner/g_beg.csv'
                plan, instructions = read_csv(file)
            elif int(route[2]) < 8:
                #intermediate
                file = 'static/csv/intermediate/g_int.csv'
                plan, instructions = read_csv(file)
            if int(route[2]) > 7:
                #advanced
                file = 'static/csv/advanced/g_adv.csv'
                plan, instructions = read_csv(file)

    return render_template("features/fitnessQs/result.html", plan=plan, instructions=instructions, file=file)
