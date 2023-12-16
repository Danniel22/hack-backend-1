from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/h4', methods=['DELETE'])
def fn_Delete():
    if request.method == 'DELETE':
        return jsonify({"payload":"delete"}), 200

if __name__ == '__main__':
    app.run(debug=True)