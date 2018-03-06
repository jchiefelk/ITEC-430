#!/usr/bin/python
from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(_name_)
app.config ['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password123#'
app.config['MYSQL_DATABASE_DB'] = 'Users'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
#app.run()
