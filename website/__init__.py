#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:47:42 2023

@author: dexter
"""

from flask import Flask, render_template, redirect, request, abort, jsonify

from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #db.init_app(app)
    
    from .auth import auth
    from .views import views

    
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")
    
    #create_database(app)
    
    return app

def create_database(app):
    if not path.exists("website/"+ DB_NAME):
        db.create_all(app=app)
        print("Created")
        