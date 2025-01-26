
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

- [x] parser les cartes
  - [x] récupérer le nom du deck
  - [x] récupérer les tags
  - [x] parser un dossier de façon récursive
- [ ] interragir avec anki
  - [x] màj une carté déjà existante
  - [x] créer une nlle carte
    - commande "addNotes"
    - ajouter plusieurs notes en mode multi
    - ajouter une note qui contient une image
    - écrire l'id
    - créer les requests puis invoquer
  - [ ] instruction delete
- [x] màj mes cartes ANKI Python


Pour tester :
- créer un deck test dans un dossier en dehors de mon PCRAG
- forcer l'écriture dans un autre deck (écraser au niveau du parsing)
- checker que ça c'est bien passé
- vérifier une carte avec un média
- vérifier une carte avec du code
- hashes ??