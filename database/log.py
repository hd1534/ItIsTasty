from . import DB as db
from enum import Enum

from datetime import datetime


class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer,
                   primary_key=True,
                   nullable=False,
                   autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)
    success = db.Column(db.Boolean, default=False)

    user = db.relationship("User", back_populates="log")
    mission = db.relationship("Mission", back_populates="log")


def add_log(data):
    db.session.add(Log(
        user_id=data['user_id'],
        mission_id=data['mission_id'],
        start_time=datetime.today()
    ))
    db.session.commit()


def finish_log(log_id):
    log = Log.query.filter_by(id=log_id)

    if log.first() is None:
        return 404

    log.update({
        'end_time': datetime.today(),
        'success': True
    })
    db.session.commit()
    return 200


def get_log(id):
    return Log.query.filter_by(id=id).first()


def get_log_user_mission_id(user_id, mission_id):
    return Log.query.filter_by(user_id=user_id, mission_id=mission_id).first()


def get_all_log():
    return Log.query.all()


def delete_log(id):
    log = Log.query.filter_by(id=id).first()
    if log is None:
        return 404
    db.session.delete(log)
    db.session.commit()
    return 200
