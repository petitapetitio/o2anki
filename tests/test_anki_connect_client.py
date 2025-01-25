from pathlib import Path
from time import time

from o2anki.anki_connect_client import AnkiConnectClient
from o2anki.o2anki import O2Anki
from tests.test_parsing_files import note


# partir d'un fichier avec des cartes sans ID
# garder une copie du fichier
# écraser à la fin


def test_add_card():
    client = AnkiConnectClient()
    req = client.add_basic_note_request(note("q1?", "r1"))
    note_id = client.invoke(req)
    print(note_id)


def test_export_folder():
    t = time()
    # O2Anki().export(Path("assets/client_assets"))
    O2Anki().export(Path("test_vault"))
    print(f"Elapsed: {time() - t}")


