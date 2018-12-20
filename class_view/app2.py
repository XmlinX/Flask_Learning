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


app.add_url_rule('/list/', endpoint='list', view_func=My_list.as_view('list'))


if __name__ == '__main__':
    app.run(debug=True)
