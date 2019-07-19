from ItIsTasty.resource import api
from flask_restplus import Resource, fields, marshal
from flask import request, send_file

from ItIsTasty.database.coupon import(
    add_coupon,
    get_coupon,
    get_all_coupon,
    get_all_coupon_by_user,
    delete_coupon
)

ns = api.namespace('coupon', description='쿠폰 정보')

request_coupon_model = ns.model('RequestCouponModel', {
    'user_id': fields.Integer(required=True),
    'mission_id': fields.Integer(required=True),
})

out_coupon_model = ns.model('CouponModel', {
    'user_name': fields.String(required=True, attribute='user.name'),
    'mission_title': fields.String(required=True, attribute='mission.title'),
    'reward': fields.Integer(required=True),
    'bar_code':fields.Integer(required=True),
    'print_count':fields.Integer(required=True),
    "start_time": fields.DateTime(),
    "end_time": fields.DateTime()
})

full_coupon_model = ns.model('FullCouonModel', {
    'id': fields.Integer(required=True),
    'user_id': fields.Integer(required=True),
    'mission_id': fields.Integer(required=True),
    'user_name': fields.String(required=True, attribute='user.name'),
    'mission_title': fields.String(required=True, attribute='mission.title'),
    'reward': fields.Integer(required=True),
    'bar_code':fields.Integer(required=True),
    'print_count':fields.Integer(required=True),
    "start_time": fields.DateTime(),
    "end_time": fields.DateTime()
})

coupon_list_model = ns.model('CouponListModel', {
    'coupons': fields.List(fields.Nested(full_coupon_model))
})


@ns.route('/')
class CouponResource(Resource):
    @ns.expect(request_coupon_model)
    @ns.marshal_with(out_coupon_model)
    @ns.doc(responses={200: '성공', 409: '미션 성공 x'},
            description='''쿠폰을 발급 받습니다.
                           출력은  프린트 api를 이용해주세요''')
    def post(self):
        return {}, add_coupon(request.get_json())


@ns.route('/<int:coupon_id>')
class CouponIdResource(Resource):
    @ns.doc(responses={200: '성공', 404: '없는 미션입니다.'},
            description='''쿠폰을 삭제합니다.''')
    def delete(self, coupon_id):
        return {}, delete_coupon(coupon_id)


@ns.route('/user/<int:user_id>')
class CouponUserResource(Resource):
    @ns.marshal_with(coupon_list_model)
    @ns.doc(description='''해당 유저의 모든 쿠폰을 출력합니다.''',
            responses={200: '성공'})
    def get(self, user_id):
        return {'coupons': get_all_coupon_by_user(user_id)}

