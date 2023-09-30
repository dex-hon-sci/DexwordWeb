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

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    
    from .auth import auth
    from .views import views

    
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")
    
    
    return app