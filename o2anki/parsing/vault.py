from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

from o2anki.parsing.file import File
from o2anki.parsing.parsed_note import ParsedNote


@dataclass(frozen=True)
class Vault:
    _notes: list[ParsedNote]
    decks: set[str]
    media: dict[str, Path]

    def unregistered_notes(self) -> Iterator[ParsedNote]:
        return filter(lambda n: n.note_id is None, self._notes)

    def registered_notes(self) -> Iterator[ParsedNote]:
        return filter(lambda n: n.note_id, self._notes)

    @classmethod
    def of(cls, folder: Path, excluded_paths: tuple[Path] = ()) -> "Vault":
        for excluded_path in excluded_paths:
            if not excluded_path.is_relative_to(folder):
                raise ValueError(f"Le chemin {excluded_path} n'es pas relatif au vault ({folder}) et sera ignoré")

        notes = []
        decks = set()
        media = {}
        for p in folder.glob("**/*.md"):
            if _is_relative_to(excluded_paths, p):
                continue

            for note in File(p).notes():
                notes.append(note)
                if note.target_deck:
                    decks.add(note.target_deck)
                for image in note.images:
                    files = list(folder.glob(f"**/{image}"))

                    if len(files) == 0:
                        raise Exception(f"Le fichier {image} n'a pas été trouvé dans le dossier {folder}")
                    if len(files) > 1:
                        raise Exception(f"Le nom de fichier {image} est ambigüe dans le dossier {folder}: {files}")

                    absolute_path = files[0].resolve()

                    if image in media and media[image] != absolute_path:
                        raise Exception(f"Le nom de fichier {image} est ambigüe. L'image appraît ici `{absolute_path}` et là `{media[image]}`")

                    media[image] = absolute_path

        return Vault(notes, decks, media)


def _is_relative_to(excluded_paths, p) -> bool:
    for excluded_path in excluded_paths:
        if p.is_relative_to(excluded_path):
            return True
    return False