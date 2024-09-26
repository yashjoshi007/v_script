#Coded by Sumanjay on 29th Feb 2020
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'News API is UP!<br><br>A part of <a href="https://t.me/sjprojects">Sj Projects</a>'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
