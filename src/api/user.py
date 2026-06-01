
import requests

from .main import GithubAPI
from ..myTypes.api.responses import UserInfo, RepositoryInfo

class User(GithubAPI):
    def __init__(self, GITHUB_ID: str, accept_type: str = "application/vnd.github+json", token: str = None, is_debug: bool = False):
        super().__init__(accept_type, token)
        self.GITHUB_ID = GITHUB_ID
        self.url = f'{self.base_url}/user/{self.GITHUB_ID}'
        self.is_debug = is_debug

    def get_user_info(self) -> UserInfo:
        if self.is_debug: input(f"Fetching user info in {self.url} using {'authenticated' if self.token else 'public'} API endpoint")
        return requests.get(self.url, headers=self.headers_public if not self.token else self.headers_auth)
    
    def get_repositories_info(self) -> list[RepositoryInfo]:
        if self.is_debug: input(f"Fetching repositories info in {self.url}/repos using {'authenticated' if self.token else 'public'} API endpoint")
        return requests.get(f'{self.url}/repos', headers=self.headers_public if not self.token else self.headers_auth)