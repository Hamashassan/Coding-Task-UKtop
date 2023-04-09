from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    try:
        data = request.get_json()
        numbers = data['numbers']
        result = sum(numbers)
        return jsonify({'result': result}), 200
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid input. Please provide a list of numbers.'}), 400

@app.route('/concat', methods=['POST'])
def concat_strings():
    try:
        data = request.get_json()
        str1 = data['str1']
        str2 = data['str2']
        result = str1 + str2
        return jsonify({'result': result}), 200
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid input. Please provide two strings.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
