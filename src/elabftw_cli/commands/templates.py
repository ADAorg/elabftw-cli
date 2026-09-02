from __future__ import annotations

import json
from typing import Optional

import typer

from elabftw_cli import config, client as _client

app = typer.Typer(help="Browse experiment templates (read-only).")


def _client_from_ctx() -> _client.ElabClient:
    base_url, api_key = config.load()
    return _client.ElabClient(base_url, api_key)


def _out(data: object) -> None:
    print(json.dumps(data, indent=2))


@app.command()
def list(
    limit: Optional[int] = typer.Option(None, "--limit", "-l", help="Max results to return."),
    offset: Optional[int] = typer.Option(None, "--offset", help="Pagination offset."),
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Search query."),
) -> None:
    """List experiment templates. Use this to resolve a template's ID from its title,
    e.g. before `elabftw experiments create --template-id <id>`."""
    c = _client_from_ctx()
    _out(c.get("/experiments_templates", limit=limit, offset=offset, q=search))


@app.command()
def get(id: int = typer.Argument(..., help="Template ID.")) -> None:
    """Get a single experiment template by ID."""
    c = _client_from_ctx()
    _out(c.get(f"/experiments_templates/{id}"))
