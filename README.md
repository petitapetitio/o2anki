
# Comment tester

```
python -m venv ../venvs/o2anki
source ../venvs/o2anki
python -m ensurepip --upgrade
python -m pip install setuptools --upgrade
python -m pip install -r requirements.txt
```

# TODO 

- parser les cartes
  - récupérer le nom du deck
  - récupérer les tags
  - parser un dossier de façon récursive
- enregistrer les cartes