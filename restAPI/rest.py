from flask import Flask, request
app = Flask(__name__)


@app.route('/api',methods = ['GET', 'POST', 'DELETE'])
def api_actions():
	if request.method =='GET':
		return "GET REQUEST\n"


	elif request.method =='POST':
		return "POST REQUEST\n"


if __name__ == "__main__":
	app.run(debug=True)