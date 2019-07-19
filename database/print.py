from . import DB as db


class Print(db.Model):
    __tablename__ = 'print'
    id = db.Column(db.Integer,
                   primary_key=True,
                   nullable=False,
                   autoincrement=True)

    #coupon_id = db.Column(db.Integer, db.ForeignKey('coupon.id'), nullable=False)
    coupon_id = db.Column(db.Integer, nullable=False)
    printed = db.Column(db.Boolean, default=False)
    # coupon = db.relationship("Coupon", back_populates="print")


def get_requests():
    return Print.query.filter_by(printed=False).all()
