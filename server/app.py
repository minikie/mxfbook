from flask import Flask, request, jsonify
import json
import numpy

app = Flask(__name__)

@app.route("/")
def index():
    return 'hello world!'

@app.route("/getmhdata", methods=['POST'])
def get_data():
    str = '''1|2|3|4|5
            6|7|8|9|10'''
    return str
    #return json.dumps({'test': [1,2,3]})


if __name__ == '__main__':
    app.run()