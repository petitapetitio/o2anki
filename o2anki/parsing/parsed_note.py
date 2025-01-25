from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ParsedNote:
    question: str
    answer: str
    note_id: Optional[int] = None
    target_deck: Optional[str] = None
