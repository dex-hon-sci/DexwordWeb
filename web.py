#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 05:24:07 2023

@author: dexter
"""

# frontend script to run Dexworld personal website

from flask import Flask, render_template, redirect, request, \
    abort, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
    
    
host = 'http://localhost:5000/'

#def create_app():
#   app = Flask(__name__)
#   app.config["SECRET_KEY"] =''
#   return app

app = Flask(__name__, template_folder='template')


@app.route('/',methods=['GET', 'POST'])
def index():
    
   # from .views import views
   # app.register_blueprint(views, url_prefix="/")
    
    if request.method == 'POST':
        # url input
        pass
    
    return render_template('index2.html')

#render blog with flask varaibles

if __name__ == "__main__":
    app.run(debug=True)