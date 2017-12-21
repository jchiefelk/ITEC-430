from flask import Flask, request
app = Flask(__name__)
password = {
	'secret': '111' 	
};
@app.route('/hello')
def api_hello():
	if 'password' in request.args and password['secret']==request.args['password']:
		response ={
			'message': 'Password '+request.args['password']+' correct'+'\n'
		}
		return response['message']
	else:
		return 'Incorrect Password'

if __name__ == "__main__":
	app.run(debug=True)