from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.survey import Survey


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_survey', methods=['POST'])
def add_survey():
    print(request.form, " this is request form")
    if not Survey.validate_survay(request.form):
        return redirect('/')
    data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "language": request.form['language'],
        "comment": request.form['comment']
    }
    result = Survey.add_survey(data)
    return redirect(f"/result/{result}")


@app.route('/result/<int:survey_id>')
def show_result(survey_id):
    print(survey_id, " this is servey_id")
    data = {
        "id": survey_id
    }
    one_survey = Survey.get_survey(data)
    return render_template('result.html', one_survey=one_survey)


@app.route('/all_surveys')
def all_surveys():
    all_surveys = Survey.get_all()
    print(all_surveys, " this is all surveys")
    return render_template('surveys.html', all_surveys=all_surveys)
