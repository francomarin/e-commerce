from flask import Blueprint, request, jsonify
from app.services.producto_service import crear_producto, obtener_por_id

catalogo_bp = Blueprint('catalogo', __name__)

@catalogo_bp.route('/', methods = ['POST'])
def crear_producto_route():
    data = request.get_json()
    try:
        producto = crear_producto(data)
        return jsonify({
            "mensaje": "Producto creado exitosamente",
            "producto": producto
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@catalogo_bp.route('/<int:id>', methods = ['GET'])
def obtener_producto_id_route(id):
    try:
        producto = obtener_por_id(id)
        if producto is None:
            return jsonify({"mensaje": "No se encontro el producto."}), 404
        return jsonify(producto), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404