from app import app
from flask import render_template
#Root Url
app.route('/')
def welcome():
    return render_template('index.html',title="Dropbox clone",textToDisplay="Welcome to the application")