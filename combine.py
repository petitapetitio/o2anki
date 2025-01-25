from pathlib import Path

with open("o2anki.txt", "w") as output:
    for p in Path("o2anki").glob("**/*.py"):
        with open(p) as file:
            output.write(f"\n# {p}")
            output.write(file.read())
