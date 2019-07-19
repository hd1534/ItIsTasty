from ItIsTasty.resource import api
from flask_restplus import Resource, fields, marshal
from flask import request, send_file

from ItIsTasty.database.coupon import(

)

ns = api.namespace('coupon', description='쿠폰 정보')


coupon_model = ns.model('CouponModel', {
    'user_name': fields.String(required=True),
    'mission_name': fields.String(required=True),
    'reward': fields.Integer(required=True),
    'bar_code':fields.Integer(required=True),
    "start_date": fields.DateTime(),
    "end_date": fields.DateTime()
})

