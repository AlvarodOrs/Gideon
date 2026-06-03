import requests

from constants import PROMPT_TEMPLATE
class AI_API:
    def __init__(self):
        pass

    def generate_README(self, repo_link: str):
        message = f'{PROMPT_TEMPLATE}: {repo_link}'
        return requests(...)