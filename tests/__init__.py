import os
import json
from unittest import IsolatedAsyncioTestCase

import yaml

from service_api.app import sanic_app
from service_api.config import RuntimeConfig
from service_api.models import models
from service_api.services.postgresql import Aiopg


class BaseTestCase(IsolatedAsyncioTestCase):
    fixture = None

    HEADERS = {
        "Content-type": "application/json",
    }

    @staticmethod
    def api_v1(path):
        return "/api/v1" + path

    @staticmethod
    def jdumps(payload):
        return json.dumps(payload)

    @property
    def app(self):
        return sanic_app

    async def asyncSetUp(self):
        if self.fixture is not None:
            await FixtureLoader(os.path.join(RuntimeConfig.BASE_DIR, "tests", self.fixture)).load_fixture()

    async def asyncTearDown(self):
        if self.fixture is not None:
            await clear_tables()


class FixtureLoader:
    def __init__(self, fixture_path):
        self.fixture_path = fixture_path

    async def load_fixture(self):
        data = self.dict_from_yml_fixture()

        for model in models:
            records = data.get(model.name)
            if records is not None:
                stmt = model.insert().values(records)
                try:
                    await Aiopg.execute(stmt)
                except Exception as e:
                    raise

    def dict_from_yml_fixture(self):
        with open(self.fixture_path) as fd:
            return yaml.safe_load(fd.read())


async def clear_tables():
    for model in models:
        await Aiopg.execute(f"TRUNCATE TABLE {model.name} CASCADE")
