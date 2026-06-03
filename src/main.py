import os
from dotenv import load_dotenv

from .api.user import User
from .api.repositories import Repository
from .myTypes.toUse.info import RawRepoInfo, FormattedRepoInfo

from .utils import format_repo_data, mdx_format_data

from constants import EXCLUDED_REPOS, WEB_REPO, WEB_REPO_PATH, EXCLUDED_CATEGORIES


load_dotenv()
GITHUB_ID = os.getenv('GITHUB_ID')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
class App:
    def __init__(self, is_debug: bool = False):
        self.is_debug: bool = is_debug
        self.user: classmethod = User(API_data=(GITHUB_ID, GITHUB_TOKEN), is_debug=self.is_debug)
        self.username: str = self.user.get_username()
        self.repositories: list = self.user.get_repositories_info().json()
        self.excluded_repos: list = EXCLUDED_REPOS.append(self.username)

    def get_repo_info(self, repo: RawRepoInfo, readme: str = None) -> dict[RawRepoInfo]:
        
        return {
            'name': repo['name'],
            'topics': repo['topics'],
            'description': repo['description'],
            'created_at': repo['created_at'],
            'updated_at': repo['updated_at'],
            'homepage': repo['homepage'],
            'html_url': repo['html_url'],
            'readme': readme,
            'owner': repo['owner']['login']
        }
    
    def get_file(self, repo_name: str, file_path: str, extension: str = None):
        repo = Repository(API_data=(GITHUB_ID, GITHUB_TOKEN), repository_name=repo_name, username=self.username, is_debug=self.is_debug)
        ans = repo.get_file_content(file_path=file_path, extension=extension)
        if extension is None: return ans.json()
        elif extension == 'raw': return ans.text 
        else: input(f"Unknown {extension=}")

    def fetch_data(self):
        repos = [repo for repo in self.repositories
                if repo['name'] not in EXCLUDED_REPOS]
        
        repo_data = []
        for repo in repos:
            readme_content = self.get_file(repo['name'], 'README.md', 'raw')
            repo_data.append(
                self.get_repo_info(repo=repo, readme=readme_content)
            )

        return [format_repo_data(repo) for repo in repo_data]
    
    def process_data(self, data):
        profile_readme_data = []
        files = []

        repo = Repository(API_data=(GITHUB_ID, GITHUB_TOKEN), repository_name=WEB_REPO, username=self.username, is_debug=self.is_debug)
        for _repo in data:
            files.append({
                "path": f"{WEB_REPO_PATH}/{_repo['title'].lower()}.mdx",
                "content": mdx_format_data(_repo)})

            profile_readme_data.append(f"{_repo['title']} - {_repo['description']}")
        
        repo.commit_files(files)
        #README later

if __name__ == "__main__":
    run = App(False)
    data = run.fetch_data()
    for repo in data: print(repo,'\n')
    input()
    run.process_data(data)