from flask import Blueprint, request, jsonify
from app.models.usuario import Usuario, db 

usuarios_bp = Blueprint('usuarios_bp', __name__)
@usuarios_bp.route("/usuarios/", methods=['GET'])
def all():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])\
    
@usuarios_bp.route("/usuarios/<id>", methods=['GET'])
def get(id):
    usuario = Usuario.query.get(id)
    return jsonify(usuario.to_dict())

@usuarios_bp.route("/usuarios/", methods=['POST'])
def create():
    data = request.get_json()
    usuario = Usuario(data['nombre'], data['email'], data['password'])
    db.session.add(usuario)
    db.session.commit()
    return jsonify(usuario.to_dict())

@usuarios_bp.route("/usuarios/<id>", methods=['PUT'])
def update(id):
    usuario = Usuario.query.get(id)
    data = request.get_json()
    usuario.nombre = data['nombre']
    usuario.email = data['email']
    db.session.commit()
    return jsonify(usuario.to_dict())

@usuarios_bp.route("/usuarios/<id>", methods=['DELETE'])
def delete(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify(usuario.to_dict())
