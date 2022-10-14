from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware

from service_api.services.middlewares.authentication_middleware import BasicAuthBackend, on_auth_error


origins = [
    "http://localhost:3000",
    "localhost:3000",
    "*"
]


def init_middlewares(app):
    app.add_middleware(AuthenticationMiddleware, backend=BasicAuthBackend(), on_error=on_auth_error)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    ),


__all__ = (
    "init_middlewares"
)
