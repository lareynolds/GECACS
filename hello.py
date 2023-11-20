# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 20:54:16 2023

@author: pixie
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>This is a test</p>"