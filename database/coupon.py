from . import DB as db
from enum import Enum

from datetime import datetime, timedelta
import random

from ItIsTasty.database.mission import get_mission


class Coupon(db.Model):
    __tablename__ = 'coupon'
    id = db.Column(db.Integer,
                   primary_key=True,
                   nullable=False,
                   autoincrement=True)
    bar_code = db.Column(db.Integer, nullable=True, unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)

    reward = db.Column(db.String(100), nullable=True)
    print_count = db.Column(db.Integer, default=0)

    user = db.relationship("User", back_populates="coupon")
    mission = db.relationship("Mission", back_populates="coupon")
    print = db.relationship("Print", back_populates="coupon")


def add_coupon(data):
    mission = get_mission(data['mission_id'])
    if get_coupon_by_user_mission_id(data['user_id'], data['mission_id']) is not None:
        return 409
    db.session.add(Coupon(
        user_id=data['user_id'],
        mission_id=data['mission_id'],
        start_time=datetime.today(),
        end_time=datetime.today() + timedelta(days=30),
        reward=mission.reward
    ))
    db.session.commit()
    coupon = Coupon.query.filter_by(user_id=data['user_id'], mission_id=data['mission_id'])
    coupon.update({
        'bar_code': coupon.first().id * 100000 + random.randrange(100, 100000)
    })
    db.session.commit()
    return 200


def get_coupon(id):
    return Coupon.query.filter_by(id=id).first()


def get_coupon_by_user_mission_id(user_id, mission_id):
    return Coupon.query.filter_by(user_id=user_id, mission_id=mission_id).first()


def get_all_coupon():
    return Coupon.query.all()


def get_all_coupon_by_user(user_id):
    return Coupon.query.filter_by(user_id=user_id).all()


def delete_coupon(id):
    coupon = Coupon.query.filter_by(id=id).first()
    if coupon is None:
        return 404
    db.session.delete(coupon)
    db.session.commit()
    return 200


def add_print_count(coupon_id):
    coupon = Coupon.query.filter_by(id=coupon_id)

    if coupon.first() is None:
        return 404
    print_count = coupon.first().print_count
    coupon.update({
        'print_count': print_count + 1
    })
    db.session.commit()
