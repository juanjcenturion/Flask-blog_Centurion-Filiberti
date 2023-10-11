from flask.views import MethodView
from flask import request, jsonify
from app.models.models import *
from app import database as db, app

from app.schemas.schemas import (
    UserSchema
)

class UsersAPI(MethodView):
    def get(self, user_id = None):
        if user_id is None:
            users = User.query.all()
            resultado =  UserSchema().dump(users, many=True)
        else:
            user = User.query.get(user_id)
            resultado = UserSchema().dump(user)
        return jsonify(resultado)

    def post(self):
        user_json = UserSchema().load(request.json)
        username = user_json.get('username')
        password = user_json.get('password')

        new_user = User(username=username, password_hash = password, is_admin = False)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(UserSchema().dump(new_user))

    def put(self, user_id):
        user = User.query.get(user_id)
        user_json = UserSchema().load(request.json)
        username  = user_json.get('username')
        user.username = username
        db.session.commit()
        return jsonify(UserSchema().dump(user))
    
    def delete(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify(mensaje=f"Borraste el pais {user_id}")

app.add_url_rule("/user", view_func=UsersAPI.as_view('pais'))
app.add_url_rule("/user/<user_id>", 
                view_func=UsersAPI.as_view('pais_por_id')
                )
