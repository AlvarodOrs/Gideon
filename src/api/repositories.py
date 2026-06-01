import requests

from .main import GithubAPI
from ..myTypes.api.responses import ExtendedRepositoryInfo

class Repository(GithubAPI):
    def __init__(self, GITHUB_ID: str, repository_name: str, accept_type: str = "application/vnd.github+json", token: str = None, is_debug: bool = False):
        super().__init__(accept_type, token)
        self.GITHUB_ID = GITHUB_ID
        self.repository_name = repository_name
        self.url = f'{self.base_url}/repos/{self.GITHUB_ID}'
        self.is_debug = is_debug
        
    def get_repo_info(self) -> ExtendedRepositoryInfo:
        if self.is_debug: input(f"Fetching user info in {self.url}/{self.repository_name} using {'authenticated' if self.token else 'public'} API endpoint")
        return requests.get(f'{self.url}/{self.repository_name}', headers=self.headers)
    
    def get_file_content(self, file_path: str):
        if self.is_debug: input(f"Fetching content of {file_path} in {self.url}/{self.repository_name} using {'authenticated' if self.token else 'public'} API endpoint")
        return requests.get(f'{self.url}/{self.repository_name}/contents/{file_path}', headers=self.headers)
    
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()
    GITHUB_ID = os.getenv('GITHUB_ID')
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    worker1 = Repository(GITHUB_ID, "REPO", token=GITHUB_TOKEN, is_debug=True)
    worker1.get_repo_info()