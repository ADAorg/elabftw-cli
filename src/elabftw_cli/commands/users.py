from __future__ import annotations

import json
import sys
from typing import Optional

import typer

from elabftw_cli import config, client as _client

app = typer.Typer(help="Manage users.")


def _c() -> _client.ElabClient:
    base_url, api_key = config.load()
    return _client.ElabClient(base_url, api_key)


def _out(data: object) -> None:
    print(json.dumps(data, indent=2))


@app.command()
def list(
    team: Optional[int] = typer.Option(None, "--team", help="Filter by team ID."),
    current_team: bool = typer.Option(False, "--current-team", help="Filter by requester's current team."),
    only_admins: bool = typer.Option(False, "--only-admins", help="Return only team admins."),
    only_archived: bool = typer.Option(False, "--only-archived", help="Return only archived users."),
) -> None:
    """List users."""
    c = _c()
    _out(c.get(
        "/users",
        team=team,
        currentTeam=1 if current_team else None,
        onlyAdmins=only_admins or None,
        onlyArchived=only_archived or None,
    ))


@app.command()
def get(id: int = typer.Argument(..., help="User ID.")) -> None:
    """Get a single user by ID."""
    c = _c()
    _out(c.get(f"/users/{id}"))


@app.command()
def create(
    firstname: str = typer.Option(..., "--firstname", help="First name."),
    lastname: str = typer.Option(..., "--lastname", help="Last name."),
    email: str = typer.Option(..., "--email", help="Email address."),
    team: Optional[int] = typer.Option(None, "--team", help="Team ID to add the user to."),
    usergroup: Optional[int] = typer.Option(None, "--usergroup", help="Permission level: 1=Sysadmin, 2=Admin, 4=User (default)."),
    valid_until: Optional[str] = typer.Option(None, "--valid-until", help="Account expiry date (YYYY-MM-DD)."),
    orgid: Optional[str] = typer.Option(None, "--orgid", help="Internal organisation ID."),
) -> None:
    """Create a new user."""
    c = _c()
    payload: dict = {"firstname": firstname, "lastname": lastname, "email": email}
    if team is not None:
        payload["team"] = team
    if usergroup is not None:
        payload["usergroup"] = usergroup
    if valid_until is not None:
        payload["valid_until"] = valid_until
    if orgid is not None:
        payload["orgid"] = orgid
    _out(c.post("/users", payload))


@app.command()
def patch(
    id: int = typer.Argument(..., help="User ID."),
    firstname: Optional[str] = typer.Option(None, "--firstname", help="New first name."),
    lastname: Optional[str] = typer.Option(None, "--lastname", help="New last name."),
    email: Optional[str] = typer.Option(None, "--email", help="New email address."),
    orcid: Optional[str] = typer.Option(None, "--orcid", help="ORCID identifier."),
    valid_until: Optional[str] = typer.Option(None, "--valid-until", help="Account expiry date (YYYY-MM-DD)."),
    orgid: Optional[str] = typer.Option(None, "--orgid", help="Internal organisation ID."),
) -> None:
    """Update a user."""
    payload: dict = {}
    if firstname is not None:
        payload["firstname"] = firstname
    if lastname is not None:
        payload["lastname"] = lastname
    if email is not None:
        payload["email"] = email
    if orcid is not None:
        payload["orcid"] = orcid
    if valid_until is not None:
        payload["valid_until"] = valid_until
    if orgid is not None:
        payload["orgid"] = orgid
    if not payload:
        print("error: at least one field to update must be provided", file=sys.stderr)
        raise SystemExit(1)
    c = _c()
    _out(c.patch(f"/users/{id}", payload))
