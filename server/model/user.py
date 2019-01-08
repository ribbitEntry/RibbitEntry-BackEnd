from sqlalchemy import Column

from server.extensions import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(db.String(50), primary_key=True)
    pw = Column(db.String(50))
    nickname = Column(db.String(50))

    theme_color = Column(db.String(20), default='#F58EA8')
    proimg = Column(db.VARCHAR(2048), default='  ')
    backimg = Column(db.VARCHAR(2048), default='  ')
    introduction = Column(db.String(100), default='소개를 작성해주세요.')

    follow_num = Column(db.Integer, default=0)
    follower_num = Column(db.Integer, default=0)
