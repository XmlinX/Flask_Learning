#### 章节1——Flask视图函数与url

#### 课时1 【虚拟环境】

##### 	为什么需要使用虚拟环境？

​	到目前为主，我们所有的第三方包都是直接通过pip install 的方式安装的。这样安装会将那个包安装到我们系统级别的Python环境中。但是这样就有一个问题，如果你现在用Djiango 1.10.x写了个网站，然后你的领导跟你说，之前的旧项目是用Djiango 0.9开发的，让你维护，但是Djiango 0.9 和Djiango 1.10.x 相互不兼容。这时候就会碰到一个问题，我如何在我的电脑中同时拥有Djiango 0.9 和Djiango 1.10.x 两套环境呢？这时候我们发现可以通过虚拟环境来解决这个问题了。

##### 	虚拟环境原理

​	 虚拟环境相当于一个抽屉，在这个抽屉中安装的任何软件包都不会影响其他抽屉。并且在项目中，我可以指定这个项目使用的虚拟环境来配合我的项目。比如我们现在有一个项目是基于Djiango 0.9 开发的，又有一个项目是基于Djiango 1.10.x 开发的。这个时候可以创建两个虚拟环境分别安装Djiango 0.9 和Djiango 1.10.x 来配合我们的项目。



#### 课时2【安装虚拟环境】

```Python
    #安装到系统级别的环境中

    '''安装到Python2环境中'''
    pip install virtualenv 

    '''安装到Python3环境中'''
    pip3 install virtualenv

    #创建虚拟环境
    virtualenv my_venv

    #进入到虚拟环境
    source my_venv/bin/active
    '''进入到虚拟环境之后，之后所有的操作都只是对该环境有影响，而不会对其系统环境产生影响'''

    #推出虚拟环境
    deactive

    #创建虚拟环境的时候指定Python解释器
    virtualenv -p + 解释器路径 + 虚拟环境名称


```



#### 课时3【使用virtualenvwrapper】 

```Python
#使用virtualenvwrapper
'''virtualenvwrapper 这个软件可以更好的帮助我们管理虚拟环境，使得我们管理虚拟环境更加简单，不用在跑道虚拟环境所在的目录，去激活虚拟环境'''
pip install virtualenvwrapper

#创建虚拟环境，将会在当前用户下创建一个Env的文件夹，然后将这个虚拟环境安装到这个目录下。
mkvirtualenv my_env

#切换到相应的虚拟环境
workon my_env

#列举所有的虚拟环境
lsvirtualenv

#删除虚拟环境
rmvirtualenv my_env

#修改虚拟环境所在的目录
export WORKON_HOME=/Users/xiameilin/Envs
source /Users/xiameilin/anaconda3/bin/virtualenvwrapper.sh

#创建虚拟环境的时候指定的Python解释器
mkvirtualenv --python==解释器路径 + 虚拟环境名称

```



#### 课时4【课程介绍】 

​	URL与视图 + Jinja2模版 + SQLAlchemy框架 + Flask知识点补充 + msmcache缓存 + Redis 



#### 课时5【Flask预热】 

环境准备：

​	python 3.6 + Pycharm 

安装虚拟环境：

​	virtualenvwrapper

安装flask：

```python
pip install flask
```



#### 课时6【URL组成部分详解】

URL：uniform resource locator  统一资源定位符

一个URL主要由以下几部分组成：scheme://host:port/path/?query-string=xxxx#anchor

​	scheme:代表的是访问使用的协议，一般是http或者https以及ftp协议等；

​	host:主机名，域名，比如www.baidu.com,代表服务器的名称（IP地址主机名类似我们手机号码和备注）

​	port:端口号，类似于门牌号，因为一个服务器上不止一个服务，通过端口号来区别不同的服务（http:80，			   			  	https:443）

​	path:查找路径

​	query-string：查询字符串

​	anchor：锚点

URL中所有的字符串都是使用ascii编码，如果出现非ascii码，浏览器一般都会尽心编码后传输。

​	

#### 课时7【Web服务器、应用服务器、Web应用框架】

web服务器：用来处理http请求，响应静态文件，常用的有Apache，Nginx，以及微软的IIS。比如我们发送一个请求到百度，那么百度首先使用web服务器，接受我们的请求，如果我们的请求是一个静态文件（css／html／js／img）那么web服务器直接将结果返回给我们，但是如果我们请求的是一个动态的数据，这些数据是要存在数据库的，请求完之后需要做一定的逻辑处理，因此web服务器就无法处理，就需要讲请求转给我们的应用服务器。

应用服务器：负责处理逻辑的服务器。比如PHP、Python代码，web服务器是无法处理的，只能由应用服务器来处理。常用的有uwsgi、tocat，它的作用类似于Python解释器，用来执行具体的代码。

Web应用框架：是我们是开发网站的时候更加迅速，不是必须的。封装了一些底层的代码……



####课时8 【第一个Flask程序详解】

特点：

​	1、微框架，简洁，只做它需要做的，给开发者提供了很大的扩展性；

​	2、Flask和相关的依赖（Jinja2，Werkzeug）设计优秀；

​	3、SQLAlchemy的ORM模型操作数据库可以减少大量书写SQL的时间；

​	4、社区活跃度很高；

Flask的灵活度非常高，他不会帮你做太多的决策，即使做了很多的选择，你也可以很容易的更换成你需要的。



```python
'''1、从Flask这个包中倒入Flask这个类
   2、Flask这个类是项目的核心，以后很多操作都是基于这个类的对象
   3、注册URL、注册蓝图等都是基于这个类的对象'''
from flask import Flask

#由Flask生成的一个对象，参数__name__作用：
#1、规定了模版和静态资源的查找路径；
#2、以后Flask—SQLAlchemy，Flask-migrate等插件报错，可以通过该参数快速定位到具体问题在哪里
app = Flask(__name__)

#装饰器，以后我们在访问该路径（／）的时候，会自动执行下面装饰的视图函数，将该视图函数的返回值返回给我们的浏览器
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    #启动一个测试应用服务器
    app.run()，供调试使用，性能差，上线不能使用，需要使用uwsgi
```



#### 课时9【debug模式详解】

##### 1、为什么要开起debug模式？

​	（1）如果开启了debug模式，如果程序中有异常，在我们的浏览器不是展示出来；

​	（2）如果开启了debug模式，不需要重新启动，只需要保存下，程序就会自动加载；

##### 2、如何开启debug模式：

```python
app.run(debug=True)
app.debug = True
app.config.update(DEBUG=True)
#使用配置文件：
#备注：首先要新建一个config文件，然后引入该文件
app.config.from_object(config)
```



#### 课时10【配置文件的两种使用方式】

```python
'''方式一'''
#定义一个config.py的文件，并引入模块
import config
app.congig.from_object(config)

'''方式二'''
# 定义一个config.py的文件,此种方式不需要引入该模块，同时也不一定非得指定为为.py文件，任何格式的文件都可以
# 需要注意的是，此时需要以字符串的形式写全文件的名称
app.config.from_pyfile('config.py')

```



#### 课时11【Flask中传递参数的两种方式】

```python
#视图函数和URL的映射
@app.route('/')
def hello_world():
    print('开启debug模式5')
    return 'Hello World!'

#视图函数中传递参数
@app.route('/p/<article_id>')
def article_detail(article_id):
    return '您访问的书籍详情是%s'% article_id

#视图函数中可以传递的数据类型

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

'''如果页面想做SEO优化，就是被搜索引擎搜索到，则使用path的形式，如果不希望被搜索引擎搜索到则建议使用查询字符串的形式'''

```



#### 课时12【URL_for使用详解】

##### 1、为什么要使用URL_for函数？

​	（1）实际项目中，ulr的变化的频率比视图函数高很多，如果写死了url，那么对于应用了url的地方，都要相应的改动，在项目较大的时候改起来就很麻烦；

​	（2）自动处理特殊字符



##### 2、如何使用url_for函数？

```python
@app.route('/')
def hello_world():
    print(url_for('my_list', page=2, count = 12))
    return 'Hello World!'

@app.route('/list/<page>/')
def my_list(page):
    print(url_for('hello_world'))
    return '你访问的是第%s页' % page
```



##### 3、url_for(endpoint, **args)

​	endpoint:第一个参数就是视图函数对应的字符串名称；

​	**args:关键字参数。如果该参数在视图函数中已经定义了，那么该参数将会当做url的一部分，拼接到url后面；如果该参数在视图函数中没有定义，那么它将以查询字符串的形式添加到url后面；



#### 课时13【自定义url转换器】

1、在实际开发中，有时候希望自己定义符合自己要求的数据类型，这个时候我们自己来定义一个Baseconverter类的对象来实现。

```python
#引入Baseconverter类
from werkzeug.routing import Baseconverter

#定义一个自己的数据类型，继承自Baseconverter
class My_Converter(Baseconverter):
    #定义规则
    regex = r'1[8357]\d{9}'
    
#将自定义的数据类型绑定到对象上
app.url_map.converter['tel'] = My_Converter

#引用自己定义的数据类型
@app.route('/u/<tel:phone>')
def my_phone(phone):
    return "您查询的电话号码是%s" % phone

```

2、在实际开发中，如果我们需要经常处理一些url的参数，这个时候我们也可以自定义一个转换器，实现该转换器的to_python方法，避免每次都要处理该参数。该函数会将用户请求url的参数传给value，然后进行处理，最后将处理后的返回值传递给视图函数，帮助视图函数处理请求url

```python
#引入Baseconverter类
from werkzeug.routing import Baseconverter

#定义一个自己的数据类型，继承自Baseconverter
class ListConverter(BaseConverter):

    def to_python(self, value):
        return value.split('+')
#将自定义的数据类型绑定到对象上
app.url_map.converter['list'] = ListConverter
```

3、还有一种场景，我们在调用url_for()函数的时，将url_for()函数的参数（**args）传递给该函数的value，然后在to_url方法中进行处理，最后将处理后的结果返回给url_for，生成符合要求的url形式

```python
#引入Baseconverter类
from werkzeug.routing import Baseconverter

#自定义转换器：在实际开发过程中，有时候希望传递自定义的数据类型
class ListConverter(BaseConverter):

    def to_url(self, value):
        return '+'.join(value)

app.url_map.converters['list'] = ListConverter
```

完整实例代码如下：

```python
class TelephoneConverter(BaseConverter):
    regex = r'1[3875]\d{9}'

class ListConverter(BaseConverter):

    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        return '+'.join(value)


app.url_map.converters['tel'] = TelephoneConverter
app.url_map.converters['list'] = ListConverter

#自定义url转换器
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

```



#### 课时14【其它小知识点补充】

1、在一个局域网中，如果希望他人也能够访问到我们的网站，则可以通过通过设置host='0.0.0.0'

```python
app.run(debug=True, port=9000, host='0.0.0.0')
```

2、



#### 课时15【重定向】

重定向分两种：永久性重定向和暂时性。

1、永久性重定向：http的状态码为301，一般用在旧的网站被废弃要转到一个新的网址，确保用户访问。

2、暂时性重定向：http的状态码为302，一般用在页面的暂时性跳转。通常要访问的页面时存在的，比如要评论一篇文章，结果跳转到登录页面。

3、在Flask中，使用redirect(url,code=)来实现重定向。其中URL：用来指定重定向的到那个页面，code用来表明状态码

```python
from flask import url_for, redirect

@app.route('/profile/')
def profile():
    if request.args.get('name'):
        return "个人中心页面"
    else:
        return redirect(url_for('login'))
```



#### 课时16【视图函数中Response返回值详解】

##### 1、视图函数可以返回的对象类型：

​	（1）一个合法的Response对象，则可以直接返回

​	（2）返回一个str。其实也还是被包装成了一个Response对象，其中str作为响应的主体（body），状态码为200，MIME：text／html

​	（3）返回一个元组。元组的数据结构为：（response，status，headers）

​			response：作为响应的具体信息返回

​			status：响应的状态码

​			headers：可以以字典或者列表的形式，作为响应的头部信息返回给用户

```python
@app.route('/')
def login():
    return '这是登录页面', 200, {'x-name':'xia','x-age':18}
```

​	（4）如果以上条件都不满足，Flask会假设返回值是一个合法的WSUI应用程序，并通过Response.force_type(rv,request.envision)转换为一个请求对象



```python
#2、自定义相应对象
	#（1）定义一个类，继承自Response类
    #（2）实现force_type方法
    #（3）指定app.response_class为你定义的对象
class JsonResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JsonResponse, cls).force_type(response,environ)

app.response_class = JsonResponse

@app.route('/u/')
def users():
    return {"u-name":'zhiliao',"u-age":18}
'''jsonify作用：
1、将返回的结果转换成json对象
2、将返回的转换成一个response对象'''

#3、设置cookie信息
@app.route('/u2/')
def users_file():
    resp = Response('user')
    resp.set_cookie('country', 'china')
    return resp

```



#### 章节二--Jinja2模版

#### 课时17【模版介绍】

1、模版是什么？

​	html代码

2、为什么要使用模版？

​	在之前的章节中，视图函数只是返回文本，而在实际开发过程中其实很少这样用。因为实际的页面大多数样式和逻辑都很复杂的HTML代码，这样可以让浏览器渲染出非常漂亮的页面。

​	（1）前后端分离

​	（2）较少代码的耦合性。页面逻辑放在模版中，业务逻辑放在视图函数中，将页面逻辑和业务逻辑解耦有利于代码的维护

​	（3）提供了控制语句、继承等高级功能，减少开发的复杂度。

3、怎么样使用模版？

```python
rom flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('list.html')
```

4、其它：

默认情况下，视图函数回去项目下的templates文件夹下寻找模版，如果模版直接是在templates文件夹下，则直接使用模版的名称即可；如果在templates文件夹下还有自文件夹，那么在渲染的时候要指明自文件夹／模版名称；如果自己想指定在其他路径下面，那么就需要在初始化app对象的时候指定一个参数，即：app = Flask(__name__,template_folder=)



#### 课时18【模版传参详解】

模版中有很多的参数（数据），是变化的，不能写死，需要后端实时从数据库中去获取，然后传递到前端

```python
@app.route('/')
def hello_world():
    return render_template('index.html', name='xia', age = 18)


@app.route('/u/')
def profile():
    context = {
        "username":'json',
        "age":18,
        "country":'china',
        "Children":{
            "name":'xia',
            "age":18,
            "height":180
        }
    }
    return render_template('index.html', **context)

	#return render_template('index.html', **context)
    
    #前端
     <p>{{ username }}</p>
     <p>{{ age }}</p>
     <p>{{Children.name}}</p>
     <p>{{Children.name}}</p>
	
```



#### 课时19【模版中使用url_for】

有时候点击首页的登录按钮，会跳转到登录页面。这个时候就需要在首页给定一个a标签，然后使其href属性刚好为要跳转的页面的url即可。按照以前的做法是：

```html
<a href="/login/">登录</a>
```

但是这样和我们之前讲到的一样，很多地方都有跳转到登录页面的超链接，如果一旦我们主app中的视图函数对应的url改变了，那么所有我们使用了该url的地方全部都需要改动，如果网站较大，那么改动就会产生很大的影响。因此我们也采用视图函数反转url的形式

```html
<p>
    <a href="{{ url_for('login', id=1) }}">登录</a>
</p>
```



#### 课时20【过滤器的基本使用】

什么是过滤器？

有时候我们需要对模版中的一些变量进行处理，那就必须类似于python中的函数一样，可以将这个变量传到python函数中。在模版中，过滤器相当于一个函数，根据自身的功能将作用于当前变量，再将处理的结果返回渲染到页面中。

基本语法：过滤器通常使用管道符（|）来使用。例如：{{name|length}}，将返回name的长度。



#### 课时21【默认过滤器的使用】

{{singnature|default("此人很懒，没有留下任何说明")}}，使用default过滤器，当value不存在的时候，就会使用默认过滤器，但是如果有值，但是该值为null／none／false 等还是会显示出来，这个时候就需要给default传递一个参数boolean=True。也相当于singnature or “此人很懒，没有留下任何说明”。



#### 课时22【常用的过滤器】

##### 1、escape(或者e)自动转义过滤器

转义字符，会将<、>等符号转义成Html中的符号。使用方法如下：signature|escape(或者e)。默认是已经开启了该过滤器。可以使用下面的方法关闭该过滤器：

```html
{% autoescape off %}
        <p>个性签名：{{ signature }}</p>
{% endautoescape %}
```

##### 2、safe过滤器：可以关闭一个字符串的自动转义

```html
<p>个性签名：{{ signature|safe }}</p>
```

##### 3、其它标签：

​	（1）abs：获取参数的绝对值

​	（2）length:获取序列的长度

​	（3）first:获取序列的第一个元素

​	（4）last:获取序列的最后一个元素

​	（5）int:将参数装换为整数类型

​	（6）float:将参数转换为浮点类型

​	（7）join(d='u')：将序列通过字符串u拼接在一起

​	（8）truncate(length=24):截取对象长度的一部分

​	（9）striptags:去掉参数中所有的标签

​	（10）trim:截取字符串前面和后面的空白

​	（11）string:将变量转换为字符串

​	（12）wordcount：统计字符串的长度

​	（13）lower:将字符串全部转换为小写

​	（14）upper:将字符串全部转换为大写

​	（15）replace(old,new):将字符串中的old的字符替换为new字符串



#### 课时23【自定义过滤器】

过滤器本质上也是一个函数，因此我们也要在代码中定义一个这样的处理函数。

```python
@app.template_filter('cut')
def my_cut(value):
    value = value.replace('hello', '')
    return value
```

#### 课时24【自定义时间处理过滤器案例】

```python
@app.route('/')
def hello_world():
    context = {
        "name":"json_xia",
        "signature":"<script>alert('hello')</script>",
        "title":"hello world hello me hello you hello we",
        "create_time":datetime(2018, 9, 3, 22, 52)
    }
    return render_template('index.html',**context)

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
        
 <p>{{ create_time|handle_time }}</p>
```



#### 课时25【if语句详解】

if 语句的具体用法跟python中用法类似，但是在Jinja2中必须放在{% if ……%}里面，下面可以写条件满足后的代码，同时还必须要有一个结束标签{% endif %}，也可以在中间嵌套elif

```html
{% if age > 18 %}
	<p>你已成年，可以进入网吧</p>
{% elif age == 18 %}
	<p>你还需要在等半年才能去网吧</p>
{% else %}
	<p>你还是未成年人，不能进入网吧</p>
{% endif %}
```



#### 课时26【for 循环详解】

```html
<tbody>
            {% for book in books %}
                {% if loop.first %}
                    <tr style="background-color: hotpink">
                {% elif loop.last %}
                    <tr style="background-color: aquamarine">
                {% else %}
                    <tr>
                {% endif %}
                    <td>{{ loop.index }}</td>
                    <td>{{ book.name }}</td>
                    <td>{{ book.author }}</td>
                    <td>{{ book.price }}</td>
                </tr>
            {% endfor %}

        </tbody>

```



#### 课时27【九九乘法表案例】

```html
<table border="1">
        <tbody>

        {% for i in range(1,10) %}
            <tr>
                {% for j in range(1, i + 1) %}

                    <td>{{ j }} * {{ i }} = {{ j*i }}</td>

                {% endfor %}

            </tr>
        {% endfor %}
            
        </tbody>
</table>
```



#### 课时28【模版中的宏】

模版中的宏，有点类似python中的函数，可以传递参数，但是不能有返回值。可以将一些经常用到的代码片段放到宏中，然后把一些不固定的值抽取出当成一个变量。

```html
{% macro my_input(name="", type="text", value="")%}
        <input name="{{ name }}" type="{{ type }}" value="{{ value }}">
{% endmacro %}

    <h1>知了登录</h1>
    <table>
        <tbody>
            <tr>
                <td>用户名:</td>
                <td>{{ my_input('username') }}</td>
            </tr>
            <tr>
                <td>密码:</td>
                <td>{{ my_input('password', type='password') }}</td>
            </tr>
            <tr>
                <td></td>
                <td>{{ my_input(value='提交', type='submit') }}</td>
         
```



#### 课时29【宏的导入和注意事项】

在实际开发中，会将一些常用的宏单独放到一个文件中，在需要使用的时候，再从这个文件中导入。

导入宏的方式有两种：

​	（1）采用 from "宏文件的路径" import 宏名称 【as 别名 】

```html
{% from "macros/macro.html" import my_input %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>知了宏</title>
</head>
<body>
    <h1>知了登录</h1>
    <table>
        <tbody>
            <tr>
                <td>用户名:</td>
                <td>{{ macro.my_input('username') }}</td>
            </tr>
            <tr>
                <td>密码:</td>
                <td>{{ macro.my_input('password', type='password') }}</td>
            </tr>
            <tr>
                <td></td>
                <td>{{ macro.my_input(value='提交', type='submit') }}</td>
            </tr>
        </tbody>
    </table>
    <p>{{ username }}</p>
</body>
</html>
```

​	(2) import ”宏文件的绝对路径“  as 别名

```html
{% import "macros/macro.html" as macro with context %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>知了宏</title>
</head>
<body>
    <h1>知了登录</h1>
    <table>
        <tbody>
            <tr>
                <td>用户名:</td>
                <td>{{ macro.my_input('username') }}</td>
            </tr>
            <tr>
                <td>密码:</td>
                <td>{{ macro.my_input('password', type='password') }}</td>
            </tr>
            <tr>
                <td></td>
                <td>{{ macro.my_input(value='提交', type='submit') }}</td>
            </tr>
        </tbody>
    </table>
    <p>{{ username }}</p>
</body>
</html>
```

备注：

​	（1）宏的路径都是相对于templates文件夹的位置而言；

​	（2）如果想要将当前模版中的变量也在宏中引用，那么可以采用 from "macros/macro.html" import my_input with context



#### 课时30【include 标签的使用】

这个标签相当于直接把指定模版中的代码复制粘贴到当前位置。

```html
<!--使用方法-->
{% include "commons/header.html" %}
    <div>
        这是我自己的内容
    </div>
{% include "commons/footer.html" %}
```

注意：

​	（1）include 的路径，也是跟import 一样，都是直接从templates根目录开始去找，不要以相对路径查找。

​	（2）可以直接使用父模版中的变量。和宏不一样，宏还需要在引入的时候加上with context ,include 可以直接使用。



#### 课时31【set和with 语句在模版中定义变量】

有时候我们在开发过程中定义一些变量，然后在整个模版中都可以使用这些变量，这个时候我们就可以通过set在模版中来定义一个变量。如果想要控制这个变量的作用域，那么可以使用with  context

```html
{% set username="xiameilin" %}
{% include "commons/header.html" %}
<div>
    这是我自己的内容
</div>
{% include "commons/footer.html" %}

<p>姓名:{{ username }}</p>
{% with age=18  %}
<p>年龄:{{ age }}</p>
{% endwith %}
```



#### 课时32【加载静态文件】

静态文件：js／css／images／html。在实际开发中，我们经常将各种静态资源都分开放在不同的文件中，便于管理。静态文件一般存放在项目的static文件夹下面，通常我们会根据需要将js／css／imags文件分别放在不同的文件夹下。

```html
	<link rel="stylesheet" href="{{ url_for('static', filename='css/css01.css') }}">
    <script src="{{ url_for('static', filename='js/js01.js') }}"></script>
    <img src="{{ url_for('static', filename='images/bokeh.png') }}">
```

加载静态文件，需要注意到以下几点：

​	（1）如果是css文件，需要添加herf属性

​	（2）如果是js／images文件，需要添加src属性

​	（3）属性值为"url_for('static', filename='css/css01.css'))"，其中该函数的第一参数默认为'static'，第二个关键字参数值为静态资源的路径，该路径都是相对于static文件夹而言的绝对路径。



#### 课时33【模版继承】

Flask中的模版可以继承，通过继承可以把模版中的许都重复的元素提取出来，放在父模版中，并且父模版中通过定义block给子模版开一个口子，子模版根据需要，再实现这个block，假设现在有一个base.html这个父模版代码如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <title>
        {% block title %}

        {% endblock %}
    </title>

    <style>
        .nav ul {
            overflow: hidden;
        }
        .nav ul li {
            float: left;
            margin: 0 30px;

        }
    </style>
</head>
<body>
    <nav class="nav">
        <ul type="none">
            <li>首页</li>
            <li>课程详情</li>
            <li>视频教程</li>
            <li>关于我们</li>
        </ul>
    </nav>
    {% block my_block %}
        <p>我是父模版中的代码</p>
    {% endblock %}
    <footer>
        这是底部内容
    </footer>
</body>
</html>
```

子模版代码：

```html
{% extends "base.html" %}

{% block title %}
    知了首页
{% endblock %}

{% block my_block %}
    {{ super() }}
    {{ self.title() }}
    <p>这是子模版实现的代码</p>
{% endblock %}

```



#### 课时38【类视图】

之前我们接触到的视图都是函数，所以我们一般称为视图函数。其实我们的视图函数也可以基于类实现，类视图的好处是能支持继承。

1、基于标准的类视图

​	（1）继承:views.View

​		class My_list(views.View):

​	（2）必须在子类中实现dispatch_request，该方法类似于视图函数，用来处理请求。也要返回一个基于Response类或者子类的对象

​	（3）将类视图映射到url下面

​		app.add_url_rule('/list/', endpoint='list', view_func=My_list.as_view('list'))

```python
from flask import Flask, views, jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def hello_world():
    return 'Hello World!'


class JsonView(views.View):
    def get_data(self):
        raise NotImplementedError
    def dispatch_request(self):
        return jsonify(self.get_data())


class My_list(JsonView):
    def get_data(self):
        return {'name':'zjiliao',"age":18}


app.add_url_rule('/list/', endpoint='list', view_func=My_list.as_view('list'))


if __name__ == '__main__':
    app.run(debug=True)

```

2、基于请求方法的类视图。这种视图，我们需要自己实现get和post，然后根据用户的请求方法，如果用户使用的是get方法，则执行get方法，如果是post请求，则执行post方法

​	

```python
from flask import Flask, views, jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


class ProfileView(views.MethodView):
    def get(self):
        return '这是get请求'

    def post(self):
        return "这是post请求"

app.add_url_rule('/profile/', endpoint='profile',view_func=ProfileView.as_view('profile'))


if __name__ == '__main__':
    app.run(debug=True)

```



#### 课时40【类视图中使用装饰器】

​		

​	

​	

#### 课时41【蓝图的基本使用】

蓝图主要是为了使我们的flask项目分层解耦，可以将相同模块的视图函数放在同一个文件中，使得代码更加便于管理。

基本语法：

​	在蓝图文件中

​	（1）引入相应的模块：

```python
from flask import Blueprint
```

​	（2）生成一个蓝图（作用类似于app）

```python
user_bp = Blueprint('user', __name__, url_prefix='/user')
```

​	（3）将蓝图绑定url

```python
@user_bp.route('/profile/')
def profile():
    return "这是用户界面"

```

​	主app中：

​	（1）引入相应的蓝图

```python
from blueprints.users import user_bp
```

​	 (2)将该蓝图注册到主app上

```python
app.register_blueprint(user_bp)
```

```python

from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/profile/')
def profile():
    return "这是用户界面"

@user_bp.route('/setting/')
def setting():
    return "这是用户设置界面"


#主app中
from flask import Flask
from blueprints.users import user_bp


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.register_blueprint(user_bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

```



#### 课时42【蓝图中模版文件寻找规则】

如果项目中的templates文件夹中有相应的模版文件。就直接使用；如果项目中的templates文件夹中没有相应的模版文件，那么就去定义蓝图的时候指定的路径中寻找，并且蓝图中指定的路径可以为相对路径，相对这个蓝图文件当前所在的路径

```python
#子模版
from flask import Blueprint

user_bp = Blueprint('user', __name__, subdomain='cms')
@user_bp.route('/profile/')
def profile():
    return "这是用户界面"

@user_bp.route('/setting/')
def setting():
    return "这是用户设置界面"

#父模版
from flask import Flask
from blueprints.users import user_bp
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SERVER_NAME'] = 'hy.com:5000'
app.register_blueprint(user_bp)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

```



#### 课时46【flask数据库-MySQL以及注意事项】

​	设置root密码：root

#### 课时47【SQLAlchemy介绍和基本使用】

数据库是一个网站的基础，在Flask中可以自由的使用MySQL、PostgreSQL、SQLlite、Redis、MongoDB来写原生的语句实现功能，也可以使用更高级别的数据库抽象方式，如SQLAlchemy或MongoEngin这样的ORM。本次主要讲解Python + SQLAlchemy来进行讲解。

（1）确保安装一下软件：

​		1、mysql

​		2、MySQLdb：Python是用来操组Mysql的包。但是在在Python3中，我们使用Pymysql。安装命令：pip install Pymysql (MySQLdb)

​		3、SQLAlchemy：是一个数据库的ORM框架。安装命令：pip install SQLAlchemy

（2）使用SQLAlchemy连接和操作数据库

​		1、终端如何连接数据库：mysql   -h主机地址  -u用户名   -p（如果是本机的话，可以省略 -h主机地址）

​		2、使用SQLAlchemy连接数据库具体操作

```python
from sqlalchemy import create_engine
#from constants import DB_URI

HOSTNAME = '192.168.31.47'
PORT = '3306'
DATABASE = 'demo_test'
USERNAME = 'root'
PASSWORD = 'root'

#dialect+driver://username:password@host:port/database
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'.format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, database=DATABASE)

#使用create_engine创建一个引擎
engine = create_engine(DB_URI)

sql1 = 'select 1'
#使用with语句连接数据库，如果有异常会被捕获
with engine.connect() as  conn:
    result = conn.execute(sql1)
    print(result.fetchone())
```



#### 课时48【Flask数据库-ORM介绍】对象关系映射（模型与表之间的映射）

O：Object 对象	R：Relationship  关系	M：mapping 映射

对象关系映射。通过ORM模型，我们可以通过类的方式操作数据库，而不用再写原声的sql语句。通过把表映射成类，把行映射成实例，把字段作为属性。

随着项目越来越大，采用写原声SQL的方式在代码中出现大量的SQL语句，那么问题就出现了：

​	1、SQL语句重复利用率不高，越复杂的SQL语句条件越多，代码越长，会出现很多相近的SQL的语句。

​	2、很多SQL语句是业务逻辑拼出来的，如果有数据库需要修改，就要去修改这些逻辑，这会很容易遗漏掉对某些SQL语句的修改。

​	3、写SQL时容易忽略web安全问题，给未来造成隐患，例如：sql注入。

```python
class Person(object):
    name = 'xxxx'
    age = 18
    country = 'xxxx'    
    
create table person(name varchar(20) not null, age int default 18, country varchar(25) null)

'''可以作如下映射：
	1、Person类对应数据库中的表person
	2、Person类属性对应数据库的表的字段
	3、Person实例化一个对象对比数据库中的一条数据'''
```



#### 课时49【定义ORM模型并将其映射到数据库中】

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

HOSTNAME = '192.168.31.47'
PORT = '3306'
DATABASE = 'demo_test'
USERNAME = 'root'
PASSWORD = 'root'

#dialect+driver://username:password@host:port/database
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'.format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, database=DATABASE)
#使用create_engine创建一个引擎
engine = create_engine(DB_URI)
#用declarative_base，根据engine创建一个基类
Base = declarative_base(engine)


'''1、创建一个ORM模型，这个模型必须继承自sqlalchemy给我们提供好的基类'''
class Person(Base):
    #定义__tablename__属性，绑定这个模型和数据库中表名
    __tablename__ = 'person'
    
    '''2、给这个ORM模型创建一些属性，来跟数据库表中的字段进行一一对应，这些属性也必须是sqlalchemy给我们提供好的数据类型'''
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25))
    age = Column(Integer)
    
'''3、将创建好的ORM模型，映射到数据库中'''
Base.metadata.create_all()

#一旦使用Base.metadata.create_all()将模型映射到数据库中，即使改变模型，也不会重新映射
```



#### 课时50【使用SQLAlchemy完成数据库的增删改查】

```python
from sqlalchemy.orm import sessionmaker

#构建session对象，所有和数据库的ORM操作都必须通过一个叫session的会话对象来实现对数据的增删改查，
#Session = sessionmaker(engine)
#session = Session()
session = sessionmaker(engine)()

#增
#初始化一个对象，实质就是创建一条数据
p = Person(name='xiameilin', age=18, country='wuhan')
#将对象添加带session中
session.add(p)
#session中的对象做commit操作
session.commit()
'''添加多条数据'''
p1 = Person(name='xiameilin002', age=19, country='shenzhen')
p2 = Person(name='xiameilin003', age=20, country='guangzhou')
session.add_all([p1, p2])
session.commit()

#查
#查找某个模型对应的表中所有的数据
all_persons = session.query(Person).all()
#条件查找
def search_data():
    #查找某个模型对应的表中的数据
    #使用filter_by,相当于SQL语句中查询条件中的where子句
    all_persons = session.query(Person).filter_by(name='xiameilin').all()
    print(all_persons)
    #使用filter，不能写关键字参数，而必须写条件（条件是True，需要使用==）
    all_persons = session.query(Person).filter(Person.name=='xiameilin').all()
    #使用get方法查找，只能根据主键查找，只能返回一条数据或者none
     all_person = session.query(Person).get(1)
    #使用first()查找第一条数据
    all_person = session.query(Person).first()
    
#改
def update_data():
    #要修改对象，首先要获取到该对象，然后修改对象对应的属性为你想要的数据，最后通过commit进行提交
    person = session.query(Person).filter_by(name='xiameilin').first()
    person.name = 'yeyanmei'
    session.commit()
    
#删
def delete_data():
    person = session.query(Person).filter_by(name='yeyanmei').first()
    session.delete(person)
    session.commit()
```



#### 课时51【SQLAlchemy属性常用数据类型详解】

sqlalchemy常用数据类型：

（1）Integer：整形。映射到数据库中是int类型。

（2）Float：浮点类型。映射到数据库中是float类型，占据32位，超过之后产生精度丢失。

（3）Double：双精度浮点类型。映射到数据库中是double类型，占据64位，超过之后产生精度丢失。

（4）Boolean：传递True和False进去

（5）DECIMAL：定点类型。解决浮点类型精度丢失问题，存什么就保存什么，在使用的时需要传递两个参数，第一个参数表示总共有多少位，第二位表示小数点后面有几位。

（6）Date：存储时间。只能存储年月日，映射到数据库中是date类型，在python中可以datetime.date()指定

（7）DateTime：只能存储年月日年月日，映射到数据库中是datetime类型，在python中可datetime.datetime()指定

（8）Time：传递datetime.time()（时分秒／微秒）

（9）String：字符串类型，使用时需要指定长度，区别于Text类型

（10）Text：文本类型（最多6万字符，对应Mysql中的Text）

（11）LONGTEXT：长文本类型(from sqlalchemy.dialects.mysql import LONGTEXT)

（12）enum：枚举类型。以后只能存枚举出的具体数值到数据库中，否则报错。

```python
class TagEnum(enum.Enum):
    flask = 'flask'
    django = 'django'
    tonado = 'tonado'
    
    
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float)
    is_delete = Column(Boolean)
    # article = Article(10, 21.12121, is_delete=True)
    price_full = Column(DECIMAL(10, 4))
    tag = Column(Enum('flask', 'django', 'Tonado'))
    frame = Column(Enum(TagEnum))
  
article = Article(10, 21.12121, is_delete=True, 'flask',TagEnum.flask)
```



#### 课时52【Column常用参数】

（1）default：默认参数

（2）nullable:是否可空(True:可为空，False：不可为空)

（3）primary_key：是否是主键

（4）unique：是否唯一，默认是False

（5）autoincrement：是否自动增长

（6）onupdate：更新的时候执行的函数。当数据有更新的时候，会调用这个参数的值或者对应的函数。当第一次插入数据的时候，不会使用update的值而是使用默认值。

（7）name：该属性在数据中的字段映射。指定ORM中的属性作为数据库中的字段名，如果有些属性在定义的时候，不希望是定义时候的那个名字，就可以添加name参数。

```python
from sqlalchemy import create_engine, Column, String, Integer,DECIMAL,DateTime,Time,Date,Text,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


HOSTNAME = '192.168.31.47'
PORT = '3306'
DATABASE = 'demo_test'
USERNAME = 'root'
PASSWORD = 'root'


DB_URI = 'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'.format(username=USERNAME, password=PASSWORD, hostname=HOSTNAME, port=PORT, database=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)


class Article(Base):
    __tablename__ = 'article04'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    read_count = Column(Integer, default=100)
    title = Column(String(20), nullable=False)
    author = Column(String(25), nullable=False)
    price = Column(DECIMAL(4,2))
    create_time = Column(DateTime)
    last_modify = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    is_delete = Column(Boolean)
    telephone = Column(String(11), unique=True)
    detail = Column(Text)


article1 = Article(title='title01', author='xia01', price=12.245, create_time=datetime.now(), last_modify=datetime.now(),is_delete=False, telephone='18565709397',detail='good good study')

article2 = Article(title='title02', author='xia02', price=13.245, create_time=datetime.now(), last_modify=datetime.now(),is_delete=False, telephone='18565709396',detail='good good study')

article3 = Article(title='title03', author='xia03', price=14.245, create_time=datetime.now(), last_modify=datetime.now(),is_delete=False, telephone='18565709395',detail='good good study')

session = sessionmaker(engine)()
Base.metadata.create_all()
session.add_all([article1,article2,article3])
session.commit()
```

补充知识点：Python中的datetime和time模块

```python
#1、datetime模块
#datatime模块重新封装了time模块，提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo
from datetime import date,time,datetime,timedelta,tzinfo

#（1-1）date类,表示日期的类。常用的属性有year, month, day
datetime.date(year, month, day)
#year的范围是[MINYEAR, MAXYEAR]，即[1, 9999]；
#month的范围是[1, 12]。（月份是从1开始的，不是从0开始的_）；
#day的最大值根据给定的year, month参数来决定。例如闰年2月份有29天；

#（1-2）time类,表示时间的类，由时、分、秒以及微秒组成。常用的属性有hour, minute, second, microsecond
'''各参数的意义不作解释，这里留意一下参数tzinfo，它表示时区信息。注意一下各参数的取值范围：hour的范围为[0, 24)，minute的范围为[0, 60)，second的范围为[0, 60)，microsecond的范围为[0, 1000000)
'''
datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ])

#（1-3）datetime类。datetime是date与time的结合体，包括date与time的所有信息
datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] 
#返回一个表示当前本地时间的datetime对象
datetime.today()
#返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间                  
datetime.now([tz])
#获取当前时间
now = datetime.now()
print(now)                   
#获取指定时间
dt = datetime(2018, 12, 30, 11, 24)
print(dt)

#（1-4）timedelta类，表示时间间隔，即两个时间点之间的长度。使用timedelta可以很方便的在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算，如果要计算月份则需要另外的办法。
#日期减一天
dt1 = dt + timedelta(days=-1)#昨天
dt2 = dt - timedelta(days=1)#昨天
dt3 = dt + timedelta(days=1)#明天
delta_obj = dt3 - dt
print (type(delta_obj),delta_obj)#<type 'datetime.timedelta'> 1 day, 0:00:00
print (delta_obj.days ,delta_obj.total_seconds())#1 86400.0

#datetime转换为时间戳
print(dt.timestamp())
#根据给定的时间戮，返回一个date对象
date.fromtimestamp(timestamp)

#将用户输入的str转换为datetime
'''
%a	本地（locale）简化星期名称	 
%A	本地完整星期名称	 
%b	本地简化月份名称	 
%B	本地完整月份名称	 
%c	本地相应的日期和时间表示	 
%d	一个月中的第几天(01 - 31)
'''
print(datetime.strptime('2018-12-30 18:19:59', '%Y-%m-%d %H:%M:%S'))
#将用户输入的datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))


#返回两个时间的时间差
print((now - dt).total_seconds())
                   
#2 time模块
print(time.gmtime())
print(time.localtime()) #当前时间返回的是一个time.struct_time 对象
print(time.time()) #返回的是当前时间的时间戳
localtime = time.localtime()
print("tm_gmtoff={}".format(localtime.tm_gmtoff))

print("tm_hour={}".format(localtime.tm_hour))  #时

print("tm_isdst={}".format(localtime.tm_isdst)) #是否夏令时

print("tm_mday={}".format(localtime.tm_mday)) #ri

print("tm_min={}".format(localtime.tm_min)) #分

print("tm_mon={}".format(localtime.tm_mon)) #月

print("tm_sec={}".format(localtime.tm_sec)) #秒

print("tm_wday={}".format(localtime.tm_wday)) #周几

print("tm_yday={}".format(localtime.tm_yday)) #一年中的第几天

print("tm_year={}".format(localtime.tm_year)) #年

print("tm_zone={}".format(localtime.tm_zone))

ts = time.mktime(localtime) #通过给定的时间得到时间戳
print(ts)

#格式化输出时间
print(time.strftime("%Y/%m/%d",localtime)) # 返回的是时间字符串
timeStr = "2017-08-05 23:00:00"
print(time.strptime(timeStr,"%Y-%m-%d %X")) #返回的是一个time.struct_time 对象

```



#### 课时53【query函数的参数】

```python
#1、模型对象，指定查找这个模型的所有属性查找出来。
result = session.query(Article).all()
for article in result:
    print(article)
    
#2、模型中的属性。可以指定只查找模型中的部分属性，将要查找的属性组成元祖的形式返回。
result = session.query(Article.id, Article.price, Article.telephone).all()
for article in result:
    print(article)
    
#3、聚合函数
result1 = session.query(func.count(Article.id)).all()
print(result1)
result2 = session.query(func.sum(Article.price)).all()
print(result2)
result3 = session.query(func.avg(Article.price)).all()
print(result3)
result4 = session.query(func.max(Article.price)).all()
print(result4)
result5 = session.query(func.min(Article.price)).all()
print(result5)


'''完整实例代码'''
from sqlalchemy import create_engine, Column, String, Integer,DECIMAL,DateTime,Time,Date,Text,Boolean,func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

HOSTNAME = '192.168.31.47'
PORT = '3306'
DATABASE = 'demo_test'
USERNAME = 'root'
PASSWORD = 'root'


DB_URI = 'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'.format(username=USERNAME, password=PASSWORD, hostname=HOSTNAME, port=PORT, database=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)


class Article(Base):
    __tablename__ = 'article04'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    read_count = Column(Integer, default=100)
    title = Column(String(20), nullable=False)
    author = Column(String(25), nullable=False)
    price = Column(DECIMAL(4,2))
    create_time = Column(DateTime)
    last_modify = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    is_delete = Column(Boolean)
    telephone = Column(String(11), unique=True)
    detail = Column(Text)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

#query可用参数
#1、模型对象，指定查找这个模型的所有属性
result = session.query(Article).all()
for article in result:
    print(article)

#2、模型中的属性。可以指定只查找模型中的部分属性
result = session.query(Article.id, Article.price, Article.telephone).all()
for article in result:
    print(article)

#3、聚合函数
result1 = session.query(func.count(Article.id)).first()
print(result1)
result2 = session.query(func.sum(Article.price)).first()
print(result2)
result3 = session.query(func.avg(Article.price)).first()
print(result3)
result4 = session.query(func.max(Article.price)).first()
print(result4)
result5 = session.query(func.min(Article.price)).first()
print(result5)
```



#### 课时54【filter常用到的过滤条件】

```python
from sqlalchemy import create_engine, Column, String, Integer,DECIMAL,DateTime,Time,Date,Text,Boolean,func, and_,or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

HOSTNAME = '192.168.31.47'
PORT = '3306'
DATABASE = 'demo_test'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = 'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'.format(username=USERNAME, password=PASSWORD, hostname=HOSTNAME, port=PORT, database=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)


class Article(Base):
    __tablename__ = 'article04'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    read_count = Column(Integer, default=100)
    title = Column(String(20), nullable=False)
    author = Column(String(25), nullable=False)
    price = Column(DECIMAL(4,2))
    create_time = Column(DateTime)
    last_modify = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    is_delete = Column(Boolean)
    telephone = Column(String(11), unique=True)
    detail = Column(Text)
    pub_author = Column(String(20), nullable=True)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

#equal
result_01 = session.query(Article).filter(Article.id == 2).all()
#print(session.query(Article).filter(Article.id == 2))
#print(result_01)

#not equal
result_02 = session.query(Article).filter(Article.id != 2).all()
#print(session.query(Article).filter(Article.id != 2))
#print(result_02)

#like
result_03 = session.query(Article).filter(Article.author.like('xia%')).all()
# print(result_03)
# print(session.query(Article).filter(Article.author.like('xia%')))

#and
result_04 = session.query(Article).filter(and_(Article.id == 1, Article.title == 'title01')).all()
# print(result_04)
# print(session.query(Article).filter(and_(Article.id == 1, Article.id == 2)))

#in,需要有个下划线。这是因为in是python的一个关键字，所以避免使用关键字in_
result_05 = session.query(Article).filter(Article.id.in_([1,2])).all()
print(result_05)

#not in(也可以使用~Article.id.in_)
result_06 = session.query(Article).filter(Article.id.notin_([1,2])).all()
print(result_06)

#is null
result_07 = session.query(Article).filter(Article.pub_author == None).all()
print(result_07)

#is not null
result_08 = session.query(Article).filter(Article.pub_author != None).all()
print(result_08)

#or
result_09 = session.query(Article).filter(or_(Article.id == 1, Article.author == 'xia03')).all()
print(result_09)
```



#### 课时55【外键及四种约束】

之前讲的都是一张表的，现在看下多张表之间操作的。SQLAlchemy中通过ForeignKey通过外键实现多表之间的关联

```python
from sqlalchemy import create_engine, Column, String, Integer,DECIMAL,DateTime,Time,Date,Text,Boolean,func, and_,or_, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

HOSTNAME = '192.168.31.47'
PORT = '3306'
DATABASE = 'sqlalchemy_demo'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = 'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'.format(username=USERNAME, password=PASSWORD, hostname=HOSTNAME, port=PORT, database=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    age = Column(Integer, default=25)
    sex = Column(Enum('Male', 'Femal', 'Other'))
    hobby = Column(String(20), nullable=True)
    birthday = Column(DateTime, nullable=True)

class Article(Base):
    __tablename__ = 'article'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    read_count = Column(Integer, default=100)
    title = Column(String(20), nullable=False)
    author = Column(String(25), nullable=False)
    price = Column(DECIMAL(4,2))
    create_time = Column(DateTime)
    last_modify = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    is_delete = Column(Boolean)
    telephone = Column(String(11), unique=True)
    detail = Column(Text)
    pub_author = Column(String(20), nullable=True)
	'''uid是外键，外键的数据类型必须和所引用的父表的主键的那个字段的数据类型保持一致'''
    uid = Column(Integer, ForeignKey('user.id', ondelete='Restrict'))


session = sessionmaker(engine)()
Base.metadata.drop_all()
Base.metadata.create_all()

date1 = datetime(2017, 9, 29,10,34,5)
date2 = datetime(2015, 9, 29,12,23,45)
user = User(name='xia01', sex='Male', hobby='PingPong', birthday=date1)
session.add(user)
session.commit()

'''ForeignKey的约束条件'''
1、Restrict：默认。父表中的数据删除，会阻止删除该数据
2、NO CATION：Mysql中同上
3、Cascade：集联删除。父表中的数据删除，从表中的数据也跟着删除
4、SET Null：父表中的数据删除，从表中的数据相应设置为空

```



#### 课时56【ORM模型和一对多的关系】

```python
from sqlalchemy import create_engine, Column, String, Integer,DECIMAL,DateTime,Time,Date,Text,Boolean,func, and_,or_, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

HOSTNAME = '192.168.31.47'
PORT = '3306'
DATABASE = 'sqlalchemy_demo'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = 'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'.format(username=USERNAME, password=PASSWORD, hostname=HOSTNAME, port=PORT, database=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    age = Column(Integer, default=25)
    sex = Column(Enum('Male', 'Femal', 'Other'))
    hobby = Column(String(20), nullable=True)
    birthday = Column(DateTime, nullable=True)
    articles = relationship('Article')


class Article(Base):
    __tablename__ = 'article'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    read_count = Column(Integer, default=100)
    title = Column(String(20), nullable=False)
    author = Column(String(25), nullable=False)
    price = Column(DECIMAL(4,2))
    create_time = Column(DateTime)
    last_modify = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    is_delete = Column(Boolean)
    telephone = Column(String(11), unique=True)
    detail = Column(Text)
    pub_author = Column(String(20), nullable=True)
    uid = Column(Integer, ForeignKey('user.id', ondelete='Restrict'))
    
    author = relationship('User', backref='articles')


session = sessionmaker(engine)()
# Base.metadata.drop_all()
# Base.metadata.create_all()
'''没有使用relationship之前'''
article = session.query(Article).first()
uid = article.uid
user = session.query(User).get(uid)

'''使用relationship之后'''
article = session.query(Article).first()
print(article.author)

```



#### 课时57【一对一关系映射】

```python
'''【一对多】关系的数据操作'''
#1、现在有一个用户两篇文章【一对多】，如果要将文章都添加到该用户上面，如何操作？
user = User()
article1 = Article()
article2 = Article()
user.articles.append(article1)
user.articles.append(article2)
session.add(user)
session.commit()

#2、现在只有一个用户，一篇文章，只想把这个作者添加到这篇文章上面
user = User()
article = Article()
article.author = user
session.add(article)
session.commit()
```

随着网站的发展，用户越来越多，用户表的字段越来越多。但是现在，比如有些用户信息是不经常用的，如果每次使用都全部查询，自然会影响到数据库性能，因此可以再另外使用一张表来存放一些不经常使用的用户扩展信息。此时，用户扩展信息表和用户信息表之间的关系就是一对一的关系。我们在使用的时候，通过加入uselist=False可以指定个一对一关系。author = relationship('User', backref=backref('User',uselist=False))



#### 课时58【多对多关系映射】

```python
from sqlalchemy import create_engine, Column, String, Integer,DECIMAL,DateTime,Time,Date,Text,Boolean,func, and_,or_, Enum, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship,backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

HOSTNAME = '192.168.31.47'
PORT = '3306'
DATABASE = 'sqlalchemy_demo'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = 'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'.format(username=USERNAME, password=PASSWORD, hostname=HOSTNAME, port=PORT, database=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)


class Article(Base):
    __tablename__ = 'article'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    read_count = Column(Integer, default=100)
    title = Column(String(20), nullable=False)
    author = Column(String(25), nullable=False)
    price = Column(DECIMAL(4,2))
    create_time = Column(DateTime)
    last_modify = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    is_delete = Column(Boolean)
    telephone = Column(String(11), unique=True)
    detail = Column(Text)
    pub_author = Column(String(20), nullable=True)
    uid = Column(Integer, ForeignKey('user.id', ondelete='Restrict'))
    #author = relationship('User', backref='articles')
    author = relationship('User', backref=backref('Article',uselist=False))
    tags = relationship("Tag", backref="articles",secondary=article_tag)


article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id",Integer, ForeignKey('article.id'), primary_key=True),
    Column("tag_id",Integer, ForeignKey('tag.id'), primary_key=True)
)

```

总结：

​	1、先把两个需要做多对多的模型定义出来；

​	2、使用table定义一个中间表，中间表一般就是包含两个模型的外键字段就可以了，并且让它作为一个联合主键

​	3、在两个需要做多对多的模型中随便选择一个模型定义一个relationship属性来绑定三者之间的关系，需要传入一个secondary=中间表



#### 课时59【Flask数据库操作】ORM模型删除数据注意事项

可以正常删主表中的数据：首先会将从表中的关联字段设置为null，然后在将主表中的数据删除掉。

如果也想ORM中无法删除掉数据，那就需要将从表中的关联字段不能为空（nullable=false）



#### 课时60【Flask数据库操作】ORM模型中的cascade

在SQLAlchemy中，只要将数据添加到一个session中，和它相关联的数据都会保存到相应的数据库表中。这是在你们设置的？其实就是在创建关联的时候，relationship有一个字段cascade可以设置相关的参数值。

（1）save-update:默认选项。在添加一条数据的时候，会把他和它相关连的数据都添加到数据库中。

（2）delete：表示删除某个模型中的数据的时候，也删除与之相关联的其他表中的数据。

（3）





#### 课时62【Flask数据库操作】三种排序详解

1、order_by ：可以指定根据表中的某个字段进行排序。如果在前面加个“-”表示是倒序。

```
session.query(Article).order_by(Article.create_time).all()
```

 2、在定义模型的时候，指定默认排序：有时候不希望在每次查找的时候都设置排序规则，那么可以在定义模型的时候指定按照某个字段排序规则，这个时候有两种方式：

（1）给relationship指定order_by参数

（2）在定义模型的时候加如下代码：

__mapper_args__ = {

​	"order_by":create_time

}





#### 课时76【WTForms】WTForms表单验证基本使用

WTForms这个库有两个作用：（1）验证用户提交数据的合法性；（2）渲染模版

```python
'''没有WTForms的时候表单验证是这样的：'''
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        password_repeat = request.form.get('password_repeat')
        if len(username) < 3 or len(username) < 10:
            return "用户名长度不正确"
        if len(password) < 6 or len(password) > 10:
            return "用户名密码不正确"
        if password != password_repeat:
            return "两次输入的密码不一致"
            
            
if __name__ == '__main__':
    app.run(debug=True)


```

使用WTForms的做表单验证的基本步骤：

1、自定义一个表单类，继承自wtform.Form类

2、定义好需要验证的字段，字段名称必须和模版中的那些需要验证的input标签的name属性值保持一致

3、在需要验证的字段上，需要指定好具体的数据类型

4、在相关的字段上，指定验证器

5、以后在视图中，就需要使用这个表单类的对象，并且把需要验证的数据，也就是request.form传递给这个表单类[form = RegistForm(request.form)]。然后调用form.validate()方法。如果返回True，那么代表用户输入的是合法，否则代表用户的数据有问题。如果验证失败，可以通过form.errors来获取错误信息。

```python
'''使用WTForms的时候表单验证是这样的：'''
from flask import Flask, render_template, request
from wtforms import Form, StringField
from wtforms.validators import Length, EqualTo

class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message="用户名长度必须在3-10位之间")])
    password = StringField(validators=[Length(min=6, max=10, message="密码长度必须在6-10位之间")])
    password_repeat = StringField(validators=[Length(min=6, max=10, message="两次输入的密码不一致"), EqualTo("password")])

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        form = RegistForm(request.form)
        if form.validate():
            return "注册成功"
        else:
            print(form.errors)
            return "注册失败"

if __name__ == '__main__':
    app.run(debug=True)


```



#### 课时77【WTForms】WTForms常用的验证器

数据发过来，经过表单验证，因此需要验证器来进行验证，以下对一些常用的验证器进行讲解：

Email：验证上传的数据是否是邮箱；

EqualTo：验证上传的数据是否与另一个字段相等，常用的就是密码和确认密码两个字段是否相等；

InputRequired：(字段必须传值)原始数据的需要验证,需要输入验证。如果不是特殊情况，应该使用InputRequired。

Length：长度限制，有min和Max两个值限制，如果处在着两个数字之间则满足。

NumberRange：数字区间，有min和max两个值限制，如果处在这两个数字区间则满足。

Regerp：自定义正则表达式。

URL：必须是URL的形式。

UUID：验证UUID。

```python
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, EqualTo, Email, InputRequired, NumberRange, Regexp, URL, UUID
#from uuid import UUID

class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message="用户名长度必须在3-10位之间")])
    password = StringField(validators=[Length(min=6, max=10)])
    password_repeat = StringField(validators=[Length(min=3, max=10), EqualTo("password")])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[InputRequired()])
    age = IntegerField(validators=[NumberRange(12, 100)])
    phone = StringField(validators=[Regexp(r'1[3587]\d{9}')])
    home_page = StringField(validators=[URL()])
    uuid = StringField(validators=[UUID()])
    
```



#### 课时78【WTForms】自定义表单验证器

如果像鬼表单中某一个字段进行更加细化的验证，那么需要针对这个字段进行单独验证。步骤如下：

1、定义一个方法，方法名规则是：validate_字段名(self, field)

2、在方法中，使用 field.data可以获取到该字段的具体值

3、如果满足条件，可以什么都不做，如果不满足条件那么抛出一个wtforms.validators.ValidataError的异常，并把验证的失败信息传递到这个异常类中。

如下自定义验证码验证器（captcha）

```python
from wtforms import Form, StringField, IntegerField, ValidationError
from wtforms.validators import Length, EqualTo, Email, InputRequired, NumberRange, Regexp, URL, UUID
#from uuid import UUID

class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message="用户名长度必须在3-10位之间")])
    password = StringField(validators=[Length(min=6, max=10)])
    password_repeat = StringField(validators=[Length(min=3, max=10), EqualTo("password")])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[InputRequired()])
    age = IntegerField(validators=[NumberRange(12, 100)])
    phone = StringField(validators=[Regexp(r'1[3587]\d{9}')])
    home_page = StringField(validators=[URL()])
    uuid = StringField(validators=[UUID()])
    captcha = StringField(validators=[Length(4, 4)])
    def validate_captcha(self, field):
        # print(field.data)
        if field.data != '1234':
            raise ValidationError("验证码错误")

```



#### 课时79【WTForms】使用WTForms渲染模版

```python
from wtforms import Form, StringField, IntegerField, ValidationError, BooleanField, SelectField
from wtforms.validators import Length, EqualTo, Email, InputRequired, NumberRange, Regexp, URL, UUID
#from uuid import UUID

class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message="用户名长度必须在3-10位之间")])
    password = StringField(validators=[Length(min=6, max=10)])
    password_repeat = StringField(validators=[Length(min=3, max=10), EqualTo("password")])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[InputRequired()])
    age = IntegerField(validators=[NumberRange(12, 100)])
    phone = StringField(validators=[Regexp(r'1[3587]\d{9}')])
    home_page = StringField(validators=[URL()])
    #uuid = StringField(validators=[UUID()])
    #captcha = StringField(validators=[Length(4, 4)])
    def validate_captcha(self, field):
        # print(field.data)
        if field.data != '1234':
            raise ValidationError("验证码错误")


class SettingForm(Form):
    username = StringField("用户名", validators=[InputRequired()])
    age = IntegerField("年龄", validators=[NumberRange(12, 100)])
    remember = BooleanField('记住我：')
    tags = SelectField("标签", choices=[('1','Python'),('2','Java'),('3','SQL')])
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Settings_Page</title>
</head>
<body>
    <form action="" method="POST">
        <table>
            <tr>
                <td>{{ form.username.label }}</td>
                <td>{{ form.username}}</td>
            </tr>
            <tr>
                <td>{{ form.age.label }}</td>
                <td>{{ form.age}}</td>
            </tr>
            <tr>
                <td>{{ form.remember.label }}</td>
                <td>{{ form.remember}}</td>
            </tr>
            <tr>
                <td>{{ form.tags.label }}</td>
                <td>{{ form.tags}}</td>
            </tr>
        </table>
    </form>

</body>
</html>
```



#### 课时80【Flask文件上传】上传文件以及访问文件的上传

1、在模版的使用form表单中，需要指定enctype="multipart/form-data"才能上传文件；

2、在后台如果想要获取到上传的文件，那么应该使用request.files.get('avatar')来获取；

3、保存文件之前，先使用secure_filename(avatar.filename)来对上传的文件的名字做一个过滤，这样才能保证不会有安全问题；

4、获取上传的文件后，使用avatar.save(os.path.join(UPLOAD_PATH, filename))来保存文件；

5、从服务器获取文件，应该使用send_from_directory(文件目录，文件名)

```python
from flask import Flask, request, render_template, send_from_directory
from forms import RegistForm, LoginForm, SettingForm
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/', methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "Success"
        else:
            print(form.errors)
            return "Fail"


@app.route('/setting/', methods=['GET', 'POST'])
def Setting():
    if request.method == "GET":
        form = SettingForm()
        return render_template('settings.html', form=form)


@app.route('/upload/', methods=['GET', 'POST'])
def Upload():
    if request.method == "GET":
        return render_template("upload_file.html")
    else:
        desc = request.form.get('desc')#获取描述信息
        avatar = request.files.get('avatar')
        filename = secure_filename(avatar.filename)
        avatar.save(os.path.join(UPLOAD_PATH, filename))
        return "文件上传成功"

if __name__ == '__main__':
    app.run(debug=True)

```



#### 课时81【Flask文件上传】使用flask_wtf验证上传的文件

1、定义表单验证的时候，需要使用FileField

2、验证器需要从flask_wtf.file  中倒入file_required, file_allowed

3、如果想要获取form表单中的多种类型的字段值，需要使用from werkzeug.datastructures import CombinedMultiDict 

```python
from flask_wtf.file import file_required, file_allowed

class UploadForm(Form):
    avatar = FileField(validators=[file_required(), file_allowed(['jpg', 'gif', 'png'])])
    desc = StringField(validators=[InputRequired()])

@app.route('/upload/', methods=['GET', 'POST'])
def Upload():
    if request.method == "GET":
        return render_template("upload_file.html")
    else:
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            desc = request.form.get('desc')#获取描述信息
            avatar = request.files.get('avatar')
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(UPLOAD_PATH, filename))
            print(desc)
            return "文件上传成功"
        else:
            print(form.errors)
            return "Failed"

```



#### 课时82【Flask Cookie】cookie的基本概念

1、cookie：在网站中，http是无状态的。也就是说即使第一次连接服务器后并且成功登录之后，第二次请求服务器依然不能知道当前请求是哪一个用户。cookie的出现就是为了解决这个问题，第一次登录服务器返回一些数据（cookie）给到浏览器，然后浏览器保存到本地，当用户发送第二个请求的时候，会自动的把上一次请求存储的cookie数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前的用户是哪一个了。cookie存储的数据量有限，不同的浏览器有不同的存储大小，但一般不超过4kb。因此使用cookie只能存储一些小量的数据 。	cookie的有效期；cookie的域名；

#### 课时83【Flask Cookie】Flask设置和操作cookie

设置cookie需要在Response对象上设置（flask.Response）

```python
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    resp = Response("知了课堂")
    resp.set_cookie('username','xia_m_lin',max_age=10)
    resp.set_cookie('age','18', max_age=10)
    return resp

@app.route('/del/')
def del_cookie():
    resp = Response("删除cookie")
    #删除cookie
    resp.delete_cookie('username')
    return resp

if __name__ == '__main__':
    app.run(debug=True)


```

#### 课时84【Flask Cookie】设置cookie的有效期（过期时间）

```python
@app.route('/')
def hello_world():
    resp = Response("知了课堂")
    resp.set_cookie('username','xia_m_lin',max_age=10)
    expires = datetime(year=2019, month=2, day=5, hour=0, minute=30, second=0)
    resp.set_cookie('age','18', expires=expires)
    return resp
'''
(1)expires参数使用的是格林尼治时间，如果我们要使用的话，需要在时间上减少8个小时
(2)如果同时设置了expires和max_age,那么将会以max_age作为标准
(3)expires接收的参数是datetime类型
(4)如果expires和max_age那么cookie的过期时间是关闭浏览器就是失效
'''
```

#### 课时85 【Flask Cookie】设置cookie的有效域名

```python
@app.route('/')
def hello_world():
    resp = Response("知了课堂")
    resp.set_cookie('username','xia_m_lin',max_age=10, domain='.hy.com')
    expires = datetime(year=2019, month=2, day=5, hour=0, minute=30, second=0)
    resp.set_cookie('age','18', expires=expires)
    return resp
```

#### 课时86【Flask Session】session的基本概念

1、session：session与cookie的作用有点类似，都是为了存储用户相关的信息。不同的是，cookie是存储在本地浏览器，session是存储在服务器。session 是一个概念，一个思路，一个服务器授权解决方案，不同的服务器，不同的框架，不同的语言有不同的实现。虽然实现不一样，但是他们的目的是都是服务器为了方便存储数据的。session的出现是为了解决cookie存储数据的不安全的问题。

2、session与cookie的结合使用：（1）session存储在服务器端：服务器端可以使用mysql、redis、memached等存储session信息。原理是，客户端发送验证信息过来（比如用户名和密码），服务器验证成功后，把用户的相关信息存储到sesion中，随机生成一个唯一的session_id,再把这个sesion_id存储到cookie中返回给浏览器。浏览器以后再请求我们的服务器时，就会把这个session_id自动的发送给服务器，服务器再把cookie中session_id 取出来，然后从服务器的session中找到这个用户的相关信息，这样就达到安全识别用户信息的目的。（2）session存储到客户端：客户端发送验证信息过来，服务器把相关验证信息进行一个严格的加密，然后把这个加密信息存储到cookie，返回给客户端。客户端再请求服务器的时候，会自动把cookie发送给服务器，服务器拿到cookie之后，就从cookie中找到加密的那个session信息，然后也就可以实现安全认证。

#### 课时87【Flask Session】Flask操作session

1、设置session：通过flask.session就可以操作session了，操作session就跟操作字典一样session['username']='zhiliao'

2、获取session：通过session.get(key)来获取

3、删除sesion中的值：可以使用3种方式来删除（1）session.pop(key) (2)sesión.clear()可以删除所有的session (3)del session[key]

4、设置session的有效期：如果没有设置session的有效期，那么默认关闭浏览器后过期；如果设置session.permanent = True，那么就是默认保存31天；如果设置app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)就可以按照设置的时长保存；

```python
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

```

#### 课时88【CSRF攻击与防御】CSRF的原理

CSRF攻击概述：CSRF（cross site request forgery 跨站请求伪造）是一种网路的攻击方式。网站是通过cookie来实现登录功能的，而cookie只要存在于浏览器中，只要浏览器在访问这个cookie的服务器的时候，就会自动的携带cookie信息到服务器上去。那么这个时候就存在一个漏洞，如果你访问了一个别有用心或有病毒的网站，这个网站可以在网页源代码中插入js代码，使用js代码给其他服务器发送请求。那么因为在发送请求的时候，浏览器自动的把cookie发送给对应的服务器，这个时候相应的服务器就不知道这个请求是伪造的，就会被欺骗过去了。从而达到在用户不知情的情况下，给某个服务器发送了请求。

#### 课时89【CSRF攻击与防御】实战项目--中国工商银行注册功能完成

防御CSRF攻击：CSRF攻击的要点就是在服务器发送请求









#### 课时92【CSRF攻击与防御】CSRF防御原理

1、用户访问工商银行网站进行登录，登录后工商银行相应的cookie信息；										2、用户访问转账页面，工商银行在返回页面之前会做两件事：（1）在cookie中添加成csrf_token（2）在body中（表单页面）中添加一个input标签，input标签中含有相同的csrf_token值，然后返回									3、用户在发送转账的请求，此时带有csrf_token值的input标签也会被一同提交到服务器							4、而js代码无法操作其它域名下的cookie（浏览器做了一层限制）



#### 课时93【CSRF攻击与防御】Flask中CSRF防御的方法和原理

```python

import config
from flask_wtf import CSRFProtect


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
CSRFProtect(app)


<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
```



#### 课时94【CSRF攻击与防御】AJAX处理CSRF漏洞

在AJAX中使用csrf保护，则必须手动添加X-CSRFToken到Header中。但是CSRF从哪里来，还是需要通过模版来渲染，而Flask比较推荐的方式是在meta标签中渲染CSRF，如下：

```html
<meta name="csrf-token" content="{{ csrf_token() }}">
```



#### 课时103【Flask Restful】Restful API 规范介绍

Restful_api是用在前端于后台进行通信的一套规范。使用这个规范可以让前后端开发更加轻松。

协议：采用http和https协议

数据传输：数据之间传输的格式应该都是用json而不是xml

URL连接：URL链接中，不能有动词，只能有名词。并且对于一些名词，如果出现重复，那么应该在后面s。比如：获取文章列表，应该使用'/articles/',而不是使用'/get_article/'

http请求的方法：																					1、get：从服务器获取资源，而不会对服务器的资源造成影响；												2、post：在服务器上新创建一个资源；																	3、put：在服务器上更新一个资源（客户端提供所有改变后的数据）；											4、patch：在服务器上更新资源（客户端只提供需要改变的属性）；											5、delete：从服务器上删除资源

示例如下：																				GET/user/ 	获取所有用户																			POST/user/ 	新增一个用户																			PUT/user/id/ 	更新一个用户的信息（需要提供用户的所有信息）																		PATCH/user/id/ 	更新一个用户的信息（只需要提供需要更改的信息）																			DELETE/user/id/	删除一个用户

状态码：

#### 课时104【Flask Restful】Flask-Restful插件的基本使用

定义Restful的视图：

如果使用Flask-Restful，那么定义视图函数的时候，就要继承Flask-Restful.Resource类，然后再根据当前请求的method来定义相应的方法。比如期望客户端是使用get()方法发送过来的请求，那么就定义一个get方法。类似于MethodView。其中（1）Api：用来绑定我们的app，并且生成api的对象；（2）Resource：用来创建视图

```python
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class LoginView(Resource):

    def post(self):
        return "username"


api.add_resource(LoginView, '/login/', endpoint='Login')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
'''注意事项：
（1）endpoint 是用来给url_for反转url的时候使用的【url_for（'Login'）】。如果不指定endpoint，那么将会使用视图函数名字的小写字母来作为endpoint【url_for（'loginview'）】

（2）add_resource的第二个参数是访问这个视图函数的URL，这个URL跟以前的route一样，可以传递参数。并且还有一点不同的就是，这个方法可以传递多个url来指定这个视图函数'''
```

