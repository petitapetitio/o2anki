
# Comment tester

```
python -m venv ../venvs/o2anki
source ../venvs/o2anki
python -m ensurepip --upgrade
python -m pip install setuptools --upgrade
python -m pip install -r requirements.txt
```

# Spécifications

Formatage des notes
- Une question commence par `Q : `en début de ligne
- Une réponse commence par `A : ` en début de ligne 

Target deck
- Un target deck peut être précisé pour un fichier (`TARGET DECK: <deck-name>`)
- La position de l'instruction n'importe pas (elle peut être à la findu fichier)
- Seule la première instruction `TARGET DECK: ` du fichier sera prise en compte

# TODO 

- [ ] parser les cartes
  - [ ] récupérer le nom du deck
  - [ ] récupérer les tags
  - [x] parser un dossier de façon récursive
- [ ] enregistrer les cartes