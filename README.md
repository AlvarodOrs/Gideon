<!-- [START]
## Overview

Gideon automates the maintenance of a developer's public presence by syncing data from their GitHub repositories into two targets: the profile `README.md` and a Next.js personal web.

Instead of manually updating project lists, stats, or descriptions every time a repo changes, Gideon fetches the latest public repo data and regenerates the relevant sections automatically.

## Scope

- **GitHub data ingestion** — fetches public repository metadata via the GitHub API (names, descriptions, languages, stars, last updated)
- **README generation** — updates the GitHub profile README with current project data and stats
- **Next.js integration** — pushes structured repo data into a Next.js site so the portfolio stays current without manual edits
- **Automation layer** — designed to run on a schedule or trigger, keeping both targets in sync passively

## Status

In progress. Core sync pipeline under development.
[END] -->
