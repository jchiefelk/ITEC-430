from flask import Flask
from flaskext.mysql import MySQL
app=Flask(__name__)

#mySQL
mysql = MySQL()

app
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='employees'
app.config['MYSQL_DATABASE_HOST']='127.0.0.1'
mysql.init_app(app)
conn = mysql.connect()
