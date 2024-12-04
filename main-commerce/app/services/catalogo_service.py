from app import cache, CATALOGO_SERVICE_URL
from app.services.api_requests import forward_request

class CatalogoService:

    @cache.memoize(timeout=90)
    def obtener_producto(self, id):
        url = f"{CATALOGO_SERVICE_URL}/{id}"
        response, status_code = forward_request(url, "GET")
        if status_code == 200:
            return response
        else:
            return None