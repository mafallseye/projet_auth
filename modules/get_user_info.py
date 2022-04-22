from optparse import Values
from flask import Flask, jsonify, request, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint

def check_password(Pass):
    maj = 0
    num = 0
    for i in Pass :
        if i >= 'A' and i <= 'Z':
            maj += 1
    for i in Pass :
        if i >= '0' and i <= '8':
            num += 1
    if maj == 0 or num == 0 or len(Pass) < 8:
        return (False)
    return True

GET_INFOS = Blueprint("get_user_info", __name__)
@GET_INFOS.route('/register', methods=['POST'])
def Register():
    infos = request.form
    data = []

    if not check_password(infos["password"]):
        return ("Invalid Password")
    data.append(infos["userid"])
    data.append(infos["mail"])
    data.append(infos["username"])
    data.append(infos["password"])

    return jsonify(data)

#def get_blueprint():
#    return REGISTER