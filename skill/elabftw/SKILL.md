---
name: elabftw
description: Interact with an elabFTW electronic lab notebook via the `elabftw` CLI — list, read, create, patch, and delete experiments, items (resources), users, teams, and teamgroups. Use whenever the user wants to query or modify elabFTW data. All output is JSON.
---

# elabFTW CLI

`elabftw` is a command-line client for the elabFTW REST API v2. Every command prints
**JSON to stdout**, errors go to **stderr**, and the **exit code** is `0` on success or
`1` on failure — so you can parse stdout directly and branch on the exit code.

## Setup

The CLI must be installed and authenticated before use.

**Install** (isolated, puts `elabftw` on PATH):

```bash
uv tool install git+https://github.com/ADAorg/elabftw-cli
# or: pipx install git+https://github.com/ADAorg/elabftw-cli
```

**Authenticate** with environment variables (preferred for agents):

```bash
export ELABFTW_BASE_URL=https://your-elab-instance.example.org
export ELABFTW_API_KEY=your-api-key-here
```

Env vars take precedence over `~/.elabftw.toml` (which has the same `base_url` / `api_key`
keys). If credentials are missing, commands exit `1` with a message on stderr — check
that the two env vars are set before assuming a command is broken.

## Usage

```
elabftw <resource> <command> [OPTIONS] [ARGS]
```

Run `elabftw --help` or `elabftw <resource> --help` for the authoritative option list at
any level. Output conventions:

- **list** → JSON array
- **get / create** → JSON object
- **patch / delete** → `{"ok": true}`

### Experiments

```bash
elabftw experiments list
elabftw experiments list --search "crispr" --limit 10
elabftw experiments get 42
elabftw experiments create --title "My experiment"
elabftw experiments create --title "My experiment" --body "<p>Notes</p>" --category-id 3
elabftw experiments create --title "My experiment" --template-id 7   # create from a template
elabftw experiments patch 42 --title "Updated title"
elabftw experiments patch 42 --status "finished"
elabftw experiments patch 42 --bodyappend "<h2>2026-09-02</h2><p>Progress notes...</p>"
elabftw experiments upload 42 --file results.png --comment "figure 1"
elabftw experiments delete 42
```

`--category-id` sets the experiment's *category* (a classification), not a template.
Use `--template-id` to create from a template — resolve the ID by name first with
`elabftw experiments-templates list` (see below). Prefer `--bodyappend` over `--body`
once an entry already has content: `--body` replaces the whole body, `--bodyappend`
adds to it — the right choice for a notebook entry written to incrementally over time.

### Templates

Read-only from the CLI — create/edit templates in the elabFTW UI.

```bash
elabftw experiments-templates list
elabftw experiments-templates list --search "AgendoProject"
elabftw experiments-templates get 7
```

### Items (resources)

```bash
elabftw items list
elabftw items list --search "buffer" --limit 20
elabftw items get 7
elabftw items create --title "PBS 1x" --category-id 2
elabftw items patch 7 --title "PBS 1x (updated)"
elabftw items patch 7 --bodyappend "<p>Restocked 2026-09-02.</p>"
elabftw items upload 7 --file coa.pdf --comment "certificate of analysis"
elabftw items delete 7
```

### Users

```bash
elabftw users list
elabftw users list --team 1 --only-admins
elabftw users get 5
elabftw users create --firstname Alice --lastname Smith --email alice@example.org
elabftw users create --firstname Bob --lastname Jones --email bob@example.org --team 1 --usergroup 2
elabftw users patch 5 --email new@example.org
elabftw users patch 5 --valid-until 2026-12-31
```

`--usergroup`: `1` = Sysadmin, `2` = Admin, `4` = User (default).

### Teams

```bash
elabftw teams list            # requires Sysadmin
elabftw teams get 1
elabftw teams get current     # requester's current team
elabftw teams create --name "Biology Lab"
elabftw teams patch 1 --name "Biochemistry Lab"
elabftw teams patch current --announcement "Lab meeting Friday 14:00"
```

### Teamgroups

Teamgroups are nested under a team — every command takes the team ID as the first argument.

```bash
elabftw teamgroups list 1
elabftw teamgroups get 1 3
elabftw teamgroups create 1 --name "PhD students"
elabftw teamgroups rename 1 3 --name "MSc students"
elabftw teamgroups add-user 1 3 --user-id 7
elabftw teamgroups remove-user 1 3 --user-id 7
elabftw teamgroups delete 1 3
```

## Guidance for agents

- **Parse stdout as JSON.** Don't screen-scrape; the shape is stable (array / object / `{"ok": true}`).
- **Check the exit code.** Non-zero means failure — read stderr for the reason rather than retrying blindly.
- **`delete` is destructive and not reversible.** Confirm the target ID with the user before deleting experiments, items, users, or teamgroups.
- **Permissions matter.** Some commands (e.g. `teams list`, user creation) require Sysadmin/Admin rights; a `1` exit with a permissions message means the API key lacks the role, not that the CLI is broken.
- **Discover options at runtime** with `--help` instead of guessing flags.
- **Resolve template names to IDs first.** There's no `--template` by name — use
  `elabftw experiments-templates list --search "<name>"` and pass the matching `id` to
  `experiments create --template-id`.
