from ItIsTasty.resource import api
from flask_restplus import Resource, fields, marshal
from flask import request, send_file

from ItIsTasty.database.mission import(
    add_mission,
    update_mission,
    get_mission,
    get_all_mission_and_log_by_user_id,
    get_all_mission,
    delete_mission
)


ns = api.namespace('form/mission', description='미션 정보(form 사용)')


mission_model = ns.model('MissionModel', {
    'title': fields.String(required=True),
    'description': fields.String(required=True),
    'start_time': fields.DateTime(required=True),
    'end_time': fields.DateTime(required=True),
    'reward': fields.String(required=False)
})

full_mission_model = ns.model('FullMissionModel', {
    'id': fields.Integer(required=True),
    'title': fields.String(required=True),
    'description': fields.String(required=True),
    'start_time': fields.DateTime(required=True),
    'end_time': fields.DateTime(required=True),
    'reward': fields.String(required=False)
})

log_model = ns.model('LogModel', {
    'user_id': fields.Integer(required=True),
    'mission_id': fields.Integer(required=True),
    'start_time': fields.DateTime(required=True),
    'end_time': fields.DateTime(required=True),
    'success': fields.Boolean(required=True)
})

full_mission_log_model = ns.model('FullMissionLogModel', {
    'id': fields.Integer(required=True),
    'user_id': fields.Integer(attribute='log.user_id', required=True),
    'title': fields.String(required=True),
    'description': fields.String(required=True),
    'start_time': fields.DateTime(required=True),
    'end_time': fields.DateTime(required=True),
    'reward': fields.String(required=False),
    'my_start_time': fields.DateTime(attribute='log.start_time', required=True),
    'my_end_time': fields.DateTime(attribute='log.end_time', required=True),
    'success': fields.Boolean(required=True)
})

mission_list_model = ns.model('MissionListModel', {
    'missions': fields.List(fields.Nested(full_mission_model))
})

mission_log_list_model = ns.model('MissionLogListModel', {
    'missions': fields.List(fields.Nested(full_mission_log_model))
})


@ns.route('/')
class MissionResource(Resource):
    @ns.expect(mission_model)
    @ns.doc(responses={200: '성공'},
            description='''미션을 추가합니다.''')
    def post(self):
        add_mission(request.form)
        return {}, 200

    @ns.marshal_with(mission_list_model)
    @ns.doc(description='''모든 미션을 출력합니다.''',
            responses={200: '성공'})
    def get(self):
        return {'missions': get_all_mission()}


@ns.route('/mission/<int:mission_id>')
class MissionIdResource(Resource):
    @ns.expect(mission_model)
    @ns.doc(responses={200: '성공', 404: '없는 미션입니다.'},
            description='''미션 정보를 수정합니다.''')
    def put(self, mission_id):
        return {}, update_mission(mission_id, request.form)

    @ns.doc(responses={200: '성공', 404: '없는 미션입니다.'},
            description='''미션을 삭제합니다.''')
    def delete(self, mission_id):
        return {}, delete_mission(mission_id)


@ns.route('/user/<int:user_id>')
class MissionUserResource(Resource):
    @ns.marshal_with(mission_log_list_model)
    @ns.doc(description='''모든 미션을 출력합니다.''',
            responses={200: '성공'})
    def get(self, user_id):
        return {'missions': get_all_mission_and_log_by_user_id(user_id)}, 200