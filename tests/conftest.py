import os
from asyncio import get_event_loop

import pytest
from alembic.config import Config
from alembic import command

from service_api.config import RuntimeConfig
from service_api.services.postgresql import Aiopg


async def create_test_db(db_name):
    await Aiopg.execute("DROP DATABASE IF EXISTS %s" % db_name)
    await Aiopg.execute("CREATE DATABASE %s" % db_name)
    await Aiopg.close()


async def drop_test_db(db_name):
    await Aiopg.close()
    await Aiopg.execute("DROP DATABASE IF EXISTS %s" % db_name)
    await Aiopg.close()


@pytest.fixture(scope="session", autouse=True)
def db_fixture():
    loop = get_event_loop()

    loop.run_until_complete(create_test_db(RuntimeConfig.UNITTEST_PG_NAME))

    # Use UNITTEST_PG_NAME as main database
    pg_name = RuntimeConfig.PG_NAME
    RuntimeConfig.PG_NAME = RuntimeConfig.UNITTEST_PG_NAME

    alembic_cfg = Config(os.path.join(RuntimeConfig.BASE_DIR, "alembic.ini"))
    alembic_cfg.set_main_option('script_location', os.path.join(RuntimeConfig.BASE_DIR, "alembic"))
    command.upgrade(alembic_cfg, "head")

    yield

    # Switch back to the main database and drop test database
    RuntimeConfig.PG_NAME = pg_name
    loop.run_until_complete(drop_test_db(RuntimeConfig.UNITTEST_PG_NAME))

    loop.close()
