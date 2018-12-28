from sqlalchemy import Column, ForeignKey
from datetime import datetime

from server.extensions import db


class Post(db.Model):
    __tablename__ = 'post'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    post_id = Column(db.Integer, primary_key=True)
    user = Column(db.String, ForeignKey("user.id"))
    date = Column(db.DateTime, default=datetime.now)

    title = Column(db.String(50), nullable=False)
    content = Column(db.String(100), nullable=False)
    image = Column(db.String)

    like = Column(db.Integer, default=0)
    comment = Column(db.Integer, ForeignKey("comment.comment_id"), default=None)
