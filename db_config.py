# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:11:24 2020

@author: Sami
"""

from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '01014363146'
app.config['MYSQL_DATABASE_DB'] = 'boutique'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)