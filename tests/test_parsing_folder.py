from pathlib import Path

from o2anki.parsing.folder import Folder
from o2anki.parsing.parsed_note import ParsedNote


def test_parsing_folder():
    assert set(Folder(Path("assets/folder"), (Path("assets/folder/excluded_folder"),)).notes()) == {
        ParsedNote("question 1 ?", "answer 1"),
        ParsedNote("question 2 ?", "answer 2"),
        ParsedNote("question 3 ?", "answer 3"),
    }


