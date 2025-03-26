
from .home import home_bp 
from .usuarios import usuarios_bp 

def init_app(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(usuarios_bp)