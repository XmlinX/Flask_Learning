from sqlalchemy import create_engine, Column, String, Integer,DECIMAL,DateTime,Time,Date,Text,Boolean,func, and_,or_, Enum, ForeignKey, Table
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


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)


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
    tags = relationship("Tag", backref="articles",secondary=article_tag)


article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id",Integer, ForeignKey('article.id'), primary_key=True),
    Column("tag_id",Integer, ForeignKey('tag.id'), primary_key=True)
)




