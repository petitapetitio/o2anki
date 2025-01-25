from dataclasses import dataclass


@dataclass(frozen=True)
class SkippedNote:
    message: str
