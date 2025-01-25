import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, ClassVar

from o2anki.parsing.parsed_note import ParsedNote
from o2anki.parsing.skipped_note import SkippedNote


@dataclass(frozen=True)
class File:
    _content: str
    _target_deck_regex: ClassVar[re.Pattern] = re.compile(r"TARGET DECK: ([\w ]+)\n")

    @classmethod
    def from_path(cls, filepath: Path):
        with open(filepath) as f:
            return File(f.read())

    def notes(self) -> Iterator[ParsedNote | SkippedNote]:
        target_deck = self._target_deck_regex.findall(self._content)
        target_deck = target_deck[0] if len(target_deck) > 0 else None

        for split in self._content.split("\nQ : ")[1:]:
            try:
                q, rsplit = split.split("\nA : ")
            except ValueError as e:
                yield SkippedNote(f"La question `{split.strip()}` est sans réponse.")
                continue

            id_split = rsplit.split("<!-- ID : ")
            if len(id_split) == 1:
                note_id = None
                r = rsplit.split("\n\n\n")[0]
            elif len(id_split) == 2:
                r, i = id_split
                note_id = int(i.split("-->")[0].strip())
            else:
                raise ValueError(f"Erreur lors du parsing de {split}")

            yield ParsedNote(question=q.strip(), answer=r.strip(), note_id=note_id, target_deck=target_deck)
