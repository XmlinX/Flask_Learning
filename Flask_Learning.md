

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