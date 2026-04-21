from __future__ import annotations

import json
import sys
from typing import Optional

import typer

from elabftw_cli import config, client as _client

app = typer.Typer(help="Manage teamgroups (nested under a team).")


def _c() -> _client.ElabClient:
    base_url, api_key = config.load()
    return _client.ElabClient(base_url, api_key)


def _out(data: object) -> None:
    print(json.dumps(data, indent=2))


@app.command()
def list(team_id: int = typer.Argument(..., help="Team ID.")) -> None:
    """List teamgroups for a team."""
    c = _c()
    _out(c.get(f"/teams/{team_id}/teamgroups"))


@app.command()
def get(
    team_id: int = typer.Argument(..., help="Team ID."),
    id: int = typer.Argument(..., help="Teamgroup ID."),
) -> None:
    """Get a single teamgroup."""
    c = _c()
    _out(c.get(f"/teams/{team_id}/teamgroups/{id}"))


@app.command()
def create(
    team_id: int = typer.Argument(..., help="Team ID."),
    name: str = typer.Option(..., "--name", "-n", help="Teamgroup name."),
) -> None:
    """Create a new teamgroup."""
    c = _c()
    _out(c.post(f"/teams/{team_id}/teamgroups", {"name": name}))


@app.command()
def rename(
    team_id: int = typer.Argument(..., help="Team ID."),
    id: int = typer.Argument(..., help="Teamgroup ID."),
    name: str = typer.Option(..., "--name", "-n", help="New teamgroup name."),
) -> None:
    """Rename a teamgroup."""
    c = _c()
    _out(c.patch(f"/teams/{team_id}/teamgroups/{id}", {"name": name}))


@app.command()
def add_user(
    team_id: int = typer.Argument(..., help="Team ID."),
    id: int = typer.Argument(..., help="Teamgroup ID."),
    user_id: int = typer.Option(..., "--user-id", help="User ID to add."),
) -> None:
    """Add a user to a teamgroup."""
    c = _c()
    _out(c.patch(f"/teams/{team_id}/teamgroups/{id}", {"how": "add", "userid": user_id}))


@app.command()
def remove_user(
    team_id: int = typer.Argument(..., help="Team ID."),
    id: int = typer.Argument(..., help="Teamgroup ID."),
    user_id: int = typer.Option(..., "--user-id", help="User ID to remove."),
) -> None:
    """Remove a user from a teamgroup."""
    c = _c()
    _out(c.patch(f"/teams/{team_id}/teamgroups/{id}", {"how": "unreference", "userid": user_id}))


@app.command()
def delete(
    team_id: int = typer.Argument(..., help="Team ID."),
    id: int = typer.Argument(..., help="Teamgroup ID."),
) -> None:
    """Delete a teamgroup."""
    c = _c()
    c.delete(f"/teams/{team_id}/teamgroups/{id}")
    _out({"ok": True})
