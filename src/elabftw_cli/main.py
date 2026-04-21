import typer

from elabftw_cli.commands import experiments, items

app = typer.Typer(
    name="elabftw",
    help="CLI for the elabFTW API. Output is always JSON on stdout.",
    no_args_is_help=True,
)

app.add_typer(experiments.app, name="experiments")
app.add_typer(items.app, name="items")


def main() -> None:
    app()
