class GithubAPI:
    def __init__(self, accept_type: str = "application/vnd.github+json", token: str = None):
        self.token = token
        self.headers_public = {
            'Accept': accept_type,
            'X-GitHub-Api-Version': "2026-03-10"
            }
        if token:
            self.headers_auth = {
                'Accept': accept_type,
                'X-GitHub-Api-Version': "2026-03-10",
                'Authorization': f'token {self.token}'
                }
        else:
            print("No token provided, using public API endpoints")
            self.headers_auth = self.headers_public 

        self.base_url = 'https://api.github.com'