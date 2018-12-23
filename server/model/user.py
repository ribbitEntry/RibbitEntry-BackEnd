from sqlalchemy import Column
from . import db


class User(db.Model):
    __tablename__ = 'user'

    id = Column(db.String(50), primary_key=True)
    pw = Column(db.String(50), nullable=False)
    nickname = Column(db.String(50), nullable=False)

    proimg = Column(db.String, default='')
    backimg = Column(db.String, default='')
    introduction = Column(db.String(100), default='소개를 작성해주세요.')

    follow_num = Column(db.String(10), default=0)
    follower_num = Column(db.String(10), default=0)