from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ParsedNote:
    question: str
    answer: str
    note_id: Optional[int]
    target_deck: Optional[str]
    file_tags: tuple[str]
