#datatime模块重新封装了time模块，提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo
from datetime import datetime,timedelta



#date类
datetime.date(year, month, day)
#获取当前时间
now = datetime.now()
print(now)



#time类
datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ])


#datetime类
#datetime相当于date和time结合起来。
datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )


#获取指定时间
dt = datetime(2018, 12, 30, 11, 24)
print(dt)
#timedelta类，时间加减
#使用timedelta可以很方便的在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算，如果要计算月份则需要另外的办法。
#日期减一天
dt1 = dt + timedelta(days=-1)#昨天
dt2 = dt - timedelta(days=1)#昨天
dt3 = dt + timedelta(days=1)#明天
delta_obj = dt3 - dt
print (type(delta_obj),delta_obj)#<type 'datetime.timedelta'> 1 day, 0:00:00
print (delta_obj.days ,delta_obj.total_seconds())#1 86400.0



#datetime转换为时间戳
print(dt.timestamp())

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