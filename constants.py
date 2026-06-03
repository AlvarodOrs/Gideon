WEB_REPO = "adors.dev"
WEB_REPO_PATH = "content/projects"
EXCLUDED_REPOS = ["UNIR", "TESTING"]
CATEGORIES = ['finance', 'engineering', 'utils', 'website']
EXCLUDED_CATEGORIES = None #['website']
MDX_TEMPLATE = """
## Overview
[2 lines of content]

## Scope
- [Function1] — [what is it, 1 line]

## Status
[is it live, completed, in progress or planned]. [Phase where we are now]
"""
PROMPT_TEMPLATE = f"You are a profesional README redacter that wil ONLY ANSWER WITH THE ASKED OUTPUT, you are tasked with creating a README following this template {MDX_TEMPLATE} for the following github repo"