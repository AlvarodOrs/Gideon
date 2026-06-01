from .api.user import User
from .api.repositories import Repository

from .myTypes.toUse.info import RawRepoInfo, FormattedRepoInfo

class APIProcesses:
    def __init__(self, GITHUB_ID: str, token: str = None, is_debug: bool = False):
        self.GITHUB_ID = GITHUB_ID
        self.token = token
        self.is_debug = is_debug

    def list_repositories(self):
        user = User(self.GITHUB_ID, self.token, self.is_debug)
        return user.get_repositories_info().json()

    def get_file_content(self, repository_name: str, file_path: str):
        self.accept_type: str = "application/vnd.github+json"
        repo = Repository(self.GITHUB_ID, repository_name, self.accept_type, self.token, self.is_debug)
        return repo.get_file_content(file_path).json()
    
    def get_repo_info(self, repository_name: str):
        repo = Repository(self.GITHUB_ID, repository_name, self.token, self.is_debug)
        return repo.get_repo_info().json()

    def get_repos_info(self) -> list[RawRepoInfo]:
        required_info = [
            {
                'name': repo['name'],
                'topics': repo['topics'],
                'description': repo['description'],
                'created_at': repo['created_at'],
                'homepage': repo['homepage'],
                'readme': self.get_file_content(repo['name'], 'README.md')
            }
            for repo in self.list_repositories()
        ]
        # repo = Repository(self.GITHUB_ID, repository_name, self.token, self.is_debug)
        input("done")
        for repo in required_info:
            print(repo)
            input("done")
        return required_info