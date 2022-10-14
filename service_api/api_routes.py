from sanic.blueprints import Blueprint

from service_api.resources import HealthCheckResource


def get_routes_api_v1():
    bp = Blueprint(name="api_v1", url_prefix="/v1")

    bp.add_route(HealthCheckResource.as_view(), "/health")

    return bp
