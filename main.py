from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/testSend"
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def hello_world():
    mycol = mongo.db["customers"]
    mydict = {"name": "Kao", "address": "ITE"}
    x = mycol.insert_one(mydict)
    return "<p>1ENGINEER</p>"