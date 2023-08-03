# Declare a full text search interface (abstract class)
from abc import ABC, abstractmethod
from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass
@dataclass_json
class FullTextSearchResult:
    result_text: str
    id: str
    similarity: float


class FullTextSearchInterface(ABC):
    """Interface for full text search."""

    @abstractmethod
    def search(self, request: str) -> list[FullTextSearchResult]:
        """Search for the request."""
        pass

    @abstractmethod
    def add_document(self, document: str, id: str):
        """Add a document to the search."""
        pass
