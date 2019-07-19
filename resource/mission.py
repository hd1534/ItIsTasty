from ItIsTasty.resource import api
from flask_restplus import Resource, fields, marshal
from flask import request, send_file

from ItIsTasty.database.mission import(
    add_mission,
    update_mission,
    get_mission,
    get_all_mission,
    delete_mission
)


ns = api.namespace('mission', description='미션 정보')


mission_model = ns.model('MissionModel', {
    'title': fields.String(required=True),
    'description': fields.String(required=True),
    'start_time': fields.DateTime(required=True),
    'end_time': fields.DateTime(required=True),
    'reward': fields.Integer(required=False)
})

full_mission_model = ns.model('FullMissionModel', {
    'idx': fields.Integer(required=True),
    'title': fields.String(required=True),
    'description': fields.String(required=True),
    'start_time': fields.DateTime(required=True),
    'end_time': fields.DateTime(required=True),
    'reward': fields.Integer(required=False)
})

mission_list_model = ns.model('MissionListModel', {
    'users': fields.List(fields.Nested(full_mission_model))
})


@ns.route('/')
class MissionResource(Resource):
    @ns.expect(mission_model)
    @ns.doc(responses={200: '성공'},
            description='''미션을 추가합니다.''')
    def post(self):
        add_mission(request.get_json())
        return {}, 200

    @ns.marshal_with(mission_list_model)
    @ns.doc(description='''모든 미션을 출력합니다.''',
            responses={200: '성공'})
    def get(self):
        return {'users': get_all_mission()}


@ns.route('/<int:mission_idx>')
class MissionIdxResource(Resource):
    @ns.expect(mission_model)
    @ns.doc(responses={200: '성공', 404: '없는 미션입니다.'},
            description='''미션 정보를 수정합니다.''')
    def put(self, mission_idx):
        return {}, update_mission(mission_idx, request.get_json())

    @ns.doc(responses={200: '성공', 404: '없는 미션입니다.'},
            description='''미션을 삭제합니다.''')
    def delete(self, mission_idx):
        return {}, delete_mission(mission_idx)
