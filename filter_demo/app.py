from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        "name":"json_xia",
        "signature":"<script>alert('hello')</script>",
        "title":"hello world hello me hello you hello we",
        "create_time":datetime(2018, 9, 3, 22, 52)
    }
    return render_template('index.html',**context)


@app.template_filter('cut')
def my_cut(value):
    value = value.replace('hello', '')
    return value


@app.template_filter('handle_time')
def handle_time(time):
    if isinstance(time, datetime):
        timestamp = (datetime.now() - time).total_seconds()
        if timestamp < 60:
            return "刚刚"
        elif 60 < timestamp < 60*60:
            t = int(timestamp/60)
            return "%s 分钟前" % t
        elif 60*60 < timestamp < 24*60*60:
            t = int(timestamp/60/60)
            return "%s 小时前" % t
        elif 24*60*60 < timestamp < 24*60*60*30:
            t = int(timestamp/60/60/24)
            return "%s 几天前" % t
        else:
            return time




if __name__ == '__main__':
    app.run(debug=True)
