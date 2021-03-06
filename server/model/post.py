from sqlalchemy import Column, ForeignKey
from datetime import datetime

from server.extensions import db


class Post(db.Model):
    __tablename__ = 'post'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    post_id = Column(db.Integer, primary_key=True, autoincrement=True)
    user = Column(db.String(50), ForeignKey("user.id"))
    date = Column(db.DateTime, default=datetime.now)

    content = Column(db.String(100))
    image = Column(db.VARCHAR(2048), default='')

    like = Column(db.Integer, default=0)
