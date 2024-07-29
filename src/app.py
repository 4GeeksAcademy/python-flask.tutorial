from flask import Flask, jsonify, request

app = Flask(__name__)

# Global todos variable
todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json

    if not request_body or 'label' not in request_body or 'done' not in request_body:
        return jsonify({"error": "Invalid input"}), 

    todos.append(request_body)

    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

    if position < 0 or position >= len(todos):
        return jsonify({"error": "Position out of range"}), 

    removed_todo = todos.pop(position)
    
    print(f"Deleted todo at position {position}: {removed_todo}")
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
