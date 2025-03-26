from flask import Flask
from app.config.settings import Config
from app.models import init_app as init_db
from app.routes import init_app as init_routes

def create_app():
    app = Flask(__name__)
    
    # Cargar configuración desde clase Config
    app.config.from_object(Config)
    
    # Inicializar base de datos
    init_db(app)

    # Registrar rutas (usuarios, reconocimiento, etc.)
    init_routes(app)

    return app
