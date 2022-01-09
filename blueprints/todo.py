from flask import Blueprint, jsonify

todo_blueprint = Blueprint("todo", __name__)


@todo_blueprint.route("", methods=("GET",))
def list():
    return jsonify({"success": True, "todos": []})
