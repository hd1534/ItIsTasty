from . import DB as db
from enum import Enum

from datetime import datetime


class Log(db.Model):
    __tablename__ = 'log'
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
    success = db.Column(db.Boolean, default=False)

    #user = db.relationship("User", back_populates="log")
    #mission = db.relationship("Mission", back_populates="log")

