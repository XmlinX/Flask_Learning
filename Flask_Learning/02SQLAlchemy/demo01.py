from sqlalchemy import create_engine, Column, String, Integer,DECIMAL,DateTime,Time,Date,Text,Boolean
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


article1 = Article(title='title01', author='xia01', price=12.245, create_time=datetime.now(), last_modify=datetime.now(),is_delete=False, telephone='18565709397',detail='good good study')

article2 = Article(title='title02', author='xia02', price=13.245, create_time=datetime.now(), last_modify=datetime.now(),is_delete=False, telephone='18565709396',detail='good good study')

article3 = Article(title='title03', author='xia03', price=14.245, create_time=datetime.now(), last_modify=datetime.now(),is_delete=False, telephone='18565709395',detail='good good study')

session = sessionmaker(engine)()
Base.metadata.create_all()
#Base.metadata.drop_all()
session.add_all([article1,article2,article3])
session.commit()