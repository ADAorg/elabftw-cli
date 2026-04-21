import typer

from elabftw_cli.commands import experiments, items, teams, teamgroups, users

app = typer.Typer(
    name="elabftw",
    help="CLI for the elabFTW API. Output is always JSON on stdout.",
    no_args_is_help=True,
)

app.add_typer(experiments.app, name="experiments")
app.add_typer(items.app, name="items")
app.add_typer(users.app, name="users")
app.add_typer(teams.app, name="teams")
app.add_typer(teamgroups.app, name="teamgroups")


def main() -> None:
    app()
