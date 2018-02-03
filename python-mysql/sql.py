from flask.ext.mysql import MySQL

#mySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']=''
app.config['MYSQL_DATABASE_HOST']=''
mysql.init_app(app)
conn = mysql.connect()
