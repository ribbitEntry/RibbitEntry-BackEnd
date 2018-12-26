from sqlalchemy import Column

from server.extensions import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(db.String(50), primary_key=True)
    pw = Column(db.String(50), nullable=False)
    nickname = Column(db.String(50), nullable=False)

    theme_color = Column(db.string(20), default='')
    proimg = Column(db.String(10000000000), default='')
    backimg = Column(db.String(30), default='')
    introduction = Column(db.String(100), default='소개를 작성해주세요.')

    follow_num = Column(db.String(10), default=0)
    follower_num = Column(db.String(10), default=0)
