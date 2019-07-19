from . import DB as db
from enum import Enum

from datetime import datetime


class Coupon(db.Model):
    __tablename__ = 'coupon'
    id = db.Column(db.Integer,
                   primary_key=True,
                   nullable=False,
                   autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)

    reward = db.Column(db.Integer, nullable=True)
    bar_code = db.Column(db.Integer, nullable=True)
    print_count = db.Column(db.Integer, default=0)

    user = db.relationship("User", back_populates="coupon")
    mission = db.relationship("Mission", back_populates="coupon")
    # print = db.relationship("Print", back_populates="coupon")


def add_coupon(data):
    db.session.add(Coupon(
        title=data['title'],
        description=data['description'],
        start_time=data['start_time'],
        end_time=data['end_time'],
        reward=data['reward']
    ))
    db.session.commit()


def update_coupon(id, data):
    coupon = Coupon.query.filter_by(id=id)

    if coupon.first() is None:
        return 404

    coupon.update({
        'title': data['title'],
        'description': data['description'],
        'start_time': data['start_time'],
        'end_time': data['end_time'],
        'reward': data['reward']
    })
    db.session.commit()
    return 200


def get_coupon(id):
    return Coupon.query.filter_by(id=id).first


def get_all_coupon():
    return Coupon.query.all()


def delete_coupon(id):
    coupon = Coupon.query.filter_by(id=id).first()
    if coupon is None:
        return 404
    db.session.delete(coupon)
    db.session.commit()
    return 200


