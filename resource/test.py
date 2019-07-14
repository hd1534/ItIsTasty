from ItIsTasty.resource import api
# import datetime
from flask_restplus import Resource, fields, marshal
'''
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)
'''
# from flask import Flask, send_file
from ItIsTasty.database.test import (
    add_test,
    get_test,
    delete_test,
    get_all_test,
    write,
    read
)
from flask import request
# import xlsxwriter


ns = api.namespace('test', description='연습을 하자!')


test_model = ns.model('TestModel', {
    'idx': fields.Integer(required=True),
    'name': fields.String(required=True)
})


data_model = ns.model('Data', {
    'data': fields.String(required=True)
})

test_list_model = ns.model('TestListModel', {
    'tests': fields.List(fields.Nested(test_model))
})


@ns.route('/txt')
class Test(Resource):
    @ns.expect(data_model)
    @ns.doc(responses={200: '성공'},
            description="배고파")
    def post(self):
        data = request.get_json()
        write(data['data'])
        return 200

    @ns.marshal_with(data_model)
    @ns.doc(reponses={200: '성공'},
            description='배고파')
    def get(self):
        return {'data': read()}


@ns.route('/')
class TestResource(Resource):
    @ns.expect(test_model)
    @ns.doc(responses={200: '성공'},
            description='''배고파''')
    def post(self):
        data = request.get_json()
        add_test(data['name'])
        return {}, 200

    @ns.marshal_with(test_list_model)
    @ns.doc(description='''모든 test를 출력.''',
            responses={200: '성공'})
    def get(self):
        data = get_all_test()
        return {'tests': data}