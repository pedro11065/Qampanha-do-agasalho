from flask import Blueprint, request, render_template
from src.model.classes import *
from src.config.colors import *

team = Blueprint('auth_team', __name__, template_folder='templates', static_folder='static')

@team.route('/search', methods= ['POST']) #methods=['GET', 'POST']
def index_page():
    print(yellow("[API]: ") + "POST request from api/search received")

    # data = request.get_json() ; backend = Backend()
    # return backend.user.login(data)

    return render_template('index.html')
    