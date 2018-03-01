from flask import Flask, request
app = Flask(__name__)

password={
	'secret': '1111'
}

@app.route('/api',methods = ['GET', 'POST', 'DELETE'])
def api_actions():
	if request.method =='GET':

		print(request.args)

		if 'password' in request.args and password['secret']==request.args['password']:
			response={
			'message': 'Password '+request.args['password']+' correct'+'\n'
			}
			return response['message']
		else:
			return 'Incorrect Password\n'

		return "GET REQUEST\n"


	elif request.method =='POST':
		return "POST REQUEST\n"


if __name__ == "__main__":
	app.run(debug=True)
