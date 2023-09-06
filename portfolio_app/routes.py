from flask import Blueprint, render_template
import requests
import random

site = Blueprint('site', __name__, template_folder='templates')

@site.route('/')
def home():
    print('Testing the homepage')
    return render_template('index.html')

@site.route('/about')
def about():
    print('About')
    return render_template('about.html')

@site.route('/projects')
def projects():
    print('Projects')
    return render_template('projects.html')

@site.route('/workout/', methods=['GET'])
def workout():
    
    url_bodyPart = "https://exercisedb.p.rapidapi.com/exercises/"

    headers = {
        "X-RapidAPI-Key": "24242474c2msh279df8013b73b3ap1cf7b1jsncf839b04e2e2",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    data = requests.get(url_bodyPart, headers=headers).json()

    ids = []

    for elem in data:
        for k, v in elem.items():
            if k == 'id':
                ids.append(v)

    result = random.choice(ids)

    url_id = f"https://exercisedb.p.rapidapi.com/exercises/exercise/{result}"

    exercise = requests.get(url_id, headers=headers).json()

    return render_template('workout.html', exercise = exercise)

# @site.route('/contact')
# def about():
#     print('Contact')
#     return render_template('contact.html')