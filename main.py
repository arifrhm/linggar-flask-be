from flask import Flask, jsonify, request

# Membuat instance Flask
app = Flask(__name__)

# Data tugas akan disimpan dalam list untuk kemudahan
tasks = []

# Endpoint untuk mendapatkan semua tugas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Endpoint untuk mendapatkan tugas berdasarkan ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404

# Endpoint untuk menambahkan tugas baru
@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Endpoint untuk memperbarui tugas
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['title'] = request.json.get('title', task['title'])
        task['description'] = request.json.get('description', task['description'])
        task['done'] = request.json.get('done', task['done'])
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404

# Endpoint untuk menghapus tugas
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({'result': True})
    else:
        return jsonify({'error': 'Task not found'}), 404

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True)
