from flask import Flask
from blueprints.users import user_bp


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SERVER_NAME'] = 'hy.com:5000'
app.register_blueprint(user_bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
