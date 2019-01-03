from datetime import datetime
from sqlalchemy import Column, ForeignKey

from server.extensions import db


class Comment(db.Model):
    __tablename__ = 'comment'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    comment_id = Column(db.Integer, primary_key=True, autoincrement=True)
    user = Column(db.String(50), ForeignKey("user.id"))
    date = Column(db.DateTime, default=datetime.now)

    content = Column(db.String(100), nullable=False)
