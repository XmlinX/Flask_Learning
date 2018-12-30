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