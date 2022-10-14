import click

from service_api.app import sanic_app
from service_api.config import RuntimeConfig


@click.group()
def cli():
    pass


@cli.command("runserver")
@click.option("-h", "--host", default="0.0.0.0")
@click.option("-p", "--port", default=5001)
@click.option(
    "-f", "--fast", type=bool, default=False,
    help=(
            "Get the maximum CPU performance. "
            "This will automatically run the maximum number of workers given the system constraints."
    )
)
@click.option("--debug", default=RuntimeConfig.DEBUG)
def runserver(host, port, fast, debug):
    conf = {
        "host": host,
        "port": port,
        "debug": debug,
        "auto_reload": debug,
        "access_log": debug,
        "fast": fast,
    }
    sanic_app.run(**conf)


if __name__ == "__main__":
    cli()
