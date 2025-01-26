from pathlib import Path

import pytest

from o2anki.parsing.vault import Vault
from tests.conftest import TEST_ASSETS_DIR
from tests.test_parsing_files import note


def test_parsing_vault():
    vault = Vault.of(
        TEST_ASSETS_DIR / "folder", (TEST_ASSETS_DIR / "folder/excluded_folder",)
    )
    assert set(vault.unregistered_notes()) == {
        note("question 1 ?", "answer 1", filepath=TEST_ASSETS_DIR / "folder/card1.md"),
        note("question 2 ?", "answer 2", filepath=TEST_ASSETS_DIR / "folder/card2.md"),
        note(
            "question 3 ?",
            "answer 3",
            filepath=TEST_ASSETS_DIR / "folder/subfolder/card3.md",
        ),
    }


def test_passing_unrelated_excluded_folders_raise_an_exception():
    with pytest.raises(ValueError):
        Vault.of(Path(TEST_ASSETS_DIR / "folder"), (Path("another/radix"),))


def test_parsing_vault_with_assets():
    vault_path = Path(TEST_ASSETS_DIR / "a_vault_that_contains_card_with_assets")
    vault = Vault.of(vault_path)
    assert vault.media == {
        "media.png": (
            Path(TEST_ASSETS_DIR / "a_vault_that_contains_card_with_assets")
            / "_assets"
            / "media.png"
        ).resolve()
    }
