from . import DB as db
from enum import Enum

from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,
                   primary_key=True,
                   nullable=False,
                   autoincrement=True)
    rfid = db.Column(db.String(10), nullable=True)
    user_type = db.Column(db.Enum('A', 'N'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    birth_day = db.Column(db.Integer, nullable=False)
    joined_date = db.Column(db.DateTime, nullable=True)
    living_place = db.Column(db.String(100), nullable=True)
    image_hashed = db.Column(db.Text(), nullable=True)
    image_origin = db.Column(db.Text(), nullable=True)

    log = db.relationship("Log", back_populates="user")
    coupon = db.relationship("Coupon", back_populates="user")


def add_user(data):
    db.session.add(User(
        name=data['name'],
        birth_day=data['birth_day'],
        rfid=data['rfid'],
        user_type=data['user_type'],
        joined_date=datetime.today(),
        living_place=data['living_place']
    ))
    db.session.commit()


def update_user(id, data):
    user = User.query.filter_by(id=id)

    if user.first() is None:
        return 404

    user.update({
        'name': data['name'],
        'birth_day': data['birth_day'],
        'rfid': data['rfid'],
        'user_type': data['user_type'],
        'living_place': data['living_place']
    })
    db.session.commit()
    return 200


def get_user(id):
    return User.query.filter_by(id=id).first()


def get_user_by_rfid(rfid):
    return User.query.filter_by(rfid=rfid).first()


def get_all_user():
    return User.query.all()


def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return 404
    db.session.delete(user)
    db.session.commit()
    return 200
