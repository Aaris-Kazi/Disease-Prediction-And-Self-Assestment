from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# @app.route('/', methods = ['POST', 'GET'])
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/assist')
def assist():
    return render_template('assist.html')



if __name__ == '__main__':
    app.run(debug=True)