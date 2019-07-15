from . import DB as db


class User(db.Model):
    __tablename__ = 'user'
    idx = db.Column(db.Integer,
                    primary_key=True,
                    nullable=False,
                    autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    living_place = db.Column(db.String(100), nullable=False)

    # serial = db.Column(db.Integer, nullable=False)


def add_user(data):
    db.session.add(User(
        name=data['name'],
        age=data['age'],
        living_place=data['living_place']
    ))
    db.session.commit()


def get_user(idx):
    return User.query.filter_by(idx=idx).first


def get_all_user():
    return User.query.all()


def delete_user(idx):
    user = User.query.filter_by(idx=idx).first()
    if user is None:
        return 404
    db.session.delete(user)
    db.session.commit()
    return 200
