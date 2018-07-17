from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)

# api = Api(hello_world_flask)
api = Api(app)

def checkPostedData(postedData, functionName):
    if "x" not in postedData or "y" not in postedData:
        return 3001
    else:
        return 200

class Add(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJSON = {
                "Message":"An error happened !",
                "Status Code":status_code
            }
            return jsonify(retJSON)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x + y
        retMap = {
        'Message':ret,
        'Status Code':200
        }
        return jsonify(retMap)

api.add_resource(Add, "/add")





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
