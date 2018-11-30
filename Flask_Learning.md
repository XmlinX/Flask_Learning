#### 课时1 【虚拟环境】

##### 为什么需要使用虚拟环境？

到目前为主，我们所有的第三方包都是直接通过pip install 的方式安装的。这样安装会将那个包安装到我们系统级别的Python环境中。但是这样就有一个问题，如果你现在用Djiango 1.10.x写了个网站，然后你的领导跟你说，之前的旧项目是用Djiango 0.9开发的，让你维护，但是Djiango 0.9 和Djiango 1.10.x 相互不兼容。这时候就会碰到一个问题，我如何在我的电脑中同时拥有Djiango 0.9 和Djiango 1.10.x 两套环境呢？这时候我们发现可以通过虚拟环境来解决这个问题了。

##### 虚拟环境原理

 虚拟环境相当于一个抽屉，在这个抽屉中安装的任何软件包都不会影响其他抽屉。并且在项目中，我可以指定这个项目使用的虚拟环境来配合我的项目。比如我们现在有一个项目是基于Djiango 0.9 开发的，又有一个项目是基于Djiango 1.10.x 开发的。这个时候可以创建两个虚拟环境分别安装Djiango 0.9 和Djiango 1.10.x 来配合我们的项目。



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

URL与视图 + Jinja2模版 + SQLAlchemy框架 + Flask知识点补充 + msmcache缓存 + Redis 



#### 课时5【Flask预热】 

环境准备：

​	python 3.6 + pycharm 

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











