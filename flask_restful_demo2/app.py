from flask import Flask
import config
from exts import db
from flask_restful import Api, Resource, fields, marshal_with


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
api = Api(app)


class Article(object):

    def __init__(self, title, content):
        self.title = title
        self.content = content

article = Article(title='xia', content='xxxx')


class ArticleView(Resource):

    resource_field = {
        'title':fields.String,
        'author':fields.String,
    }
    @marshal_with(resource_field)
    def get(self):
        # restful 规范中，要求定义好了返回参数以后即使这个参数没有返回值，也应该返回，返回一个none
        return {"title":'xia'}


class ArticleView2(Resource):

    resource_field = {
        'title':fields.String,
        'content':fields.String,
    }
    @marshal_with(resource_field)
    def get(self):
        # 可以接受一个模型返回
        return article



api.add_resource(ArticleView2, '/article2/', endpoint='article2')
api.add_resource(ArticleView, '/article/', endpoint='article')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
