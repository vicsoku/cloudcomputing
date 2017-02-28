from flask import Flask, jsonify

app=Flask(__name__)

mytasks=[
{
	'id':1,
	'task':u'FInish Hello World',
	'session': u'Week 7',
	'done': True
},
{
	'id': 2,
	'task': u'Finish first API',
	'session': u'Week 7',
	'done': False
}
]

@app.route('/todo/api/task',methods=['GET'])
def get_tasks():
	return jsonify({'tasks':mytasks})

