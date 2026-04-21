# elabftw-cli

A command-line interface for the [elabFTW](https://www.elabftw.net/) REST API v2, designed for use by AI agents and automation scripts. All output is JSON on stdout, errors go to stderr, and the exit code is always 0 on success or 1 on failure.

## Installation

```bash
pip install -e .
```

Requires Python 3.11+.

## Authentication

Set credentials via environment variables (recommended for agents and CI):

```bash
export ELABFTW_BASE_URL=https://your-elab-instance.example.org
export ELABFTW_API_KEY=your-api-key-here
```

Or place them in `~/.elabftw.toml` (env vars take precedence):

```toml
base_url = "https://your-elab-instance.example.org"
api_key  = "your-api-key-here"
```

A template is provided at `elabftw.toml.example`.

## Usage

```
elabftw <resource> <command> [OPTIONS] [ARGS]
```

Run `elabftw --help` or `elabftw <resource> --help` at any level for full option listings.

### Experiments

```bash
elabftw experiments list                          # list all experiments
elabftw experiments list --search "crispr" --limit 10
elabftw experiments get 42                        # get by ID
elabftw experiments create --title "My experiment"
elabftw experiments create --title "My experiment" --body "<p>Notes</p>" --category-id 3
elabftw experiments patch 42 --title "Updated title"
elabftw experiments patch 42 --status "finished"
elabftw experiments delete 42
```

### Items

```bash
elabftw items list
elabftw items list --search "buffer" --limit 20
elabftw items get 7
elabftw items create --title "PBS 1x" --category-id 2
elabftw items patch 7 --title "PBS 1x (updated)"
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

Teamgroups are nested under a team — all commands require the team ID as the first argument.

```bash
elabftw teamgroups list 1                        # list teamgroups in team 1
elabftw teamgroups get 1 3                       # get teamgroup 3 in team 1
elabftw teamgroups create 1 --name "PhD students"
elabftw teamgroups rename 1 3 --name "MSc students"
elabftw teamgroups add-user 1 3 --user-id 7
elabftw teamgroups remove-user 1 3 --user-id 7
elabftw teamgroups delete 1 3
```

## API coverage

See [API_COVERAGE.md](API_COVERAGE.md) for a full breakdown of which elabFTW API endpoints are implemented.

## Output format

Every command prints JSON to stdout:

- **list** → JSON array
- **get / create** → JSON object
- **patch / delete** → `{"ok": true}`

Errors print a message to stderr and exit with code 1.
