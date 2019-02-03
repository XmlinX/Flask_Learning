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
sql2 = 'show tables'
sql3 = 'drop table b '
sql4 = 'create table student(id int primary key, name varchar (20), sex varchar (10))'
sql5 = 'alter table student add city varchar (20) not null '
sql6 = 'alter table student modify city varchar (30) not null '
sql7 = 'alter table student change city city_zone varchar (25) not null '

#使用with语句连接数据库，如果有异常会被捕获
with engine.connect() as  conn:
    result = conn.execute(sql7)
    #print(result.fetchall())


