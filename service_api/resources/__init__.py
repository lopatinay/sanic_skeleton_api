import json

from sanic.views import HTTPMethodView
from sanic.response import text, HTTPResponse

from service_api.services.common import JsonEncoder


class BaseResource(HTTPMethodView):
    DEFAULT_HEADERS = {"Content-Type": "application/json"}

    @staticmethod
    def json(payload, status=200, headers=None, *args, **kwargs):
        return HTTPResponse(
            json.dumps(payload, cls=JsonEncoder),
            status,
            BaseResource.DEFAULT_HEADERS | (headers or {}),
            *args,
            **kwargs
        )

    @staticmethod
    def text(payload, *args, **kwargs):
        return text(payload, *args, **kwargs)


class HealthCheckResource(BaseResource):
    async def get(self, request):
        return self.text("healthy")
