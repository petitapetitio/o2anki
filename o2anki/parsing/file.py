import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, ClassVar

from o2anki.parsing.parsed_note import ParsedNote
from o2anki.parsing.skipped_note import SkippedNote


@dataclass(frozen=True)
class File:
    _filepath: Path

    _target_deck_regex: ClassVar[re.Pattern] = re.compile(r"TARGET DECK: ([\w -_]+)\n")
    _file_tags_regex: ClassVar[re.Pattern] = re.compile(r"FILE TAGS: ([\w -_]+)\n")

    def notes(self) -> Iterator[ParsedNote | SkippedNote]:
        with open(self._filepath) as f:
            content = f.read()

        target_deck = self._target_deck_regex.findall(content)
        target_deck = target_deck[0] if len(target_deck) > 0 else None

        file_tags: list[str] = self._file_tags_regex.findall(content)
        file_tags = file_tags[0].split(" ") if len(file_tags) > 0 else []

        for split in content.split("\nQ : ")[1:]:
            try:
                q, rsplit = split.split("\nA : ")
            except ValueError as e:
                print(f"La question `{split.strip()}` est sans réponse.")
                continue

            id_split = rsplit.split("<!--ID: ")
            if len(id_split) == 1:
                note_id = None
                r = rsplit.split("\n\n\n")[0]
            elif len(id_split) == 2:
                r, i = id_split
                note_id = int(i.split("-->")[0].strip())
            else:
                raise ValueError(f"Erreur lors du parsing de {split}")

            yield ParsedNote(
                question=q,
                answer=r.strip(),
                note_id=note_id,
                target_deck=target_deck,
                file_tags=tuple(file_tags),
                filepath=self._filepath
            )
