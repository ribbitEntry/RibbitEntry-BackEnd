from sqlalchemy import Column, ForeignKey

from server.extensions import db


class Follow(db.Model):
    __tablename__ = 'follow'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    follow_id = Column(db.Integer, primary_key=True, autoincrement=True)
    follow = Column(db.String(50), ForeignKey("user.id"))
    follower = Column(db.String(50), ForeignKey("user.id"))