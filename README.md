
# How to install

```
python -m venv ../venvs/o2anki
source ../venvs/o2anki
python -m ensurepip --upgrade
python -m pip install setuptools --upgrade
python -m pip install -r requirements.txt
```

To execute the tests : 
```
pytest
```

# Spécifications

Note formatting : 
- a question is marked by a line that starts with `Q : `
- an answer is marked by a line that start with `A : `

Target deck
- the target deck as to be explicited for each file (`TARGET DECK: <deck-name>`)
- the target deck can be declared anywhere in the file 
- only one target deck declaration can be present in a file

# TODO 

- [ ] recetter sur mon deck d'anglais (en cours)
- [ ] adding `DELETE: ID` tag handling
- [ ] adding css and code_hilite for code blocs


# Resources

- https://github.com/ObsidianToAnki/Obsidian_to_Anki
- https://foosoft.net/projects/anki-connect/