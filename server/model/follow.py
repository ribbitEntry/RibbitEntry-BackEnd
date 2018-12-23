from . import db
from sqlalchemy import Column, ForeignKey


class Follow(db.Model):
    __tablename__ = 'follow'

    follow = Column(db.String, ForeignKey("user.id"))
    follower = Column(db.String, ForeignKey("user.id"))