from flask import render_template, Blueprint, redirect, url_for, request
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
        water = "Please ensure you are drinking at least 3 litres of water per day"
    else:
        water= "Well done, ensure you continue drinking 3 or more litres of water per day"
    if len(choices[1]) >=3:
        meal, recipe = read_csv('static/csv/meals/all.csv')
        return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)
    if (choices[1][0]) == "none":
        meal, recipe = read_csv('static/csv/meals/none.csv')
        return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)
    if 'gluten' in choices[1] or 'keto' in choices[1]:
        if 'nut' in choices[1]:
            meal, recipe = read_csv('static/csv/meals/n_gk.csv')
            return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)
        elif 'vegan' in choices[1] or 'lactose' in choices[1]:
            meal, recipe = read_csv('static/csv/meals/vl_gk.csv')
            return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)
        elif 'veg' in choices[1]:
            meal, recipe = read_csv('static/csv/meals/gk_veg.csv')
            return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)
        elif 'pesc' in choices[1]:
            meal, recipe = read_csv('static/csv/meals/gk_p.csv')
            return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)
        meal, recipe = read_csv('static/csv/meals/gk.csv')
        return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)
    elif 'vegan' in choices[1] or 'lactose' in choices[1]:
        if 'nut' in choices[1]:
            meal, recipe = read_csv('static/csv/meals/n_vl.csv')
            return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)

        meal, recipe = read_csv('static/csv/meals/vl.csv')
        return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)

    elif 'veg' in choices[1]:
        if 'nut' in choices[1]:
            meal, recipe = read_csv('static/csv/meals/n_veg.csv')
            return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)

        meal, recipe = read_csv('static/csv/meals/veg.csv')
        return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)
    elif 'nut' in choices[1]:
        if 'pesc' in choices[1]:
            meal, recipe = read_csv('static/csv/meals/n_p.csv')
            return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)
        meal, recipe = read_csv('static/csv/meals/nut.csv')
        return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)

    elif 'pesc' in choices[1]:
        meal, recipe = read_csv('static/csv/meals/pesc.csv')
        return render_template("features/nutritionQs/result.html", meal=meal, recipe=recipe, water=water)
