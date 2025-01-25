from pathlib import Path
from typing import Optional

from o2anki.parsing.file import File
from o2anki.parsing.parsed_note import ParsedNote
from o2anki.parsing.skipped_note import SkippedNote


def file_notes(file):
    return list(File.from_path(Path(file)).notes())


def note(question: str, answer: str, *, note_id: Optional[int] = None, target_deck: Optional[str] = None, file_tags: tuple = ()):
    return ParsedNote(question, answer, note_id, target_deck, file_tags)


def test_parsing_empty_file():
    assert file_notes("assets/file_without_card.md") == []


def test_parsing_question_sans_reponse():
    assert file_notes("assets/question_sans_reponse.md") == [SkippedNote("La question `question ?` est sans réponse.")]


def test_parsing_file_without_card():
    assert file_notes("assets/file_without_card.md") == []


def test_parsing_card_with_noise_around():
    assert file_notes("assets/card_with_noise_around.md") == [
        note("question ?", "answer")
    ]


answer_of_several_paragraphs = """\
paragraphe 1
paragraphe 1
paragraphe 1

paragraphe 2
paragraphe 2
paragraphe 2\
"""


def test_parsing_card_with_several_paragraphs():
    assert file_notes("assets/card_with_several_paragraphs.md") == [
        note("question ?", answer_of_several_paragraphs),
        note("question 2 ?", "réponse 2"),
    ]


def test_parsing_card_with_several_paragraphs_at_the_end_of_a_file():
    assert file_notes(
        "assets/card_with_several_paragraphs_at_the_end_of_a_file.md"
    ) == [note("question ?", answer_of_several_paragraphs)]


def test_parsing_card_with_question_on_several_lines():
    assert file_notes("assets/card_with_question_on_several_lines.md") == [
        note(question_of_several_lines, answer_of_several_paragraphs)
    ]


question_of_several_lines = """\
question ? 

```python
print(50)
```\
"""


def test_parsing_2_new_cards_separated_by_a_single_line():
    assert file_notes("assets/2_new_cards_separated_by_a_single_line.md") == [
        note("question 1 ?", "answer 1"),
        note("question 2 ?", "answer 2"),
    ]


def test_parsing_2_registered_cards_separated_by_a_single_line():
    assert file_notes("assets/2_registered_cards_separated_a_single_line.md") == [
        note("question 1 ?", "answer 1", note_id=1),
        note("question 2 ?", "answer 2", note_id=2),
    ]


def test_parsing_file_with_target_deck():
    assert file_notes("assets/file_with_target_deck.md") == [
        note("question 1 ?", "answer 1", target_deck="Test Deck")
    ]


def test_parsing_file_with_tags():
    assert file_notes("assets/file_with_tags.md") == [note("question 1 ?", "answer 1", file_tags=("tag-1", "tag-2"))]
