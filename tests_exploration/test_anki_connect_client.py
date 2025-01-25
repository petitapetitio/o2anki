from pathlib import Path
from time import time

from o2anki.anki_connect_client import AnkiConnectClient
from o2anki.o2anki import O2Anki
from o2anki.parsing.folder import Folder
from tests.test_parsing_files import note


def test_add_card():
    client = AnkiConnectClient()
    req = client.add_basic_note_request(note("q1?", "r1", filepath="f.md"))
    note_id = client.invoke(req)
    print(note_id)


def test_add_note_with_assets_demo():
    client = AnkiConnectClient()
    client.invoke(
        {
            "action": "addNote",
            "version": 6,
            "params": {
                "note": {
                    "deckName": "Default",
                    "modelName": "Basic",
                    "fields": {"Front": "front content", "Back": "back content"},
                    "options": {
                        "allowDuplicate": False,
                        "duplicateScope": "deck",
                        "duplicateScopeOptions": {
                            "deckName": "Default",
                            "checkChildren": False,
                            "checkAllModels": False,
                        },
                    },
                    "tags": ["yomichan"],
                    "audio": [
                        {
                            "url": "https://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kanji=猫&kana=ねこ",
                            "filename": "yomichan_ねこ_猫.mp3",
                            "skipHash": "7e2c2f954ef6051373ba916f000168dc",
                            "fields": ["Front"],
                        }
                    ],
                    "video": [
                        {
                            "url": "https://cdn.videvo.net/videvo_files/video/free/2015-06/small_watermarked/Contador_Glam_preview.mp4",
                            "filename": "countdown.mp4",
                            "skipHash": "4117e8aab0d37534d9c8eac362388bbe",
                            "fields": ["Back"],
                        }
                    ],
                    "picture": [
                        {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/A_black_cat_named_Tilly.jpg/220px-A_black_cat_named_Tilly.jpg",
                            "filename": "black_cat.jpg",
                            "skipHash": "8d6e4646dfae812bf39651b59d7429ce",
                            "fields": ["Back"],
                        }
                    ],
                }
            },
        }
    )


def test_add_note_with_assets_html():
    client = AnkiConnectClient()
    client.invoke(
        {
            "action": "addNote",
            "version": 6,
            "params": {
                "note": {
                    "deckName": "Default",
                    "modelName": "Basic",
                    "fields": {
                        "Front": "front content",
                        "Back": "<p> du texte avant <img src='black_cat.jpg'/> et du texte après</p>",
                    },
                    "tags": ["yomichan"],
                    "picture": [
                        {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/A_black_cat_named_Tilly.jpg/220px-A_black_cat_named_Tilly.jpg",
                            "filename": "black_cat.jpg",
                            "skipHash": "8d6e4646dfae812bf39651b59d7429ce",
                            "fields": [],
                        }
                    ],
                }
            },
        }
    )


def test_add_note_with_assets_local_html():
    client = AnkiConnectClient()
    client.invoke(
        {
            "action": "storeMediaFile",
            "version": 6,
            "params": {
                "filename": "Pasted image 20250125152722.jpg",
                "path": "/Users/lxnd/dev/o2anki/tests/assets/a_vault_that_contains_card_with_assets/_assets/Pasted image 20250125152722.png"
            }
        }
    )
    client.invoke(
        {
            "action": "addNote",
            "version": 6,
            "params": {
                "note": {
                    "deckName": "Default",
                    "modelName": "Basic",
                    "fields": {
                        "Front": "front content local",
                        "Back": "<p> du texte avant <img src='Pasted image 20250125152722.jpg'/> et du texte après</p>",
                    },
                    "tags": ["yomichan"],
                }
            },
        }
    )


def test_add_note_with_assets():
    client = AnkiConnectClient()
    folder = Folder.of(Path("assets/a_vault_that_contains_card_with_assets"))
    # client.invoke(req)


def test_export_folder():
    t = time()
    # O2Anki().export(Path("assets/client_assets"))
    O2Anki().export(Path("test_vault"))
    print(f"Elapsed: {time() - t}")
