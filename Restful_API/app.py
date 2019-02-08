from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class LoginView(Resource):

    def post(self):
        return "username"


api.add_resource(LoginView, '/login/', endpoint='Login')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
