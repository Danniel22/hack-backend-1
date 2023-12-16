from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/h2', methods=['POST'])
def fn_Post():
    if request.is_json:
        return jsonify({"payload":"post"}), 200
    else:
        return "Bad Request", 400

if __name__ == '__main__':
    app.run(debug=True)