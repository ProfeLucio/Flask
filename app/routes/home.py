from flask import Blueprint, request, jsonify

home_bp = Blueprint('home_bp', __name__)
@home_bp.route("/")
def home():
    return """
    <html>
        <head><title>Seminario II</title></head>
        <body>
            <h1>Bienvenido</h1>
            <p>Esta es una respuesta HTML directa desde Flask.</p>
        </body>
    </html>
    """