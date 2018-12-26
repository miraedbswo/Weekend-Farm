from flask import Blueprint, abort, request
from flask_restful import Apis
from werkzeug.security import generate_password_hash

from app.views import BaseResource
from app.models.admin import AdminModel


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin'


@api.resource('/signup')
class SignupAdmin(BaseResource):
    def post(self):
        """
        관리자 회원가입
        """
        admin_id = request.json['id']
        admin_pw = request.json['pw']
        admin_name = request.json['name']
        admin_phone_number = request.json['phone_number']

        if AdminModel.objects(id=admin_id).first():
            abort(409)

        admin_hashed_pw = generate_password_hash(admin_pw)

        AdminModel(
            id=admin_id,
            pw=admin_hashed_pw,
            name=admin_name,
            phone_number=admin_phone_number
        ).save()

        return '', 201
