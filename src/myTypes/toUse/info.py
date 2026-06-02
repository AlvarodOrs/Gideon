from dataclasses import dataclass
from typing import Optional, Literal, TypedDict

@dataclass
class RawRepoInfo:
    name: str
    topics: Optional[list[str]]
    description: Optional[str]
    created_at: str
    homepage: Optional[str]


@dataclass
class ReadmeInfo:
    content: str
    encoding: str
    name: str

@dataclass
class FormattedRepoInfo(ReadmeInfo):
    title: str
    category: Literal['finance', 'engineering', 'utils']
    description: Optional[str]
    status: Literal['planned', 'in-progress', 'completed', 'live']
    tags: Optional[list[str]]
    created: str
    updated: str
    repo: str
