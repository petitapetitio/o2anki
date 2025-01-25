
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
  - [ ] màj une carté déjà existante
  - [ ] créer une nlle carte
    - commande "addNotes"
    - ajouter plusieurs notes en mode multi
    - ajouter une note qui contient une image
    - écrire l'id
    - créer les requests puis invoquer
  - [ ] instruction delete
- [ ] màj mes cartes ANKI Python



Ajouter une nlle carte 

get_add_notes
get_delete_notes


```
if parsed.id is None:
  # Need to make sure global_tags get added.
  parsed.note["tags"] += self.global_tags.split(TAG_SEP)
  self.inline_notes_to_add.append(parsed.note)
  self.inline_id_indexes.append(position)
```