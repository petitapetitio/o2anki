from dataclasses import dataclass
from pathlib import Path

from o2anki.parsing.parsed_note import ParsedNote


@dataclass(frozen=True)
class File:
    _content: str

    @classmethod
    def from_path(cls, filepath: Path):
        with open(filepath) as f:
            return File(f.read())

    def notes(self) -> list[ParsedNote]:
        for split in self._content.split("\nQ : ")[1:]:
            q, rsplit = split.split("\nR : ")
            id_split = rsplit.split("<!-- ID : ")
            if len(id_split) == 1:
                note_id = None
                r = rsplit.split("\n\n\n")[0]
            elif len(id_split) == 2:
                r, i = id_split
                note_id = int(i.split("-->")[0].strip())
            else:
                raise ValueError(f"Erreur lors du parsing de {split}")

            yield ParsedNote(question=q.strip(), answer=r.strip(), note_id=note_id)
