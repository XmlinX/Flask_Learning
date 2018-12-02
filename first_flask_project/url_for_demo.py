from flask import Flask, url_for


app = Flask(__name__)
app.config.from_pyfile('config.py')




@app.route('/')
def hello_world():
    print(url_for('my_list', page=2, count = 12))
    return 'Hello World!'


@app.route('/list/<page>/')
def my_list(page):
    print(url_for('hello_world'))
    return '你访问的是第%s页' % page




if __name__ == '__main__':
    app.run(port=9000)