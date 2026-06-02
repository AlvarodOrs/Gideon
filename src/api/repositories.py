import requests
from typing import Optional

from .main import get_headers, get_url
from ..myTypes.api.responses import ExtendedRepositoryInfo
class Repository:
    def __init__(self, API_data: tuple[int, Optional[str]],
                 repository_name: str, username: str,
                 is_debug: bool = False):
        
        self.github_id, self.token = API_data
        self.repository_name = repository_name
        self.url = get_url(is_repo=True)
        self.is_debug = is_debug
        self.owner_login = username
        
    def get_repo_info(self) -> ExtendedRepositoryInfo:
        if self.is_debug: print(f"Fetching repo info in {self.url}/{self.github_id}/{self.repository_name} using {'authenticated' if self.token else 'public'} API endpoint")
        return requests.get(f'{self.url}/{self.github_id}/{self.repository_name}', headers=get_headers(token=self.token))
    
    def get_file_content(self, file_path: str, extension: str = None):
        if self.is_debug: print(f"Fetching content of {file_path} in {self.url}/{self.owner_login}/{self.repository_name}/contents/{file_path} using {'authenticated' if self.token else 'public'} API endpoint")
        return requests.get(f'{self.url}/{self.owner_login}/{self.repository_name}/contents/{file_path}', headers=get_headers(extension=extension, token=self.token))

    def update_file(self, new_content: str, file_path: str, sha_encoding: str = None):
        if not self.token: raise ValueError("An authorized REQUEST is needed for this action")
        if self.is_debug: print(f"Fetching content of {file_path} in {self.url}/{self.owner_login}/{self.repository_name}/contents/{file_path} using {'authenticated' if self.token else 'public'} API endpoint")
        return requests.put(f'{self.url}/{self.owner_login}/{self.repository_name}/contents/{file_path}', headers=get_headers(token=self.token), json=get_body(new_content=new_content, sha_encoding=sha_encoding))
    
    def commit_files(self, files: list[dict]):
        ref = requests.get(
            f"{self.url}/{self.owner_login}/{self.repository_name}/git/ref/heads/main",
            headers=get_headers(token=self.token)
        ).json()
        base_commit_sha = ref["object"]["sha"]

        base_commit = requests.get(
            f"{self.url}/{self.owner_login}/{self.repository_name}/git/commits/{base_commit_sha}",
            headers=get_headers(token=self.token)
        ).json()

        base_tree_sha = base_commit["tree"]["sha"]

        tree = [
            {
                "path": f["path"],
                "mode": "100644",
                "type": "blob",
                "content": f["content"]
            }
            for f in files
        ]

        new_tree = requests.post(
            f"{self.url}/{self.owner_login}/{self.repository_name}/git/trees",
            headers=get_headers(token=self.token),
            json={
                "base_tree": base_tree_sha,
                "tree": tree
            }
        ).json()

        new_commit = requests.post(
            f"{self.url}/{self.owner_login}/{self.repository_name}/git/commits",
            headers=get_headers(token=self.token),
            json={
                    "message": "Gideon auto-update",
                    "tree": new_tree['sha'],
                    "parents": [base_commit_sha],
                    "author": {
                        "name": "Gideon",
                        "email": "gideon@adors.dev"
                    },
                    "committer": {
                        "name": "Gideon",
                        "email": "gideon@adors.dev"
                    }
                }
        ).json()

        return requests.patch(
            f"{self.url}/{self.owner_login}/{self.repository_name}/git/refs/heads/main",
            headers=get_headers(token=self.token),
            json={"sha": new_commit["sha"]}
        )