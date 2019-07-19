from . import DB as db

from ItIsTasty.database.coupon import (
    get_coupon,
    add_print_count
)


class Print(db.Model):
    __tablename__ = 'print'
    id = db.Column(db.Integer,
                   primary_key=True,
                   nullable=False,
                   autoincrement=True)
    coupon_id = db.Column(db.Integer, db.ForeignKey('coupon.id'), nullable=False)
    coupon = db.relationship("Coupon", back_populates="print")


def add_request(coupon_id):
    db.session.add(Print(coupon_id=coupon_id))
    db.session.commit()
    return 200


def get_request():
    request = Print.query.first()
    if request is None:
        return 404
    coupon_id = request.coupon_id
    coupon = get_coupon(coupon_id)
    add_print_count(coupon_id)
    db.session.delete(request)
    db.session.commit()
    return coupon
