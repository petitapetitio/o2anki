from pathlib import Path

from o2anki.parsing.folder import Folder
from tests.test_parsing_files import note


def test_parsing_folder():
    assert set(Folder.of(Path("assets/folder"), (Path("assets/folder/excluded_folder"),)).notes) == {
        note("question 1 ?", "answer 1"),
        note("question 2 ?", "answer 2"),
        note("question 3 ?", "answer 3"),
    }


