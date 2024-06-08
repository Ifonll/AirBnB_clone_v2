#!/usr/bin/python3
""""flask starts a web application"""
from flask import Flask

app = Flask(__name__)

@app.route("/",strict_slashes=False)
def saying_hello():
    """"dispplays hello"""
    return "Hello HBNB!"

@app.route("/hbnb",strict_slashes=False)
def hbnb():
    """"displays hbnb"""
    return "HBNB"
    
if __name__=="__main__":
    app.run(host="0.0.0.0")