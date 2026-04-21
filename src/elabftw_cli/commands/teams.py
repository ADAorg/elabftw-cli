from __future__ import annotations

import json
import sys
from typing import Optional

import typer

from elabftw_cli import config, client as _client

app = typer.Typer(help="Manage teams.")


def _c() -> _client.ElabClient:
    base_url, api_key = config.load()
    return _client.ElabClient(base_url, api_key)


def _out(data: object) -> None:
    print(json.dumps(data, indent=2))


@app.command()
def list() -> None:
    """List all teams. Requires Sysadmin permissions."""
    c = _c()
    _out(c.get("/teams"))


@app.command()
def get(id: str = typer.Argument(..., help="Team ID or 'current'.")) -> None:
    """Get a single team by ID (or 'current')."""
    c = _c()
    _out(c.get(f"/teams/{id}"))


@app.command()
def create(
    name: str = typer.Option(..., "--name", "-n", help="Team name."),
) -> None:
    """Create a new team. Requires Sysadmin permissions."""
    c = _c()
    _out(c.post("/teams", {"name": name}))


@app.command()
def patch(
    id: str = typer.Argument(..., help="Team ID or 'current'."),
    name: Optional[str] = typer.Option(None, "--name", "-n", help="New team name."),
    announcement: Optional[str] = typer.Option(None, "--announcement", help="Announcement text shown to all team members."),
    orgid: Optional[str] = typer.Option(None, "--orgid", help="Organisation ID."),
    visible: Optional[int] = typer.Option(None, "--visible", help="Visibility flag (0 or 1)."),
) -> None:
    """Update a team."""
    payload: dict = {}
    if name is not None:
        payload["name"] = name
    if announcement is not None:
        payload["announcement"] = announcement
    if orgid is not None:
        payload["orgid"] = orgid
    if visible is not None:
        payload["visible"] = visible
    if not payload:
        print("error: at least one field to update must be provided", file=sys.stderr)
        raise SystemExit(1)
    c = _c()
    _out(c.patch(f"/teams/{id}", payload))
