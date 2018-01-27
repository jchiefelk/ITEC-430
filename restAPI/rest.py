from flask import Flask, request
app = Flask(__name__)


@app.route('/api',methods = ['GET', 'POST', 'DELETE'])
def api_actions():
	if request.method =='GET':
<<<<<<< HEAD

		return "GET REQUEST\n"
		'''
		if 'password' in request.args and password['secret']==request.args['password']:
			response={
			'message': 'Password '+request.args['password']+' correct'+'\n'
			}
			return response['message']
		else:
			return 'Incorrect Password\n'
		'''
=======
		return "GET REQUEST\n"
>>>>>>> f7b07a1bf5d89025b6c9b8ffa53d71fd08d7c775


	elif request.method =='POST':
		return "POST REQUEST\n"


if __name__ == "__main__":
	app.run(debug=True)
