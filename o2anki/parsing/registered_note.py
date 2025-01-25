from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class RegisteredNote:
    question: str
    answer: str
    note_id: int
    filepath: Path
