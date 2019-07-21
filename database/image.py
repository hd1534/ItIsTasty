from . import DB as db
from enum import Enum

from datetime import datetime


class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer,
                   primary_key=True,
                   nullable=False,
                   autoincrement=True)
    image_hashed = db.Column(db.Text(), nullable=True)
    image_origin = db.Column(db.Text(), nullable=True)


'''
def get_image():
    images = get_image_by_id(id)
    imagepath = os.path.join(app.config['UPLOAD_FOLDER'],
                             images.image_hashed)

    return send_file(imagepath,
                     attachment_filename=images.image_origin,
                     as_attachment=True)
'''
