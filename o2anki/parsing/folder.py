from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

from o2anki.parsing.file import File
from o2anki.parsing.parsed_note import ParsedNote
from o2anki.parsing.skipped_note import SkippedNote


@dataclass(frozen=True)
class Folder:
    notes: list[ParsedNote | SkippedNote]
    decks: set[str]

    def unregistered_notes(self) -> Iterator[ParsedNote]:
        return filter(lambda n: isinstance(n, ParsedNote) and n.note_id is None, self.notes)

    @classmethod
    def of(cls, path: Path, excluded_paths: tuple[Path] = ()) -> "Folder":
        notes = []
        decks = set()
        for p in path.glob("**/*.md"):
            if p.parent in excluded_paths:
                continue

            for n in File(p).notes():
                notes.append(n)
                if n.target_deck:
                    decks.add(n.target_deck)

        return Folder(notes, decks)
