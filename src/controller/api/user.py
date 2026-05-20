from flask import Blueprint, request, render_template
from src.model.classes import *
from src.config.colors import *

user = Blueprint('auth_user', __name__, template_folder='templates', static_folder='static')

@user.route('/searchByTeam', methods= ['POST']) #methods=['GET', 'POST']
def search_users():
    print(yellow("[API]: ") + "POST request from user/api/search received")

    data = request.get_json() ; backend = Backend()
    return backend.user.searchByTeam(data)


@user.route('/create', methods= ['POST']) #methods=['GET', 'POST']
def create_users():
    print(yellow("[API]: ") + "POST request from user/api/create received")

    data = request.get_json() ; backend = Backend()
    return backend.user.create(data)