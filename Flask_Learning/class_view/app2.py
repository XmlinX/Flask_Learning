from flask import Flask, views, jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def hello_world():
    return 'Hello World!'


class JsonView(views.View):
    def get_data(self):
        raise NotImplementedError
    def dispatch_request(self):
        return jsonify(self.get_data())


class My_list(JsonView):
    def get_data(self):
        return {'name':'zjiliao',"age":18}


class ProfileView(views.MethodView):
    def get(self):
        return '这是get请求'

    def post(self):
        return "这是post请求"



app.add_url_rule('/list/', endpoint='list', view_func=My_list.as_view('list'))
app.add_url_rule('/profile/', endpoint='profile', view_func=ProfileView.as_view('profile'))


if __name__ == '__main__':
    app.run(debug=True)
