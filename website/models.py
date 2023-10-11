#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 02:44:07 2023

@author: dexter
"""

from . import db
from flask_login import UserMixin
#from sql_alchemy.sql import func


# id, title, Topic, Project, file, date_created
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    
    #date_created = db.Column(db.Date(timezone=True), default=func.now())
    
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True)
    Topic = db.Column(db.String(150), unique=True)
    Project = db.Column(db.String(150), unique=True)
    file = db.Column(db.String(150), unique=True)
    
    #date_created = db.Column(db.Date(timezone=True), default=func.now())
