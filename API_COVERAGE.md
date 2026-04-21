# elabFTW API Coverage

Tracks which REST API v2 endpoints are implemented in the CLI.

Legend: ✅ covered · ⬜ not implemented

---

## Experiments

| Method | Endpoint | CLI command | Status |
|--------|----------|-------------|--------|
| GET | /experiments | `elabftw experiments list` | ✅ |
| POST | /experiments | `elabftw experiments create` | ✅ |
| GET | /experiments/{id} | `elabftw experiments get <id>` | ✅ |
| PATCH | /experiments/{id} | `elabftw experiments patch <id>` | ✅ |
| DELETE | /experiments/{id} | `elabftw experiments delete <id>` | ✅ |
| POST | /experiments/{id} | duplicate / action endpoint | ⬜ |

## Items

| Method | Endpoint | CLI command | Status |
|--------|----------|-------------|--------|
| GET | /items | `elabftw items list` | ✅ |
| POST | /items | `elabftw items create` | ✅ |
| GET | /items/{id} | `elabftw items get <id>` | ✅ |
| PATCH | /items/{id} | `elabftw items patch <id>` | ✅ |
| DELETE | /items/{id} | `elabftw items delete <id>` | ✅ |
| POST | /items/{id} | duplicate / action endpoint | ⬜ |

---

## Sub-resources (entity-scoped)

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /{entity_type}/{id}/comments | ⬜ |
| GET | /{entity_type}/{id}/comments/{subid} | ⬜ |
| POST | /{entity_type}/{id}/comments | ⬜ |
| PATCH | /{entity_type}/{id}/comments/{subid} | ⬜ |
| DELETE | /{entity_type}/{id}/comments/{subid} | ⬜ |
| GET | /{entity_type}/{id}/revisions | ⬜ |
| GET | /{entity_type}/{id}/revisions/{subid} | ⬜ |
| PATCH | /{entity_type}/{id}/revisions/{subid} | ⬜ |

## Uploads

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /uploads | ⬜ |
| POST | /uploads | ⬜ |
| GET | /uploads/{id} | ⬜ |
| PATCH | /uploads/{id} | ⬜ |
| DELETE | /uploads/{id} | ⬜ |
| POST | /uploads/replace | ⬜ |
| GET | /user-uploads | ⬜ |

## Tags

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /tags | ⬜ |
| POST | /tags | ⬜ |
| GET | /tags/{id} | ⬜ |
| PATCH | /tags/{id} | ⬜ |
| DELETE | /tags/{id} | ⬜ |
| GET | /team-tags | ⬜ |
| POST | /team-tags | ⬜ |
| GET | /team-tags/{id} | ⬜ |
| PATCH | /team-tags/{id} | ⬜ |
| DELETE | /team-tags/{id} | ⬜ |
| GET | /favorite-tags | ⬜ |
| POST | /favorite-tags | ⬜ |
| DELETE | /favorite-tags/{id} | ⬜ |

## Steps

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /steps | ⬜ |
| POST | /steps | ⬜ |
| PATCH | /steps/{id} | ⬜ |
| DELETE | /steps/{id} | ⬜ |
| GET | /unfinished-steps | ⬜ |

## Links

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /experiments-links | ⬜ |
| POST | /experiments-links | ⬜ |
| DELETE | /experiments-links/{id} | ⬜ |
| GET | /items-links | ⬜ |
| POST | /items-links | ⬜ |
| DELETE | /items-links/{id} | ⬜ |
| GET | /compounds-links | ⬜ |
| POST | /compounds-links | ⬜ |
| DELETE | /compounds-links/{id} | ⬜ |

## Templates

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /experiments-templates | ⬜ |
| POST | /experiments-templates | ⬜ |
| GET | /experiments-templates/{id} | ⬜ |
| PATCH | /experiments-templates/{id} | ⬜ |
| DELETE | /experiments-templates/{id} | ⬜ |
| POST | /experiments-templates/{id} | ⬜ |
| GET | /items-types | ⬜ |
| POST | /items-types | ⬜ |
| GET | /items-types/{id} | ⬜ |
| PATCH | /items-types/{id} | ⬜ |
| DELETE | /items-types/{id} | ⬜ |
| POST | /items-types/{id} | ⬜ |

## Categories & Status

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /experiments-categories | ⬜ |
| POST | /experiments-categories | ⬜ |
| GET | /experiments-categories/{id} | ⬜ |
| PATCH | /experiments-categories/{id} | ⬜ |
| DELETE | /experiments-categories/{id} | ⬜ |
| GET | /experiments-status | ⬜ |
| POST | /experiments-status | ⬜ |
| GET | /experiments-status/{id} | ⬜ |
| PATCH | /experiments-status/{id} | ⬜ |
| DELETE | /experiments-status/{id} | ⬜ |
| GET | /resources-categories | ⬜ |
| POST | /resources-categories | ⬜ |
| GET | /resources-categories/{id} | ⬜ |
| PATCH | /resources-categories/{id} | ⬜ |
| DELETE | /resources-categories/{id} | ⬜ |
| GET | /resources-status | ⬜ |
| POST | /resources-status | ⬜ |
| GET | /resources-status/{id} | ⬜ |
| PATCH | /resources-status/{id} | ⬜ |
| DELETE | /resources-status/{id} | ⬜ |

## Compounds

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /compounds | ⬜ |
| POST | /compounds | ⬜ |
| GET | /compounds/{id} | ⬜ |
| DELETE | /compounds/{id} | ⬜ |

## Users & Teams

| Method | Endpoint | CLI command | Status |
|--------|----------|-------------|--------|
| GET | /users | `elabftw users list` | ✅ |
| POST | /users | `elabftw users create` | ✅ |
| GET | /users/{id} | `elabftw users get <id>` | ✅ |
| PATCH | /users/{id} | `elabftw users patch <id>` | ✅ |
| GET | /teams | `elabftw teams list` | ✅ |
| POST | /teams | `elabftw teams create` | ✅ |
| GET | /teams/{id} | `elabftw teams get <id>` | ✅ |
| PATCH | /teams/{id} | `elabftw teams patch <id>` | ✅ |
| GET | /teams/{id}/teamgroups | `elabftw teamgroups list <team_id>` | ✅ |
| POST | /teams/{id}/teamgroups | `elabftw teamgroups create <team_id>` | ✅ |
| GET | /teams/{id}/teamgroups/{subid} | `elabftw teamgroups get <team_id> <id>` | ✅ |
| PATCH | /teams/{id}/teamgroups/{subid} | `elabftw teamgroups rename / add-user / remove-user` | ✅ |
| DELETE | /teams/{id}/teamgroups/{subid} | `elabftw teamgroups delete <team_id> <id>` | ✅ |

## Notifications & Todo

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /notifications | ⬜ |
| GET | /notifications/{id} | ⬜ |
| PATCH | /notifications/{id} | ⬜ |
| DELETE | /notifications/{id} | ⬜ |
| GET | /todolist | ⬜ |
| POST | /todolist | ⬜ |
| GET | /todolist/{id} | ⬜ |
| PATCH | /todolist/{id} | ⬜ |
| DELETE | /todolist/{id} | ⬜ |

## Events & Calendar

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /events | ⬜ |
| POST | /events | ⬜ |
| GET | /events/{id} | ⬜ |
| PATCH | /events/{id} | ⬜ |
| DELETE | /events/{id} | ⬜ |

## Storage & Containers

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /containers | ⬜ |
| POST | /containers | ⬜ |
| GET | /containers/{id} | ⬜ |
| PATCH | /containers/{id} | ⬜ |
| DELETE | /containers/{id} | ⬜ |
| GET | /storage-units | ⬜ |
| POST | /storage-units | ⬜ |
| GET | /storage-units/{id} | ⬜ |
| PATCH | /storage-units/{id} | ⬜ |
| DELETE | /storage-units/{id} | ⬜ |

## API Keys

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /apikeys | ⬜ |
| POST | /apikeys | ⬜ |
| DELETE | /apikeys/{id} | ⬜ |

## Config & Admin

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /config | ⬜ |
| PATCH | /config | ⬜ |
| DELETE | /config | ⬜ |
| GET | /info | ⬜ |
| GET | /reports | ⬜ |
| GET | /extra-fields-keys | ⬜ |
| GET | /idps | ⬜ |
| POST | /idps | ⬜ |
| GET | /idps/{id} | ⬜ |
| PATCH | /idps/{id} | ⬜ |
| DELETE | /idps/{id} | ⬜ |
| GET | /idps-sources | ⬜ |
| POST | /idps-sources | ⬜ |
| GET | /idps-sources/{id} | ⬜ |
| PATCH | /idps-sources/{id} | ⬜ |
| DELETE | /idps-sources/{id} | ⬜ |

## Import / Export / DSpace

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | /exports | ⬜ |
| POST | /exports | ⬜ |
| GET | /exports/{id} | ⬜ |
| DELETE | /exports/{id} | ⬜ |
| GET | /import | ⬜ |
| POST | /import | ⬜ |
| GET | /dspace/read | ⬜ |
| POST | /dspace/create | ⬜ |
| POST | /dspace/submit | ⬜ |
