import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class ParsedNote:
    question: str
    answer: str
    identifier: Optional[int] = None


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
            r = rsplit.split("\n\n\n")[0]
            yield ParsedNote(question=q.strip(), answer=r.strip())


def file_notes(file):
    return list(File.from_path(Path(file)).notes())


def test_empty_file():
    assert file_notes("assets/file_without_card.md") == []


def test_file_without_card():
    assert file_notes("assets/file_without_card.md") == []


def test_card_with_noise_around():
    assert file_notes("assets/card_with_noise_around.md") == [
        ParsedNote("question ?", "3.7")
    ]


answer_of_several_paragraphs = """\
paragraphe 1
paragraphe 1
paragraphe 1

paragraphe 2
paragraphe 2
paragraphe 2\
"""


def test_card_with_several_paragraphs():
    assert file_notes("assets/card_with_several_paragraphs.md") == [
        ParsedNote("question ?", answer_of_several_paragraphs),
        ParsedNote("question 2 ?", "réponse 2"),
    ]


def test_card_with_several_paragraphs_at_the_end_of_a_file():
    assert file_notes("assets/card_with_several_paragraphs_at_the_end_of_a_file.md") == [
        ParsedNote("question ?", answer_of_several_paragraphs)
    ]
