from flask import request
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User_Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,{}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)