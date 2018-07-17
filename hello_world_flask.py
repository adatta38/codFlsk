from flask import Flask, jsonify, requests
app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hello_World !"


@app.route('/add_two_nums')

def add_two_nums():
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]
    z = x + y
    retJSON = {
        "z":z
    }
    return jsonify(retJSON), 200


if __name__ == "__main__":
    app.run(debug=True)
