#coding=utf-8
from flask import Flask, url_for, request,redirect, Response,jsonify


app = Flask(__name__)


class JsonResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JsonResponse, cls).force_type(response,environ)

app.response_class = JsonResponse


@app.route('/')
def login():
    return '这是登录页面', 200, {'x-name':'xia','x-age':18}


@app.route('/profile/')
def profile():
    if request.args.get('name'):
        return "个人中心页面"
    else:
        return redirect(url_for('login'))


@app.route('/u/')
def users():
    return {"u-name":'zhiliao',"u-age":18}


@app.route('/u2/')
def users_file():
    resp = Response('user')
    resp.set_cookie('country', 'china')
    return resp




app.run(debug=True, port=9000)