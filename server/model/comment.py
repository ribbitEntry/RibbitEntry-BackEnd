from datetime import datetime
from sqlalchemy import Column, ForeignKey

from server.extensions import db


class Comment(db.Model):
    __tablename__ = 'comment'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    comment_id = Column(db.Integer)
    user = Column(db.String, ForeignKey("user.id"))
    date = Column(db.DateTime, default=datetime.now)

    title = Column(db.String(50), nullable=False)
    content = Column(db.String(100), nullable=False)
