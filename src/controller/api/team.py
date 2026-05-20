from flask import Blueprint, request, render_template
from src.model.classes import *
from src.config.colors import *

team = Blueprint('auth_team', __name__, template_folder='templates', static_folder='static')

@team.route('/search', methods= ['GET']) #methods=['GET', 'POST']
def search_teams():
    print(yellow("[API]: ") + "GET request from team/api/search received")

    backend = Backend()
    return backend.team.search()