from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
    __tablename__ = 'person'
    '''2、给这个ORM模型创建一些属性，来跟表中的字段进行一一对应，这些属性也必须是sqlalchemy给我们提供好的数据类型'''
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25))
    age = Column(Integer)
    country = Column(String(50))

    def __str__(self):
        return "<Person(name:%s, age:%s, country:%s)>" % (self.name, self.age, self.country)



#构建session对象，所有和数据库的ORM操作都必须通过一个叫session的会话对象来实现对数据的增删改查，
Session = sessionmaker(engine)
session = Session()
#增
def add_data():
    #初始化一个对象，实质就是创建一条数据
    #p = Person(name='xiameilin', age=18, country='wuhan')
    #将对象添加带session中
    #session.add(p)
    #session中的对象做commit操作
    #session.commit()
    '''添加多条数据'''
    p1 = Person(name='xiameilin002', age=19, country='shenzhen')
    p2 = Person(name='xiameilin003', age=20, country='guangzhou')
    session.add_all([p1, p2])
    session.commit()

#查
def search_data():
    #查找某个模型对应的表中所欲的数据
    # all_persons = session.query(Person).all()
    # for person in all_persons:
    #     print(person)
    # all_persons = session.query(Person).filter_by(name='xiameilin').all()
    # print(all_persons)
    # all_persons = session.query(Person).filter(Person.name).all()
    all_person = session.query(Person).get(1)
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


if __name__ == '__main__':
    #add_data()
    #search_data()
    #update_data()
    delete_data()