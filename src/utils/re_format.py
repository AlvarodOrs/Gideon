import re
import base64

from constants import CATEGORIES

def set_category(topics):
    for topic in topics:
        if topic in CATEGORIES: return topic

def format_README(readme_content, where_is):
    match = re.search(where_is, readme_content, re.DOTALL)
    if match: return match.group(1).strip()
    else:
        print("[ERROR!!] Markers not found or in wrong order")
        return ''

def set_status(readme_content):
    match = re.search(r'## Status\n*\s*(.*)', readme_content, re.DOTALL)
    if match: 
        _status = match.group(1).split(".")[0]
        status = _status.lower().replace(" ", "-")
        return status
    else:
        print("[ERROR!!] No defined status")
        return ''
    
def format_repo_data(repo):
    category = set_category(repo['topics'])
    if category == 'website':
        readme = f'## Overview\n\n{repo['description']}'
        status = 'live'
    else:
        readme = format_README(repo['readme'], r'<!--\s*\[START\]\s(.*?)\[END\]\s*-->')
        status = set_status(readme)
    return {
        "title": repo['name'],
        "category": category,
        "description": repo['description'],
        "status": status,
        "tags": repo['topics'],
        "created": repo['created_at'],
        "updated": repo['updated_at'],
        "repo": repo['html_url'] if repo['homepage'] is None else repo['homepage'],
        "content": readme
    }

def mdx_format_data(repo: dict):
    _default = "Missing variable"
    tags = "\n".join(f"  - {tag}" for tag in repo["tags"])

    date = repo["created"].split("T")[0]
    updated = repo["updated"].split("T")[0]
    
    repo_name = repo['title']
    repo_link = f"https://social.adors.dev/github/{repo_name}"
    content = repo["content"]
    frontmatter = f"""---
title: {repo_name}
category: {repo['category']}
description: {repo['description']}
status: {repo['status']}
tags:
{tags}
date: {date}
updated: {updated}
repo: {repo_link}
---
{content}
"""
    return frontmatter #base64.b64encode(frontmatter.encode("utf-8")).decode("utf-8")