#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:56:46 2023

@author: dexter
"""

from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/sign-up')
def sigh_up():
    return render_template("signup.html")

@auth.route('/logout')
def logout():
    return redirect(url_for("views.home"))