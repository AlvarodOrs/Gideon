<!-- [START]
## Overview

Automation system that pulls GitHub repository metadata and generates synchronized updates for a profile README and a Next.js portfolio website.

Instead of manually updating project lists, stats, or descriptions every time a repo changes, Gideon fetches the latest public repo data and regenerates the relevant sections automatically.

## Scope

* GitHub repository metadata ingestion via API
* Automated generation of profile README content
* Automated updates to portfolio website MDX project pages
* Continuous synchronization between GitHub and personal web presence

## Constraints

* Limited to public GitHub data
* No defined configuration schema provided
* No conflict handling strategy for manual vs automated edits specified
* Dependent on external scheduling/trigger system for execution

## Status

In progress. Core sync pipeline under development.
[END] -->