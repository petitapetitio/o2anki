import sys
from pathlib import Path

from o2anki.o2anki import O2Anki

if __name__ == "__main__":
    folder = sys.argv[1]
    print(f"Run on '{folder}'")
    app = O2Anki()
    app.export(Path(folder))
