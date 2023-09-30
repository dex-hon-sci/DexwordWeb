#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 05:24:07 2023

@author: dexter
"""

from website import create_app
host = 'http://localhost:5000/'


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

