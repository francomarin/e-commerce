from app import PAGOS_SERVICE_URL
from app.services.api_requests import forward_request

class PagoService:
    @staticmethod
    def crear_pago(data):
        """Crea un pago en el microservicio de pagos"""
        url = f"{PAGOS_SERVICE_URL}/"
        response, status_code = forward_request(url, "POST", data=data)
        if status_code == 201:
            pago_id = response.get("pago", {}).get("id")
            data["pago_id"] = pago_id
            return data
        raise ValueError("Error al crear pago")

    @staticmethod
    def compensar_pago(pago_id):
        """Compensa el pago en caso de error en la transacción"""
        url = f"{PAGOS_SERVICE_URL}/compensar/{pago_id}"
        response, status_code = forward_request(url, "DELETE")
        return {"status": "Compensacion completada"} if status_code == 200 else None
