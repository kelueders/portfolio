from flask import Blueprint, render_template
import requests

site = Blueprint('site', __name__, template_folder='templates')

@site.route('/')
def home():
    print('Testing the homepage')
    return render_template('index.html')

# @site.route('/about')
# def about():
#     print('About')
#     return render_template('about.html')

@site.route('/projects')
def projects():
    print('Projects')
    return render_template('projects.html')

@site.route('/workout/<id>')
def workout():
    url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/back"

    headers = {
        "X-RapidAPI-Key": "24242474c2msh279df8013b73b3ap1cf7b1jsncf839b04e2e2",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json())

    return render_template('workout.html')

# @site.route('/contact')
# def about():
#     print('Contact')
#     return render_template('contact.html')