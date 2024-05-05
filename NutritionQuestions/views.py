from flask import render_template, Blueprint, redirect, request, url_for
from NutritionQuestions.forms import QuestionOne, QuestionTwo, QuestionThree
from FitnessQuestions.views import read_csv

meal_blueprint = Blueprint('meal', __name__, template_folder='templates/features/nutritionQs')

choices = []

@meal_blueprint.route('/meal', methods=['get','post'])
def meal_plan():
    form = QuestionOne()
    if form.yes.data:
        return redirect("/mtwo")
    if form.no.data:
        return redirect("/")
    return render_template("features/nutritionQs/question1.html", form=form, alert_message=request.args.get('alert'))

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
        return redirect(url_for('meal.meal_plan', alert='Please press ok to restart the set of questions'))
    if choices[0] <= "3":
        water = "Please ensure you are drinking at least 3 litres of water per day"
    else:
        water = "Well done, ensure you continue drinking 3 or more litres of water per day"
    if len(choices[1]) >=3:
        file = 'static/csv/meals/all.csv'
        meal, recipe = read_csv(file)

    if (choices[1][0]) == "none":
        file = 'static/csv/meals/none.csv'
        meal, recipe = read_csv(file)

    if 'gluten' in choices[1] or 'keto' in choices[1]:
        if 'nut' in choices[1]:
            file = 'static/csv/meals/n_gk.csv'
            meal, recipe = read_csv(file)

        elif 'vegan' in choices[1] or 'lactose' in choices[1]:
            file = 'static/csv/meals/vl_gk.csv'
            meal, recipe = read_csv(file)

        elif 'veg' in choices[1]:
            file = 'static/csv/meals/gk_veg.csv'
            meal, recipe = read_csv(file)

        elif 'pesc' in choices[1]:
            file = 'static/csv/meals/gk_p.csv'
            meal, recipe = read_csv(file)
        else:
            file = 'static/csv/meals/gk.csv'
            meal, recipe = read_csv(file)

    elif 'vegan' in choices[1] or 'lactose' in choices[1]:
        if 'nut' in choices[1]:
            file = 'static/csv/meals/n_vl.csv'
            meal, recipe = read_csv(file)
        else:
            file = 'static/csv/meals/vl.csv'
            meal, recipe = read_csv(file)


    elif 'veg' in choices[1]:
        if 'nut' in choices[1]:
            file = 'static/csv/meals/n_veg.csv'
            meal, recipe = read_csv(file)
        else:
            file = 'static/csv/meals/veg.csv'
            meal, recipe = read_csv(file)

    elif 'nut' in choices[1]:
        if 'pesc' in choices[1]:
            file = 'static/csv/meals/n_p.csv'
            meal, recipe = read_csv(file)
        else:
            file = 'static/csv/meals/nut.csv'
            meal, recipe = read_csv(file)


    elif 'pesc' in choices[1]:
        file = 'static/csv/meals/pesc.csv'
        meal, recipe = read_csv(file)

    return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water, file=file)
