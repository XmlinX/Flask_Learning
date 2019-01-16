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

