from flask import Blueprint, request, jsonify
from app.services.pago_service import compensar_pago, crear_pago, listar_pagos

pago_bp = Blueprint('pago', __name__)

@pago_bp.route('/', methods=['POST'])
def crear_pago_route():
    data = request.get_json()
    try:
        pago = crear_pago(data)
        return jsonify({
            "mensaje": "Pago creado exitosamente",
            "pago": pago
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@pago_bp.route('/compensar/<int:id>', methods = ["DELETE"])
def compensar_pago_route(id):
    try:
        resultado = compensar_pago(id)
        return jsonify(resultado), 200
    except ValueError as e:
        return jsonify({"mensaje": str(e)}), 404

@pago_bp.route('/', methods=['GET'])
def listar_pagos_route():
    pagos = listar_pagos()
    return jsonify(pagos), 200
