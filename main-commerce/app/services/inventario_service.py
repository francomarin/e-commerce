from app import INVENTARIO_SERVICE_URL
from app.services.api_requests import forward_request

class InventarioService:
    @staticmethod
    def registrar_venta(data):
        """Descuenta el inventario del producto"""
        url = f"{INVENTARIO_SERVICE_URL}/"
        response, status_code = forward_request(url, "POST", data=data)
        if status_code == 201:
            transaccion_id = response.get("transaccion", {}).get("id")
            data["transaccion_id"] = transaccion_id
            return data
        raise ValueError("Error al crear la venta")

    @staticmethod
    def compensar_venta(transaccion_id):
        """Compensa el descuento de inventario en caso de error"""
        url = f"{INVENTARIO_SERVICE_URL}/compensar/{transaccion_id}"
        response, status_code = forward_request(url, "DELETE")
        return {"status": "Compensacion completada"} if status_code == 200 else None

    @staticmethod
    def obtener_stock(id):
        url = f"{INVENTARIO_SERVICE_URL}/{id}"
        response, status_code = forward_request(url, "GET")
        if status_code == 200:
            return response
        else:
            return None