from constants import COMMIT_MESSAGE

def get_headers(extension: str = None, token: str = None):
    _headers = {
        'Accept': 'application/vnd.github+json',
    }
    if extension: _headers['Accept'] = f'application/vnd.github{'.'+extension}+json'
    if token: _headers['Authorization'] = f'Bearer {token}'
    _headers['X-GitHub-Api-Version'] = '2026-03-10'
    return _headers

def get_body(new_content: str, sha_encoding: str = None):
    _ = {
        "message": COMMIT_MESSAGE,
        "committer": {
            "name": "Gideon",
            "email": "gideon@adors.dev"},
        "content": new_content,
    }
    if sha_encoding: _['sha'] = sha_encoding
    return _

def get_url(is_repo: bool = False):
    if is_repo: return 'https://api.github.com/repos'
    return 'https://api.github.com'