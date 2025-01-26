from pathlib import Path

from o2anki.anki_connect_client import AnkiConnectClient
from o2anki.note_presenter import NotePresenter
from o2anki.parsing.registered_note import RegisteredNote
from o2anki.parsing.vault import Vault


class O2Anki:
    def __init__(self):
        self.client = AnkiConnectClient()
        self.presenter = NotePresenter()

    def export(self, folder: Path):

        folder = Vault.of(folder)

        self.client.check_connection()

        # create the decks
        for deck_name in folder.decks:
            request = self.client.create_deck(deck_name)
            self.client.invoke(request)

        # add the media files
        media_requests = []
        for filename, filepath in folder.media.items():
            media_requests.append(self.client.add_media_request(filename, str(filepath)))
        self.client.invoke_requests(media_requests)

        # create the notes
        create_note_requests = []
        unregistered_notes = list(folder.unregistered_notes())
        for unregistered_note in unregistered_notes:
            create_note_requests.append(
                self.client.add_basic_note_request(
                    question=self.presenter.convert(unregistered_note.question),
                    answer=self.presenter.convert(unregistered_note.answer),
                    target_deck=unregistered_note.target_deck,
                    file_tags=unregistered_note.file_tags,
                )
            )
        create_note_results = self.client.invoke_requests(create_note_requests)

        # update the notes
        update_notes_requests = []
        for note_to_update in list(folder.registered_notes()):
            update_notes_requests.append(
                self.client.update_note_request(
                    question=self.presenter.convert(note_to_update.question),
                    answer=self.presenter.convert(note_to_update.answer),
                    note_id=note_to_update.note_id,
                    tags=note_to_update.file_tags,
                )
            )
        self.client.invoke_requests(update_notes_requests)

        # write the ids
        registered_notes = []
        for unregistered_note, note_id in zip(unregistered_notes, create_note_results):
            registered_notes.append(
                RegisteredNote(
                    unregistered_note.question,
                    unregistered_note.answer,
                    note_id,
                    unregistered_note.filepath,
                )
            )

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
