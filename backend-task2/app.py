from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    # Get the username and password from the request body
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Check if both username and password are provided
    if not username or not password:
        return jsonify({'message': 'Both username and password are required.'}), 400

    # Check if the username is already taken
    if username in users:
        return jsonify({'message': 'Username already taken.'}), 400

    # Add the new user
    users[username] = password

    return jsonify({'message': 'Registration successful.'}), 200

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the request body
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Check if both username and password are provided
    if not username or not password:
        return jsonify({'message': 'Both username and password are required.'}), 400

    # Check if the username exists
    if username not in users:
        return jsonify({'message': 'Invalid username.'}), 401

    # Check if the password matches
    if users[username] != password:
        return jsonify({'message': 'Invalid password.'}), 401

    return jsonify({'message': 'Access granted.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
