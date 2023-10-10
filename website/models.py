#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 02:44:07 2023

@author: dexter
"""

from . import db
from flask_login import UserMixin
from sql_alchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)