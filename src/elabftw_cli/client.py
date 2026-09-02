from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Optional

import httpx


class ElabClient:
    def __init__(self, base_url: str, api_key: str) -> None:
        self._http = httpx.Client(
            base_url=base_url.rstrip("/") + "/api/v2",
            headers={
                "Authorization": api_key,
                "Accept": "application/json",
                # No default Content-Type here: httpx sets it per-request based on
                # whether the call uses json= (application/json) or files=
                # (multipart/form-data; boundary=...). A fixed default would force
                # every request - including uploads - onto application/json.
            },
            timeout=30,
        )

    def get(self, path: str, **params: Any) -> Any:
        resp = self._http.get(path, params={k: v for k, v in params.items() if v is not None})
        self._raise(resp)
        return resp.json()

    def post(self, path: str, body: dict[str, Any]) -> dict[str, Any]:
        resp = self._http.post(path, json=body)
        self._raise(resp)
        if resp.status_code == 201:
            location = resp.headers.get("Location", "")
            resource_id = location.rstrip("/").split("/")[-1] if location else None
            try:
                return resp.json()
            except Exception:
                return {"id": int(resource_id)} if resource_id and resource_id.isdigit() else {"ok": True}
        try:
            return resp.json()
        except Exception:
            return {"ok": True}

    def patch(self, path: str, body: dict[str, Any]) -> dict[str, Any]:
        resp = self._http.patch(path, json=body)
        self._raise(resp)
        try:
            return resp.json()
        except Exception:
            return {"ok": True}

    def delete(self, path: str) -> None:
        resp = self._http.delete(path)
        self._raise(resp)

    def post_multipart(self, path: str, file_path: str, comment: Optional[str] = None) -> dict[str, Any]:
        p = Path(file_path)
        if not p.is_file():
            print(f"error: file not found: {file_path}", file=sys.stderr)
            raise SystemExit(1)
        data = {"comment": comment} if comment is not None else None
        with p.open("rb") as fh:
            resp = self._http.post(path, files={"file": (p.name, fh)}, data=data)
        self._raise(resp)
        if resp.status_code == 201:
            location = resp.headers.get("Location", "")
            resource_id = location.rstrip("/").split("/")[-1] if location else None
            try:
                return resp.json()
            except Exception:
                return {"id": int(resource_id)} if resource_id and resource_id.isdigit() else {"ok": True}
        try:
            return resp.json()
        except Exception:
            return {"ok": True}

    @staticmethod
    def _raise(resp: httpx.Response) -> None:
        if resp.is_error:
            try:
                detail = resp.json()
            except Exception:
                detail = resp.text
            print(f"error: HTTP {resp.status_code}: {detail}", file=sys.stderr)
            raise SystemExit(1)
