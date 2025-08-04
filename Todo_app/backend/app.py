from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#CORS(app)
#CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, resources={r"/todos/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

db_created = False

@app.before_request
def create_tables():
    global db_created
    if not db_created:
        db.create_all()
        db_created = True

@app.route('/todos', methods=['GET'])
def get_todos():
    try:
        todos = Todo.query.all()
        if not todos:
            return jsonify({'message': 'Nessun todo trovato.'}), 200
        return jsonify([{'id': t.id, 'task': t.task, 'done': t.done} for t in todos]), 200
    except Exception as e:
        return jsonify({'error': f'Si è verificato un errore: {str(e)}'}), 500

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    task = data.get('task')
    if not task:
        return jsonify({'error': 'Task is required'}), 400
    todo = Todo(task=task)
    db.session.add(todo)
    db.session.commit()
    return jsonify({'id': todo.id, 'task': todo.task, 'done': todo.done}), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body mancante"}), 400
    
    if 'task' in data:
        todo.task = data['task']
    if 'done' in data:
        todo.done = data['done']
    
    db.session.commit()
    return jsonify({'id': todo.id, 'task': todo.task, 'done': todo.done}), 200


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo eliminato'}), 200

if __name__ == '__main__':
    app.run(debug=True)
