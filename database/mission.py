from . import DB as db
from enum import Enum

from datetime import datetime


class Mission(db.Model):
    __tablename__ = 'mission'
    id = db.Column(db.Integer,
                   primary_key=True,
                   nullable=False,
                   autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)
    reward = db.Column(db.Integer, nullable=True)

    coupon = db.relationship("Coupon", back_populates="mission")
    log = db.relationship("Log", back_populates="mission")


