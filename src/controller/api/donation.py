from flask import Blueprint, request, render_template
from src.model.classes import *
from src.config.colors import *

donation = Blueprint('auth_donation', __name__, template_folder='templates', static_folder='static')

@donation.route('/searchOpt', methods= ['GET']) #methods=['GET', 'POST'] 
def search_donation_opt():
    print(yellow("[API]: ") + "GET request from donation/api/search received")
    backend = Backend()
    return backend.donation.search()

@donation.route('/create', methods= ['POST']) #methods=['GET', 'POST']
def create_donation():
    print(yellow("[API]: ") + "POST request from donation/api/create received")

    data = request.get_json() ; backend = Backend()
    return backend.donation.create(data)