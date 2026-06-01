from .api_processes import APIProcesses

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()
    GITHUB_ID = os.getenv('GITHUB_ID')
    # GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    worker1 = APIProcesses(GITHUB_ID, is_debug=True)
    worker1.get_repos_info()