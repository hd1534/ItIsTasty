from ItIsTasty.resource import api
from flask_restplus import Resource, fields, marshal
from flask import request, send_file

from ItIsTasty.database.print import(
    add_request,
    get_request
)


ns = api.namespace('print', description='프린트 요청 정보')

out_coupon_model = ns.model('CouponModel', {
    'user_name': fields.String(required=True, attribute='user.name'),
    'mission_title': fields.String(required=True, attribute='mission.title'),
    'reward': fields.Integer(required=True),
    'bar_code':fields.Integer(required=True),
    "start_time": fields.DateTime(),
    "end_time": fields.DateTime()
})

print_request_model = ns.model('PrintRequestModel', {
    'coupon_id': fields.Integer(required=True)
})


@ns.route('/')
class PrintResource(Resource):
    @ns.expect(print_request_model)
    @ns.doc(responses={200: '성공'},
            description='''쿠폰을 출력을 요청합니다.''')
    def post(self):
        return {}, add_request(request.get_json()['coupon_id'])

    @ns.marshal_with(out_coupon_model)
    @ns.doc(responses={200: '성공', 404: '없음'},
            description='''프린트 요청을 받습니다.''')
    def get(self):
        return {}, get_request()
