#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:56:46 2023

@author: dexter
"""

from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return "Login"

@auth.route('/sign-up')
def sigh_up():
    return "Sigh up"

@auth.route('/logout')
def logout():
    return "Logout"