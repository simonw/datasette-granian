from datasette import hookimpl
from granian.server import Granian
from granian.constants import HTTPModes, Interfaces, Loops, ThreadModes
from granian.log import LogLevels
import click
import json


def load_app(target):
    from datasette import cli

    ds_kwargs = json.loads(target)
    ds = cli.serve.callback(**ds_kwargs)
    return ds.app()


invalid_options = {
    "get",
    "root",
    "open_browser",
    "uds",
    "reload",
    "pdb",
    # TODO: These should work actually
    "ssl_keyfile",
    "ssl_certfile",
}


def serve_with_granian(**kwargs):
    from datasette import cli

    workers = kwargs.pop("workers")
    port = kwargs["port"]
    host = kwargs["host"]
    # Need to add back default kwargs for everything in invalid_options:
    kwargs.update({invalid_option: None for invalid_option in invalid_options})
    kwargs["return_instance"] = True

    srv = Granian(
        # Pass kwars as serialized JSON to the subprocess
        json.dumps(kwargs),
        address=host,
        port=port,
        interface=Interfaces.ASGI,
        workers=workers,
        threads=1,
        pthreads=1,
        threading_mode=ThreadModes.workers.value,
        loop=Loops.auto.value,
        http=HTTPModes.auto.value,
        websockets=True,
        backlog=1024,
        log_level=LogLevels.info.value,
        ssl_cert=None,
        ssl_key=None,
    )
    srv.serve(target_loader=load_app)


@hookimpl
def register_commands(cli):
    serve_command = cli.commands["serve"]
    params = [
        param for param in serve_command.params if param.name not in invalid_options
    ]
    params.append(
        click.Option(
            ["-w", "--workers"],
            type=int,
            default=1,
            help="Number of Granian workers",
            show_default=True,
        )
    )
    granian_command = click.Command(
        name="granian",
        params=params,
        callback=serve_with_granian,
        short_help="Serve Datasette using Granian",
        help="Start a Granian server running to serve Datasette",
    )
    cli.add_command(granian_command, name="granian")
