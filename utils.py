from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
import models

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
@app.route("/allTodo",methods = ["GET"])
def getAllTodo():
    rows = models.getTodo()
    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "value": row[1],
            "active": row[2]
        })
    return jsonify({"allTodo" : data})


@app.route("/login",methods = ["POST"])
def handleLogin():
    if request.form.get("username") and request.form.get("password"):
        username = request.form["username"]
        password = request.form["password"]
        result = models.get_user(username,password)
        if result:
            return jsonify({"message":"success","permission":result[0][0]})
        else :
            return jsonify({"message":"Login fail, Username or password is incorrect"})
    return jsonify({"message":"error"})

if __name__ == '__main__':
    app.run()
