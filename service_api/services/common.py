import json
from datetime import datetime
from uuid import UUID

from arrow import Arrow

from service_api.domain import DomainModel


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        elif isinstance(obj, datetime):
            return str(obj)
        elif isinstance(obj, Arrow):
            return obj.format()
        elif isinstance(obj, DomainModel):
            return obj.json
        return json.JSONEncoder.default(self, obj)
