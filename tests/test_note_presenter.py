from o2anki.note_presenter import NotePresenter


def parser():
    return NotePresenter()



def test_parsing_markdown_to_html():
    assert parser().convert("hello ![[image.png]]") == "<p>hello <img src='image.png'/></p>"
