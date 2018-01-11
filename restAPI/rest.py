from flask import Flask, request
# from flask.ext.mysql import MySQL
app = Flask(__name__)

# mySQL Configurations
'''
mysql = MySQL()
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='testuserdb'
app.config['MYSQL_DATABASE_HOST']='127.0.0.1'
mysql.init_app(app)
conn = mysql.connect()
'''

password = {
	'secret': '111' 	
};

@app.route('/api',methods = ['GET', 'POST', 'DELETE'])
def api_actions():
	if request.method =='GET':

		print("GET REQUEST")
		'''
		if 'password' in request.args and password['secret']==request.args['password']:
			response={
			'message': 'Password '+request.args['password']+' correct'+'\n'
			}
			return response['message']
		else:
			return 'Incorrect Password\n'
		'''


	elif request.method =='POST':
		
		print("POST REQUEST")

		'''
		if 'password' in request.args and password['secret']==request.args['password']:
			response={
			'message': 'Password '+request.args['password']+' correct'+'\n'
			}
			return response['message']
		else:
			return 'Incorrect Password\n'
		'''

if __name__ == "__main__":
	app.run(debug=True)