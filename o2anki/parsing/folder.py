from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

from o2anki.parsing.file import File
from o2anki.parsing.parsed_note import ParsedNote


@dataclass(frozen=True)
class Folder:
    _path: Path
    _excluded_paths: tuple[Path] = ()

    def notes(self) -> Iterator[ParsedNote]:
        for p in self._path.glob("**/*.md"):
            if p.parent in self._excluded_paths:
                continue

            yield from File.from_path(p).notes()
