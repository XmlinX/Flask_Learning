from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


#自定义转换器：在实际开发过程中，有时候希望传递自定义的数据类型
class TelephoneConverter(BaseConverter):
    regex = r'1[3875]\d{9}'


class ListConverter(BaseConverter):

    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        return '+'.join(value)


app.url_map.converters['tel'] = TelephoneConverter
app.url_map.converters['list'] = ListConverter


@app.route('/u/<tel:telephone>/')
def phone(telephone):
    return '你查询的点换号码是%s' % telephone


@app.route('/posts/<list:boards>/')
def posts(boards):
    return '您访问的模版是%s' % boards
    #return boards


@app.route('/')
def hello_world():
    return url_for('posts',boards=['a','b'])


if __name__ == '__main__':
    app.run(debug=True, port=9000, host='0.0.0.0')