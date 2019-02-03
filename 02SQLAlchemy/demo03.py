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