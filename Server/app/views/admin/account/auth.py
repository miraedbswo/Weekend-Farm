from flask import Blueprint, abort, request
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash

from app.models.admin import AdminModel
from app.views import BaseResource


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin'


@api.resource('/login')
class AccountManagement(BaseResource):
    def post(self):
        """
        관리자 로그인
        """
        payload = request.json

        admin_id = payload['id']
        admin_pw = payload['pw']

        admin = AdminModel.objects(id=admin_id).first()

        if admin is None:
            abort(406)

        return {
            'access_token': create_access_token(identity=admin_id),
            'refresh_token': create_refresh_token(identity=admin_id)
        }, 200 if check_password_hash(admin.pw, admin_pw) else abort(406)
