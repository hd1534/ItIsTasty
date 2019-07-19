from . import DB as db
from enum import Enum

from datetime import datetime


class Coupon(db.Model):
    __tablename__ = 'coupon'
    id = db.Column(db.Integer,
                   primary_key=True,
                   nullable=False,
                   autoincrement=True)

    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    mission_id = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)

    reward = db.Column(db.Integer, nullable=True)
    bar_code = db.Column(db.Integer, nullable=True)
    print_count = db.Column(db.Integer, default=0)

    user = db.relationship("User", back_populates="coupon")
    mission = db.relationship("Mission", back_populates="coupon")
    print = db.relationship("Print", back_populates="coupon")
