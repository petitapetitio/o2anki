from datetime import time
from pathlib import Path

from o2anki.o2anki import O2Anki


def test_add_note_with_assets():
    O2Anki().export(Path("assets/a_vault_that_contains_card_with_assets"))


def test_export_folder():
    t = time()
    # O2Anki().export(Path("assets/client_assets"))
    O2Anki().export(Path("assets/a_test_vault"))
    print(f"Elapsed: {time() - t}")