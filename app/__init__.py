'''
This is the root of the application initialize the flask app here.
''' 
from flask import Flask
import logging
#initialization of app.
flaskapp = Flask(__name__)
#importing routes(Url's for the application.
import app.routes