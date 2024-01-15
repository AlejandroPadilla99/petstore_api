from flask import Blueprint, request, jsonify

item_router = Blueprint("item_router", __name__)

@item_router.route("/item/<string:item_uuid>", methods=["GET"])
def handler_get_item(item_uuid):
    try:
        return "your item" + item_uuid
    except Exception as error:
        response = jsonify({"status": "ERROR", "errors": str(error)})
        response.status_code = 500
        return response

@item_router.route("/item", methods=["POST"])
def handler_create_item():
     try: 
        item_data = request.get_json()
        return item_data
     except Exception as error:
        response = jsonify({"status": "ERROR", "errors": str(error)})
        response.status_code = 500
        return response

@item_router.route('/item/<string:item_uuid>', methods=["PUT"])
def hander_update_item(item_uuid):
    try:
        return "your item was updated " + item_uuid
    except Exception as error:
        response = jsonify({"status": "ERROR", "errors": str(error)})
        response.status_code = 500
        return response

@item_router.route('/item/<string:item_uuid>', methods=["DELETE"])
def hander_delete_item(item_uuid):
    try:
        return "your item was delete " + item_uuid
    except Exception as error:
        response = jsonify({"status": "ERROR", "errors": str(error)})
        response.status_code = 500
        return response


