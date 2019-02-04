from flask import Flask, request, Response
from datetime import datetime
from cmsviews import bp


app = Flask(__name__)
app.register_blueprint(bp)
app.config['SERVER_NAME'] = 'hy.com:5000'

@app.route('/')
def hello_world():
    resp = Response("知了课堂")
    resp.set_cookie('username','xia_m_lin',max_age=10, domain='.hy.com')
    expires = datetime(year=2019, month=2, day=5, hour=0, minute=30, second=0)
    resp.set_cookie('age','18', expires=expires)
    return resp


@app.route('/del/')
def del_cookie():
    resp = Response("删除cookie")
    resp.delete_cookie('username')
    return resp



if __name__ == '__main__':
    app.run(debug=True)
