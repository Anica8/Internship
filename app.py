from flask import Flask, render_template, Response, jsonify,request
import os
from os import path
import face_detection as fd
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("page.html",template_folder='templates')


@app.route('/next',methods=['GET'])
def imageUpload():
    res=fd.result()
    # home would contain something like "/Users/jame"
    home = str(Path.home())
    path1 = home + "\Downloads\pic.jpg"
    if path.exists(path1):
        os.remove(path1)
    return res


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True,port="5000")