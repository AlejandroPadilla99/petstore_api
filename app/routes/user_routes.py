from flask import Blueprint, jsonify, request

user_router = Blueprint("user", __name__)
item_router = Blueprint("item", __name__)

#user
@user_router.route("/user/<string:user_uuid>", methods=["GET"])
def handler_get_user(user_uuid):
    try:
        return "your user" + user_uuid
    except Exception as error:
        response = jsonify({"status": "ERROR", "errors": str(error)})
        response.status_code = 500
        return response

@user_router.route("/user", methods=["POST"])
def handler_create_user():
    try:
        user_data = request.get_json()
        return user_data
    except Exception as error:
        response = jsonify({"status": "ERROR", "errors": str(error)})
        response.status_code = 500
        return response

@user_router.route("/user/<string:user_uuid>", methods=["PUT"])
def handler_update_user(user_uuid):
    try:
        return "this is the user updated" + user_uuid
    except Exception as error:
        response = jsonify({"status": "ERROR", "errors": str(error)})
        response.status_code = 500
        return response

@user_router.route("/user/<string:user_uuid>", methods=["DELETE"])
def handler_delete_user(user_uuid):
    try:
       return "this is the user was deleted" + user_uuid 
    except Exception as error:
        response = jsonify({"status": "ERROR", "errors": str(error)})
        response.status_code = 500
        return response
