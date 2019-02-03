from flask import Flask, views

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def hello_world():
    return 'Hello World!'


class My_list(views.View):

    def dispatch_request(self):
        return "my list"


app.add_url_rule('/list/', endpoint='list', view_func=My_list.as_view('list'))


if __name__ == '__main__':
    app.run(debug=True)
