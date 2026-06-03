<!-- [START]
## Overview

Gideon is a synchronization pipeline that transforms GitHub repository metadata into structured, up-to-date public representations across two outputs: a profile `README.md` and a Next.js portfolio site.

It removes manual maintenance of project listings and descriptions by treating GitHub as the source of truth. On execution, it retrieves current repository state and deterministically regenerates downstream content.

## Scope

* Ingestion of GitHub repository metadata via GitHub REST API
* Generation of GitHub profile `README.md` from structured templates
* Generation and update of MDX-based project pages in a Next.js portfolio
* Consistent synchronization between GitHub repository state and external presentation layers

## Constraints

* Operates only on public GitHub repository data
* No formal configuration schema currently enforced for templates or output mapping
* No defined merge strategy between manually edited and auto-generated content
* Requires an external trigger mechanism (CI, cron, or manual execution) to run synchronization cycles
* Output correctness is fully dependent on template validity and repository metadata consistency

## Status

In progress. Core synchronization pipeline is in active development.
Deterministic data ingestion and regeneration flow is functional, with automation and orchestration layers still evolving.
[END] -->

# Gideon

## System Overview

Gideon is an automation pipeline that continuously synchronizes a developer’s public GitHub ecosystem with two downstream artifacts:

* A dynamically generated GitHub profile `README.md`
* A Next.js-based personal portfolio site built from MDX project definitions

It operates as a metadata-driven system: GitHub becomes the single source of truth, and all public-facing content is derived from repository state rather than manual editing.

---

## Core Behavior

Gideon periodically ingests GitHub repository metadata via the GitHub REST API, transforms it into structured intermediate representations, and renders it into two output formats:

* Markdown (for GitHub profile rendering)
* MDX (for portfolio site consumption)

The system is designed around deterministic regeneration: given the same repository state, output is reproducible.

---

## Features

* GitHub REST API ingestion of public repository metadata:
  name, description, topics, primary language, stars, forks, last update timestamp

* Automatic regeneration of GitHub profile `README.md`

* Automatic synchronization of portfolio content via MDX generation for Next.js pages

* Unified transformation pipeline ensuring consistency between README and portfolio representations

* Scheduled execution model (cron / CI-based workflows)

* Experimental AI-assisted enrichment layer (planned):
  contextual project descriptions derived from repository analysis

---

## Architecture

### Data Layer

* GitHub REST API as the sole source of truth
* Repository metadata pulled per user scope

### Processing Layer

* Transformation engine mapping raw repository data → structured schema
* Template-based rendering system for Markdown and MDX outputs
* Normalization of naming, descriptions, and categorization

### Output Layer

* GitHub profile repository (`README.md`)
* Next.js portfolio repository (MDX-based project pages)

### Automation Layer

* Scheduled execution via cron or CI/CD pipelines
* Optional event-driven triggers (webhooks or repository activity hooks, planned expansion)

---

## Installation

```bash
git clone https://github.com/AlvarodOrs/Gideon.git
cd Gideon
python -m src.main
```

---

## Usage

1. Configure GitHub API credentials
2. Define runtime constants in `constants.py`
3. Add secrets in `.env` (based on `.env.EXAMPLE`)
4. Execute manually or schedule execution via CI/CD or cron

On execution, the system:

* Fetches latest repository metadata
* Regenerates GitHub profile `README.md`
* Updates portfolio MDX project pages

---

## Configuration

* GitHub personal access token
* Target username or repository scope
* Output repository mappings (README + portfolio)
* Template definitions for Markdown and MDX rendering
* Sync interval configuration (if scheduled execution is used)

---

## Limitations

* Operates only on public GitHub repository metadata
* Requires predefined templates for stable output generation
* No semantic understanding of project intent yet (descriptions are metadata-driven, not contextualized)
* Portfolio synchronization assumes Next.js + MDX structure compatibility

---

## Roadmap

* Event-driven updates via GitHub webhooks (remove polling dependency)
* Full AI semantic layer for project description generation
* Configurable multi-user support (turning it into a general platform)
* CLI packaging for external usage
* Self-hosted deployment mode (Dockerized runtime)