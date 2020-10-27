# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:20:59 2020

@author: Sami
"""

from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)	

