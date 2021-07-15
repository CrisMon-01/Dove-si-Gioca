from flask import Flask, jsonify, make_response
import json

app = Flask(__name__)

@app.route("/")
def hello():
    with open ("./data.json", "r") as myfile:
        json_response = json.load(myfile)
        return make_response(jsonify(json_response),200)

if __name__ == '__main__':
    metodo()
    app.run(port=5000,debug=True)
