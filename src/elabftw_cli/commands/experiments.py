from __future__ import annotations

import json
import sys
from typing import Optional

import typer

from elabftw_cli import config, client as _client

app = typer.Typer(help="Manage experiments.")


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
    """List experiments."""
    c = _client_from_ctx()
    _out(c.get("/experiments", limit=limit, offset=offset, q=search))


@app.command()
def get(id: int = typer.Argument(..., help="Experiment ID.")) -> None:
    """Get a single experiment by ID."""
    c = _client_from_ctx()
    _out(c.get(f"/experiments/{id}"))


@app.command()
def create(
    title: str = typer.Option(..., "--title", "-t", help="Experiment title."),
    body: Optional[str] = typer.Option(None, "--body", "-b", help="Experiment body (HTML or plain text)."),
    category_id: Optional[int] = typer.Option(None, "--category-id", help="Experiment category ID (classification, not a template)."),
    template_id: Optional[int] = typer.Option(
        None,
        "--template-id",
        help=(
            "Template ID to create the experiment from (see `elabftw experiments-templates list`). "
            "0 uses the team's common template, -1 (the API default) creates an empty body."
        ),
    ),
) -> None:
    """Create a new experiment."""
    c = _client_from_ctx()
    payload: dict = {"title": title}
    if body is not None:
        payload["body"] = body
    if category_id is not None:
        payload["category"] = category_id
    if template_id is not None:
        payload["template"] = template_id
    _out(c.post("/experiments", payload))


@app.command()
def patch(
    id: int = typer.Argument(..., help="Experiment ID."),
    title: Optional[str] = typer.Option(None, "--title", "-t", help="New title."),
    body: Optional[str] = typer.Option(None, "--body", "-b", help="New body (replaces the existing body)."),
    bodyappend: Optional[str] = typer.Option(
        None, "--bodyappend", help="Append content (HTML or plain text) to the existing body instead of replacing it."
    ),
    status: Optional[str] = typer.Option(None, "--status", help="New status."),
) -> None:
    """Update an experiment."""
    payload: dict = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if bodyappend is not None:
        payload["bodyappend"] = bodyappend
    if status is not None:
        payload["status"] = status
    if not payload:
        print("error: at least one field to update must be provided", file=sys.stderr)
        raise SystemExit(1)
    c = _client_from_ctx()
    _out(c.patch(f"/experiments/{id}", payload))


@app.command()
def delete(id: int = typer.Argument(..., help="Experiment ID.")) -> None:
    """Delete an experiment."""
    c = _client_from_ctx()
    c.delete(f"/experiments/{id}")
    _out({"ok": True})


@app.command()
def upload(
    id: int = typer.Argument(..., help="Experiment ID."),
    file: str = typer.Option(..., "--file", "-f", help="Path to the file to attach."),
    comment: Optional[str] = typer.Option(None, "--comment", "-c", help="Optional comment for the attached file."),
) -> None:
    """Attach a file to an experiment."""
    c = _client_from_ctx()
    _out(c.post_multipart(f"/experiments/{id}/uploads", file, comment))
