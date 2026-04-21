from __future__ import annotations

import os
import sys
import tomllib
from pathlib import Path


def load() -> tuple[str, str]:
    """Return (base_url, api_key). Env vars take precedence over ~/.elabftw.toml."""
    base_url = os.environ.get("ELABFTW_BASE_URL")
    api_key = os.environ.get("ELABFTW_API_KEY")

    if not base_url or not api_key:
        cfg_path = Path.home() / ".elabftw.toml"
        if cfg_path.exists():
            with cfg_path.open("rb") as f:
                cfg = tomllib.load(f)
            base_url = base_url or cfg.get("base_url")
            api_key = api_key or cfg.get("api_key")

    missing = []
    if not base_url:
        missing.append("ELABFTW_BASE_URL (env) or base_url (config)")
    if not api_key:
        missing.append("ELABFTW_API_KEY (env) or api_key (config)")

    if missing:
        print(
            "error: missing configuration:\n  " + "\n  ".join(missing),
            file=sys.stderr,
        )
        raise SystemExit(1)

    return base_url, api_key
