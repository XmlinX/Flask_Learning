from flask import Flask, session
import os
from datetime import timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route('/')
def hello_world():
    '''设置session
    （1）设置加盐的字符串SECRET_KE
    （2）使用session来设置，跟操作字典类似'''
    session['username'] = 'zhiliao'
    session['age'] = 18
    return 'Hello World!'

#获取session
@app.route('/get_session/')
def Get_session():
    username = session.get('username')
    return username or "没有session"

#删除sesion方法一：
@app.route('/del_session/')
def Del_session():
    session.pop('username')
    return "删除成功"

#删除session方法二：
@app.route('/del_session2/')
def Del_session2():
    session.clear()
    return "删除成功"


#设置session的有效期
@app.route('/lifetime/')
def Set_lifetime():
    session['name'] = 'xia'
    session.permanent = True
    return "xia_mei_lin"


if __name__ == '__main__':
    app.run(debug=True)
