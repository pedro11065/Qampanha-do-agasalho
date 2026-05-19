from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='view/static', template_folder='view/templates')
    #app.config['SECRET_KEY'] = 'chave_secreta_nome' #Responsável por encriptar os cookies e session data (Ainda não utilizado).

    from src.controller.index import index
    from src.controller.api.donation import donation
    from src.controller.api.user import user
    from src.controller.api.team import team

    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(donation, url_prefix='/donation')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(team, url_prefix='/team')

    return app;


