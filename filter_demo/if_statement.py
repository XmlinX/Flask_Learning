from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def hello_world():
    context = {
        "name":"json_xia",
        "signature":"<script>alert('hello')</script>",
        "title":"hello world hello me hello you hello we",
        "create_time":datetime(2018, 9, 3, 22, 52),
        "age":19,
        "users":['xia1','xia2','xia3','xia4'],
        "person":{
            "username":"xia",
            "age":18,
            "country":"China"
        },
        "books":[
            {
                "name":"三国演义",
                "author":"罗贯中",
                "price":127
            }, {
                "name":"水浒传",
                "author":"施耐庵",
                "price":121
            }, {
                "name":"西游记",
                "author":"吴承恩",
                "price":130
            }, {
                "name":"红楼梦",
                "author":"曹雪芹",
                "price":160
            },
        ]

    }
    return render_template('page1.html',**context)


@app.template_filter('cut')
def my_cut(value):
    value = value.replace('hello', '')
    return value


@app.route('/v1/')
def table():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(debug=True)
