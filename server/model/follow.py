from sqlalchemy import Column, ForeignKey

from server.extensions import db


class Follow(db.Model):
    __tablename__ = 'follow'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    follow = Column(db.String, ForeignKey("user.id"))
    follower = Column(db.String, ForeignKey("user.id"))