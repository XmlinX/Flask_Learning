from flask import Flask, render_template

app = Flask(__name__)
app.config.update(DEBUG=True)


@app.route('/')
def hello_world():
    return render_template('index.html', name='xia', age=18)


@app.route('/u/')
def profile():
    context = {
        "username":'json',
        "age":18,
        "country":'china',
        "Children":{
            "name":'xia',
            "age":-18,
            "height":180
        }
    }
    return render_template('index.html', **context)


@app.route('/login/<id>')
def login(id):
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
