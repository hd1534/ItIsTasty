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
    snsimages = get_sns_post_image_by_idx(idx)
    imagepath = os.path.join(app.config['UPLOAD_FOLDER'],
                             snsimages.image_hashed)

    return send_file(imagepath,
                     attachment_filename=snsimages.image_origin,
                     as_attachment=True)
'''