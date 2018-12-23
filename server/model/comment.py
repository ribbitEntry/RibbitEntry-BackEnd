from . import db
from sqlalchemy import Column, ForeignKey
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comment'

    comment_id = Column(db.Integer)
    user = Column(db.String, ForeignKey("user.id"))
    date = Column(db.DateTime, default=datetime.now)

    title = Column(db.String(50), nullable=False)
    content = Column(db.String(100), nullable=False)
