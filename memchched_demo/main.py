import memcache


mc = memcache.Client(["192.168.0.27:11211"],debug=True)

#通过代码的形式设置一个值
mc.set('name','xmlin',time=120)

#一次性设置多个值
mc.set_multi({"title":"xia", "author":"yeyanmei","tags":"励志"}, time=120)

#获取一个值
username = mc.get('name')
print(username)

#删除数据
username = mc.get('name')
print(username)
mc.delete('name')
username = mc.get('name')
print(username)

#自增长
mc.incr('age',delta=10)
age = mc.get('age')
print(age)

#自减少
mc.decr('age', delta=100)
age = mc.get('age')
print(age)