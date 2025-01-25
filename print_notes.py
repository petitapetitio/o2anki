from pathlib import Path

from o2anki.parsing.folder import Folder

for n in Folder(Path("/Users/lxnd/Documents/PCRAG/1 PROJETS/")).notes():
    print(n)
