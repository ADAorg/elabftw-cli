from __future__ import annotations

import json
import sys
from typing import Optional

import typer

from elabftw_cli import config, client as _client

app = typer.Typer(help="Manage items (database entries).")


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
    """List items."""
    c = _client_from_ctx()
    _out(c.get("/items", limit=limit, offset=offset, q=search))


@app.command()
def get(id: int = typer.Argument(..., help="Item ID.")) -> None:
    """Get a single item by ID."""
    c = _client_from_ctx()
    _out(c.get(f"/items/{id}"))


@app.command()
def create(
    title: str = typer.Option(..., "--title", "-t", help="Item title."),
    body: Optional[str] = typer.Option(None, "--body", "-b", help="Item body (HTML or plain text)."),
    category_id: Optional[int] = typer.Option(None, "--category-id", help="Item category ID."),
) -> None:
    """Create a new item."""
    c = _client_from_ctx()
    payload: dict = {"title": title}
    if body is not None:
        payload["body"] = body
    if category_id is not None:
        payload["category_id"] = category_id
    _out(c.post("/items", payload))


@app.command()
def patch(
    id: int = typer.Argument(..., help="Item ID."),
    title: Optional[str] = typer.Option(None, "--title", "-t", help="New title."),
    body: Optional[str] = typer.Option(None, "--body", "-b", help="New body."),
) -> None:
    """Update an item."""
    payload: dict = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if not payload:
        print("error: at least one field to update must be provided", file=sys.stderr)
        raise SystemExit(1)
    c = _client_from_ctx()
    _out(c.patch(f"/items/{id}", payload))


@app.command()
def delete(id: int = typer.Argument(..., help="Item ID.")) -> None:
    """Delete an item."""
    c = _client_from_ctx()
    c.delete(f"/items/{id}")
    _out({"ok": True})
