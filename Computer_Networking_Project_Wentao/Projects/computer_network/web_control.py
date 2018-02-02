# !/usr/bin/env python
#  encoding:utf-8
from flask import Flask, render_template, request
import tools
import requests
import time
app = Flask(__name__)
@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")
@app.route('/startLED.html', methods=['GET', 'POST'])
def startLED():
    if request.method == 'POST':
        tools.startLED()
        return 'success!'
@app.route('/endLED.html', methods=['GET', 'POST'])
def endLED():
    if request.method == 'POST':
        tools.endLED()
        return 'success!'
if __name__ == '__main__':
   app.run(port=8880)
