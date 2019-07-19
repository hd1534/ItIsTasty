from ItIsTasty.resource import api
from flask_restplus import Resource, fields, marshal
from flask import request, send_file

from ItIsTasty.database.user import(
    add_user,
    update_user,
    get_user,
    get_user_by_rfid,
    get_all_user,
    delete_user
)


ns = api.namespace('form/user', description='사용자 정보(form 사용)')


user_model = ns.model('UserModel', {
    'name': fields.String(required=True),
    'birth_day': fields.Integer(required=True),
    'rfid': fields.String(required=False),
    'living_place': fields.String(required=True),
    'user_type': fields.String(required=True)
})

full_user_model = ns.model('FullUserModel', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'birth_day': fields.Integer(required=True),
    'rfid': fields.String(required=False),
    'living_place': fields.String(required=True),
    'user_type': fields.String(required=True)
})

user_list_model = ns.model('UserListModel', {
    'users': fields.List(fields.Nested(full_user_model))
})


@ns.route('/')
class UserResource(Resource):
    @ns.expect(user_model)
    @ns.doc(responses={200: '성공'},
            description='''사용자를 추가합니다.
            user_type은 꼭 A(어드민) 또는 N(노숙자)로 넣어주세요
            생일은 YYYYMMDD 8글자로 넣어주세요(0으로 시작 x)''')
    def post(self):
        add_user(request.form)
        return {}, 200

    @ns.marshal_with(user_list_model)
    @ns.doc(description='''모든 사용자를 출력합니다.''',
            responses={200: '성공'})
    def get(self):
        return {'users': get_all_user()}


@ns.route('/<int:user_id>')
class UserIdResource(Resource):
    @ns.expect(user_model)
    @ns.doc(responses={200: '성공', 404: '없는 사용자입니다.'},
            description='''사용자 정보를 수정합니다.''')
    def put(self, user_id):
        return {}, update_user(user_id, request.form)

    @ns.doc(responses={200: '성공', 404: '없는 사용자입니다.'},
            description='''사용자를 삭제합니다.''')
    def delete(self, user_id):
        return {}, delete_user(user_id)


@ns.route('/rfid/<rfid>')
class UserResource(Resource):
    @ns.marshal_with(user_model)
    @ns.doc(description='''해당 rfid의 사용자를 출력합니다.''',
            responses={200: '성공'})
    def get(self, rfid):
        return get_user_by_rfid(rfid), 200
