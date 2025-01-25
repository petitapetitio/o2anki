from pathlib import Path

from o2anki.anki_connect_client import AnkiConnectClient
from o2anki.parsing.folder import Folder
from o2anki.parsing.registered_note import RegisteredNote


class O2Anki:
    def __init__(self):
        self.client = AnkiConnectClient()

    def export(self, folder: Path):

        folder = Folder.of(folder)
        requests = []

        # create the decks
        for d in folder.decks:
            r = self.client.create_deck(d)
            self.client.invoke(r)

        # create the notes
        unregistered_notes = list(folder.unregistered_notes())
        for n in unregistered_notes:
            requests.append(self.client.add_basic_note_request(n))
        results = self.client.invoke_requests(requests)

        # write the ids
        registered_notes = []
        for unregistered_note, note_id in zip(unregistered_notes, results):
            registered_notes.append(RegisteredNote(unregistered_note.question, unregistered_note.answer, note_id, unregistered_note.filepath))

        write_ids(registered_notes)


def write_ids(notes: list[RegisteredNote]):
    # TODO : regrouper par fichier
    for note in notes:
        with open(note.filepath) as f:
            content = f.read()
            qa_block = f"Q : {note.question}\nA : {note.answer}"
            new_block = qa_block + f"\n<!--ID: {note.note_id}-->"
            content = content.replace(qa_block, new_block)

        with open(note.filepath, "w") as f:
            f.write(content)
