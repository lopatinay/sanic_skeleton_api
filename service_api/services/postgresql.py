import operator as op

from aiopg.sa import create_engine
from psycopg2 import DatabaseError, InterfaceError

from service_api.config import RuntimeConfig
from service_api.constants import APP_NAME
from service_api.services.logger.logger import app_logger


class Aiopg:
    _engine = None

    @classmethod
    def get_dns(cls):
        _dsn = (
            f"user={RuntimeConfig.PG_USER} "
            f"password={RuntimeConfig.PG_PASSWORD} "
            f"host={RuntimeConfig.PG_HOST} "
            f"port={RuntimeConfig.PG_PORT} "
            f"dbname={RuntimeConfig.PG_NAME} "
            f"application_name={APP_NAME}:{RuntimeConfig.APP_RUNTIME_ID} "
            f"options='-c search_path={RuntimeConfig.PG_SCHEMA}'"
        )
        return _dsn

    @classmethod
    async def get_engine(cls):
        if cls.is_closed():
            await cls.connect()
        return cls._engine

    @classmethod
    def is_closed(cls):
        return not bool(cls._engine) or cls._engine.closed

    @classmethod
    async def connect(cls, loop=None):
        cls._engine = await create_engine(cls.get_dns(), maxsize=2, loop=loop, echo=RuntimeConfig.PG_ECHO)

    @classmethod
    async def close(cls):
        if cls._engine is not None:
            try:
                cls._engine.close()
                await cls._engine.wait_closed()
            except (DatabaseError, InterfaceError):
                app_logger.exception("Engine failed to close.")
            finally:
                cls._engine = None

    @classmethod
    async def scalars(cls, stmt):
        engine = await cls.get_engine()
        async with engine.acquire() as conn:
            async with conn.execute(stmt) as cur:
                result = await cur.fetchall()
        return list(map(op.itemgetter(0), result))

    @classmethod
    async def execute(cls, stmt):
        engine = await cls.get_engine()
        async with engine.acquire() as conn:
            return await conn.execute(stmt)

    @classmethod
    async def fetchall(cls, stmt):
        engine = await cls.get_engine()
        async with engine.acquire() as conn:
            async with conn.execute(stmt) as cur:
                result = await cur.fetchall()
        return list(map(dict, result))

    @classmethod
    async def fetchone(cls, stmt):
        engine = await cls.get_engine()
        async with engine.acquire() as conn:
            async with conn.execute(stmt) as cur:
                result = await cur.fetchone()
        return dict(result) if result is not None else {}


class Database(Aiopg):
    pass
