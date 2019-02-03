from flask import Flask, request,render_template
import config
import uuid

app = Flask(__name__,template_folder=)
#app.debug = True
#app.config.update(DEBUG=True)
app.config.from_object(config)
#app.config.from_pyfile('config.py')

@app.route('/')
def hello_world():
    # a = 1
    # b = 0
    # c = a / b
    # print('开启debug模式5')
    # return 'Hello World!'
    return render_template('list.html')

'''string数据类型，未指明数据类型，默认采用此种数据类型，只接受字符串类型的数据'''
@app.route('/p/<article_id>')
def article_detail(article_id):
    return '您访问的书籍详情是%s'% article_id


'''int数据类型，只接受整数类型的数据'''
@app.route('/u/<int:user_id>')
def user_detail(user_id):
    return '您访问的用户详情是%s' % user_id


'''path数据类型，跟string相似，只是可以接受多重路径'''
@app.route('/p1/<path:article_id>')
def article(article_id):
    return '您访问的书籍详情是%s' % article_id

'''uuid数据类型，全宇宙唯一，只接受uuid类型的数据结构'''
@app.route('/u2/<uuid:id>')
def user(id):
    return '您访问的用户详情是%s' % id

'''any数据类型，可以在一个URL中指定多个数路径'''
@app.route('/<any(blog, article):url_path>/<id>/')
def detail(url_path, id):
    if url_path == 'blog':
        return '博客详情:%s' % id
    else:
        return '文章详情：%s' % id


'''使用查询字符串的形式'''
@app.route('/u3/')
def d():
    wd = request.args.get('wd')
    kw = request.args.get('kw')
    return '你查询的内容为：%s,%s' % (wd, kw)


if __name__ == '__main__':
    #app.run(debug=True,port=9000)
    uid = uuid.uuid4()
    print(uid)
    app.run(port=9000)
