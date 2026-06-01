from dataclasses import dataclass
from typing import Optional, Literal, TypedDict

@dataclass
class MainUserInfo(TypedDict):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: Optional[str]
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    user_view_type: str
    site_admin: bool

@dataclass
class PersonalUserInfo(TypedDict, total=False):
    name: str
    company: str
    blog: str
    location: str
    email: str
    hireable: bool
    bio: str
    twitter_username: str

@dataclass
class GithubStatsUserInfo(TypedDict):
    public_repos: int
    public_gists: int
    followers: int
    following: int

    created_at: str
    updated_at: str

@dataclass
class PlanUserInfo(TypedDict, total=False):
    collaborators: int
    name: str
    space: int
    private_repos: int

@dataclass
class BillingUserInfo(TypedDict, total=False):
    private_gists: int
    total_private_repos: int
    owned_private_repos: int
    disk_usage: int
    collaborators: int
    two_factor_authentication: bool

    plan: PlanUserInfo

    business_plus: bool
    ldap_dn: str

@dataclass
class UserInfo(
        MainUserInfo,
        PersonalUserInfo,
        GithubStatsUserInfo,
        BillingUserInfo # Optional, as it requires additional permissions
    ):
    pass

@dataclass
class LicenseInfo(TypedDict, total=False):
    key: str
    name: str
    spdx_id: str
    url: str
    node_id: str

@dataclass
class MainRepositoryInfo(TypedDict):
    html_url: str
    description: Optional[str]
    fork: bool
    url: str
    forks_url: str
    keys_url: str
    collaborators_url: str
    teams_url: str
    hooks_url: str
    issue_events_url: str
    events_url: str
    assignees_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    git_tags_url: str
    git_refs_url: str
    trees_url: str
    statuses_url: str
    languages_url: str
    stargazers_url: str
    contributors_url: str
    subscribers_url: str
    subscription_url: str
    commits_url: str
    git_commits_url: str
    comments_url: str
    issue_comment_url: str
    contents_url: str
    compare_url: str
    merges_url: str
    archive_url: str
    downloads_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    deployments_url: str
    created_at: str
    updated_at: str
    pushed_at: str
    git_url: str
    ssh_url: str
    clone_url: str
    svn_url: str
    homepage: str
    size: int
    stargazers_count: int
    watchers_count: int
    language: str
    has_issues: bool
    has_projects: bool
    has_downloads: bool
    has_wiki: bool
    has_pages: bool
    has_discussions: bool
    forks_count: int
    mirror_url: Optional[str]
    archived: bool
    disabled: bool
    open_issues_count: int
    license: Optional[LicenseInfo]
    allow_forking: bool
    is_template: bool
    web_commit_signoff_required: bool
    has_pull_requests: bool
    pull_request_creation_policy: Literal["all", "collaborators_only"]
    topics: Optional[list[str]]
    visibility: Literal["public", "private"]
    forks: int
    open_issues: int
    watchers: int
    default_branch: str

@dataclass
class RepositoryInfo(MainRepositoryInfo):
    id: int
    node_id: str
    name: str
    full_name: str
    private: bool
    owner: MainUserInfo

@dataclass
class ExtendedRepositoryInfo(RepositoryInfo):
  temp_clone_token: Optional[str]
  network_count: int
  subscribers_count: int