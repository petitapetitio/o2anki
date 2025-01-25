import re
import markdown


class NotePresenter:
    def __init__(self):
        self.markdown_parser = markdown.Markdown(
            extensions=[
                "fenced_code",
                "footnotes",
                "md_in_html",
                "tables",
                "nl2br",
                "sane_lists",
            ]
        )

    def convert(self, text: str) -> str:
        html = self.markdown_parser.convert(text)
        images = re.findall(r"!\[\[([^\]]+)\]\]", html)
        for image in images:
            html = html.replace(f"![[{image}]]", f"<img src='{image}'/>")

        return html
