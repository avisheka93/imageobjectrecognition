from app import flaskapp
from flask import render_template
#Root Url
@flaskapp.route('/')
def welcome():
    print("route is invoked")
    return render_template('home_page.html',title="Image ",textToDisplay="Welcome to the application")
    