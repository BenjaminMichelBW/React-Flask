from flask import Flask
from flask_cors import CORS

app =Flask(__name__)
CORS(app) # enable CORS on all routes

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/users')
def get_users():
    return {
        'users': ['Alice','Bob','Charlie']
    }

@app.route('/api/fruits')
def get_fruits():
    return ['Manzana', 'Banana', 'Cherry']

if __name__ == '__main__':
    app.run(debug=True) # by default, Flask runs on port 5000