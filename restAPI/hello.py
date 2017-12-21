from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {'message': 'hello world'}

todos = {}
class TodoSimple(Resource):
	def get(self, todo_id):
		print(request.args)
		print('headers')
		print(request)


		return {todo_id: todos[todo_id]}
		
	def put(self, todo_id):
		todos[todo_id] = request.form['data']
		return {todo_id: todos[todo_id]}

api.add_resource(HelloWorld,'/')
api.add_resource(TodoSimple,'/<string:todo_id>')

def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'

if __name__ == '__main__':
	app.run(debug=True)