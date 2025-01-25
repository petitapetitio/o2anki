from pathlib import Path

from o2anki.parsing.folder import Folder

for n in Folder.of(Path("/Users/lxnd/Documents/PCRAG/1 PROJETS/"))._notes:
    print(n)
