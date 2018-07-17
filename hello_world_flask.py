from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hello_World !"



@app.route('/hithere')

def hithere():
    return "You just checked into Hi There !!!"


@app.route('/add_two_nums', methods=['POST'])

def add_two_nums():
    dataDict = request.get_json(force=True)
#    return jsonify(dataDict)
    x = dataDict["x"]
    y = dataDict["y"]
    z = x + y
    retJSON = {
        "z":z
    }
    return jsonify(retJSON), 200



if __name__ == "__main__":
    app.run(debug=True)
