from sanic import Sanic, Blueprint
from sanic_cors import CORS

from service_api.api_routes import get_routes_api_v1
from service_api.config import RuntimeConfig
from service_api.constants import APP_NAME
from service_api.services.postgresql import Database


sanic_app = Sanic(APP_NAME)
sanic_app.update_config(RuntimeConfig)


cors = CORS(sanic_app, resources={r"/api/*": {"origins": "*"}})


sanic_app.blueprint(
    Blueprint.group(
        get_routes_api_v1(),
        url_prefix="api"
    )
)


@sanic_app.listener('before_server_start')
async def before_server_start(app, loop):
    await Database.connect()


@sanic_app.listener('before_server_stop')
async def before_server_stop(app, loop):
    await Database.close()
