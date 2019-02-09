from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)


class LoginView(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help="用户名错误", default="aaaa")
        parser.add_argument('password', type=str, help="密码错误")
        args = parser.parse_args()
        print(args)
        return {"username":"xiamlin"}


api.add_resource(LoginView, '/login/', endpoint='Login')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
