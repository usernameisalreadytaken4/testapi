from flask import Flask, jsonify, abort


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Chees, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id':2,
        'title': u'Learn Python',
        'description': u'Need to find a good python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if task is None:
        abort(404)
    return jsonify({'task': task[0]})


if __name__ == '__main__':
    app.run(debug=True, port=5001)