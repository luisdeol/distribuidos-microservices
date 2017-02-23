import os
from json import dumps

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')


@app.route("/students")
def students():
    students = [
        {
            "name": "Luis Felipe",
            "age": "24"
        },
        {
            "name": "Helora Dana",
            "age": "50"
        }
    ]
    return dumps(students)


@app.route("/teachers")
def teachers():
    teachers = [
        {
            "name": "Luis Felipe",
            "age": "24",
            "country": "South Korea"
        },
        {
            "name": "Helora Dana",
            "age": "90",
            "country": "Senegal"
        }
    ]
    return dumps(teachers)


@app.route("/departments")
def departments():
    departments = [
        {
            "name": "DIATINF",
            "phone_number": "12345678"
        },
        {
            "name": "DIAREN",
            "phone_number":"12345678"
        }
    ]
    return dumps(departments)


if __name__ == '__main__':
    app.run()
