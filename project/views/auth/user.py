from flask import request
from flask_restx import Resource, Namespace

# from project.helpers.decorators import admin_required
from project.models import user_schema
from project.container import user_service

api = Namespace('user')


@api.route('/')
class UsersView(Resource):
    """
    Временно работает по старой схеме. В POST также проверяется есть ли уже пользователь с данным email
    """

    def get(self):
        all_users = user_service.get_all()
        result = user_schema.dump(all_users, many=True)
        return result, 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/user/{user.id}"}


@api.route('/<int:uid>')
class UserView(Resource):
    """
    Временно работает по старой схеме плюс в PUT проверка email и старого пароля при замене на новый
    """

    def get(self, uid):
        user = user_service.get_one(uid)
        result = user_schema.dump(user)
        return result, 200

    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        result = user_service.update(req_json)
        if not result:
            return "Login and/or email doesn't match!", 404
        return "", 204

    # @admin_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
