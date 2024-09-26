from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify(message="Hello, this Flask app is hosted on Vercel!")

if __name__ == '__main__':
    app.run(debug=True)
