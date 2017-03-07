from flask import Flask, jsonify

app = Flask(__name__)

mytask = [
{
	'id': 1,
	'task': u'Finish Hello World',
	'session': u'Week 7',
	'done': True
},
{
	'id': 2,
	'task': u'Finish First API',
	'session': u'Week 7',
	'done': False
}
]

@app.route('/todo/api/tasks', methods=['GET'])
def get_tasks():
	return jsonify({'tasks': mytasks})
 
