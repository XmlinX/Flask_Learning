from sqlalchemy import create_engine, Column, String, Integer,DECIMAL,DateTime,Time,Date,Text,Boolean,func, and_,or_, Enum, ForeignKey
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


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    age = Column(Integer, default=25)
    sex = Column(Enum('Male', 'Femal', 'Other'))
    hobby = Column(String(20), nullable=True)
    birthday = Column(DateTime, nullable=True)
    #articles = relationship('Article')


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




session = sessionmaker(engine)()
#现在有一个用户，两篇文章
user = User()
article1 = Article()
article2 = Article()

#1、如果要将文章都添加到该用户上面，如何操作？
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



