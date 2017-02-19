# bullyblocker.py

from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def render():
        return render_template('index.html')

@app.route('/bullyblocker')
def render1():
        return render_template('index.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)