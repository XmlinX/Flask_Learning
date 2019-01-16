

### 章节1——Flask视图函数与url

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

    '''安装到Python2环境中'''
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



课时38【类视图】

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



课时40【类视图中使用装饰器】

​		

​	

​	

课时41【蓝图的基本使用】

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

​	（3将蓝图绑定url

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



课时42【蓝图中模版文件寻找规则】

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



课时46【flask数据库-MySQL以及注意事项】

​	设置root密码：root

课时47【SQLAlchemy介绍和基本使用】

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



课时48【Flask数据库-ORM介绍】对象关系映射（模型与表之间的映射）

O：Object 对象	R：Relationship  关系	M：mapping 映射

随着项目越来越大，采用写原声SQL的方式在代码中出现大量的SQL语句，那么问题就出现了：

​	1、SQL语句重复利用率不高，越复杂的SQL语句条件越多，代码越长，会出现很多相近的SQL的语句。

​	2、很多SQL语句是业务逻辑拼出来的，如果有数据库需要修改，就要去修改这些逻辑，这会很容易遗漏掉对某些SQL语句的修改。

​	3、写SQL时容易忽略web安全问题，给未来造成隐患。

```python
class Person(object):
    name = 'xxxx'
    age = 18
    country = 'xxxx'    
    
create table Person(name varchar(20) not null, age int default 18, country varchar(25) null)

'''可以作如下映射：
	1、Person类对应数据库中的表Person
	2、Person类属性对应数据库的字段
	3、Person实例化一个对象对比数据库中的一条数据'''
```



课时49【定义ORM模型并将其映射到数据库中】

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



课时50【使用SQLAlchemy完成数据库的增删改查】

```python
from sqlalchemy.orm import sessionmaker

#构建session对象，所有和数据库的ORM操作都必须通过一个叫session的会话对象来实现对数据的增删改查，
Session = sessionmaker(engine)
session = Session()

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
    
    #使用filter_by
    all_persons = session.query(Person).filter_by(name='xiameilin').all()
    print(all_persons)
    #使用filter
    all_persons = session.query(Person).filter(Person.name=='xiameilin').all()
    #使用get方法查找，只能根据主键查找
     all_person = session.query(Person).get(1)
    #使用first()查找第一条数据
    all_person = session.query(Person).first()
    
#改
def update_data():
    #要修改对象，首先要获取到该对象，然后修改对象对应的属性，最后通过commit进行提交
    person = session.query(Person).filter_by(name='xiameilin').first()
    person.name = 'yeyanmei'
    session.commit()
    
#删
def delete_data():
    person = session.query(Person).filter_by(name='yeyanmei').first()
    session.delete(person)
    session.commit()
```



课时51【SQLAlchemy属性常用数据类型详解】

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



课时52【Column常用参数】

（1）default：默认参数

（2）nullable:是否可空(True:可为空，False：不可为空)

（3）primary_key：是否是主键

（4）unique：是否唯一，默认是False

（5）autoincrement：是否自动增长

（6）onupdate：更新的时候执行的函数。当数据有更新的时候，会调用这个参数的值或者对应的函数。

（7）name：该属性在数据中的字段映射。指定ORM中的属性作为数据库中的字段名。如果有些属性在定义的时候，不希望是定义时候的那个名字，就可以添加name参数。

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



课时53【query函数的参数】

```python
#1、模型对象，指定查找这个模型的所有属性
result = session.query(Article).all()
for article in result:
    print(article)
    
#2、模型中的属性。可以指定只查找模型中的部分属性
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
```



课时54【filter常用到的过滤条件】

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

#in
result_05 = session.query(Article).filter(Article.id.in_([1,2])).all()
print(result_05)


#not in
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



课时55【外键及四种约束】

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



课时56【ORM模型和一对多的关系】

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

article = session.query(Article).filter().first()
print(article.author)

```



课时57【一对一关系映射】

```python
#现在有一个用户，两篇文章【一对多】
user = User()
article1 = Article()
article2 = Article()

#1、如果要将文章都添加到该用户上面，如何操作？
user.articles.append(article1)
user.articles.append(article2)
session.add(user)
session.commit()

#2、现在只有一个用户，一篇文章，只想把这个作者添加到这篇文章上面【一对一】
user = User()
article = Article()
article.author = user
session.add(article)
session.commit()
```

现在，比如有些用户信息是不经常用的，如果每次使用都全部查询，自然会影响到数据库性能，因此可以再另外使用一张表来存放一些不经常使用的用户扩展信息。此时，用户扩展信息表和用户信息表之间的关系就是一对一的关系。我们在使用的时候，通过加入uselist=False可以指定个一对一关系。author = relationship('User', backref=backref('User',uselist=False))