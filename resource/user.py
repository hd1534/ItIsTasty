from ItIsTasty.resource import api
from flask_restplus import Resource, fields, marshal
from flask import request, send_file

from ItIsTasty.database.user import(
    add_user,
    update_user,
    get_user,
    get_all_user,
    delete_user
)


ns = api.namespace('user', description='사용자 정보')


user_model = ns.model('UserModel', {
    'name': fields.String(required=True),
    'age': fields.Integer(required=True),
    'living_place':fields.String(required=True)
})

full_user_model = ns.model('FullUserModel', {
    'idx': fields.Integer(required=True),
    'name': fields.String(required=True),
    'age': fields.Integer(required=True),
    'living_place':fields.String(required=True)
})

user_list_model = ns.model('UserListModel', {
    'users': fields.List(fields.Nested(full_user_model))
})


@ns.route('/')
class UserResource(Resource):
    @ns.expect(user_model)
    @ns.doc(responses={200: '성공'},
            description='''사용자를 추가합니다.''')
    def post(self):
        add_user(request.get_json())
        return {}, 200

    @ns.marshal_with(user_list_model)
    @ns.doc(description='''모든 사용자를 출력합니다.''',
            responses={200: '성공'})
    def get(self):
        return {'users': get_all_user()}


@ns.route('/<int:user_idx>')
class UserIdxResource(Resource):
    @ns.expect(user_model)
    @ns.doc(responses={200: '성공', 404: '없는 사용자입니다.'},
            description='''사용자 정보를 수정합니다.''')
    def put(self, user_idx):
        return {}, update_user(user_idx, request.get_json())

    @ns.doc(responses={200: '성공', 404: '없는 사용자입니다.'},
            description='''사용자를 삭제합니다.''')
    def delete(self, user_idx):
        return {}, delete_user(user_idx)


@ns.route('/form/')
class UserResource(Resource):
    @ns.expect(user_model)
    @ns.doc(responses={200: '성공'},
            description='''사용자를 추가합니다.''')
    def post(self):
        add_user(request.form)
        return {}, 200

    @ns.marshal_with(user_list_model)
    @ns.doc(description='''모든 사용자를 출력합니다.''',
            responses={200: '성공'})
    def get(self):
        return {'users': get_all_user()}


@ns.route('/form/<int:user_idx>')
class UserIdxResource(Resource):
    @ns.expect(user_model)
    @ns.doc(responses={200: '성공', 404: '없는 사용자입니다.'},
            description='''사용자 정보를 수정합니다.''')
    def put(self, user_idx):
        return {}, update_user(user_idx, request.form)

    @ns.doc(responses={200: '성공', 404: '없는 사용자입니다.'},
            description='''사용자를 삭제합니다.''')
    def delete(self, user_idx):
        return {}, delete_user(user_idx)
