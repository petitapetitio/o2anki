from pathlib import Path

from o2anki.parsing.vault import Vault

for n in Vault.of(Path("/Users/lxnd/Documents/PCRAG/1 PROJETS/"))._notes:
    print(n)
