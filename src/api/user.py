
import requests
from typing import Optional

from .main import  get_headers, get_url
from ..myTypes.api.responses import UserInfo, RepositoryInfo

class User:
    def __init__(self, API_data: tuple[int, Optional[str]],
                 is_debug: bool = False):
        
        github_id, self.token = API_data
        self.url = f'{get_url()}/user/{github_id}'
        self.is_debug = is_debug
        self.headers = get_headers(token=self.token)

    def get_user_info(self) -> UserInfo:
        if self.is_debug: print(f"Fetching user info in {self.url} using {'authenticated' if self.token else 'public'} API endpoint")
        return requests.get(self.url, headers=self.headers)
    
    def get_repositories_info(self) -> list[RepositoryInfo]:
        if self.is_debug: print(f"Fetching repositories info in {self.url}/repos using {'authenticated' if self.token else 'public'} API endpoint")
        return requests.get(f'{self.url}/repos', headers=self.headers)
    
    def get_username(self) -> str:
        return self.get_user_info().json()['login']
