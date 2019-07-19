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
    #log = db.relationship("Log", back_populates="mission")


def add_mission(data):
    db.session.add(Mission(
        title=data['title'],
        description=data['description'],
        start_time=data['start_time'],
        end_time=data['end_time'],
        reward=data['reward']
    ))
    db.session.commit()


def update_mission(id, data):
    mission = Mission.query.filter_by(id=id)

    if mission.first() is None:
        return 404

    mission.update({
        'title': data['title'],
        'description': data['description'],
        'start_time': data['start_time'],
        'end_time': data['end_time'],
        'reward': data['reward']
    })
    db.session.commit()
    return 200


def get_mission(id):
    return Mission.query.filter_by(id=id).first


def get_all_mission():
    return Mission.query.all()


def delete_mission(id):
    mission = Mission.query.filter_by(id=id).first()
    if mission is None:
        return 404
    db.session.delete(mission)
    db.session.commit()
    return 200


