
# Comment installer

```
python -m venv ../venvs/o2anki
source ../venvs/o2anki
python -m ensurepip --upgrade
python -m pip install setuptools --upgrade
python -m pip install -r requirements.txt
```

Pour exécuter les tests : 
```
pytest
```

# Spécifications

Formatage des notes
- Une question commence par `Q : ` (en début de ligne)
- Une réponse commence par `A : ` (en début de ligne)

Target deck
- Le target deck peut doit être précisé pour chaque fichier fichier (`TARGET DECK: <deck-name>`)
- Le target deck peut être déclaré n'import où dans le fichier (y compris à la fin)
- Un seul target deck peut être déclaré

# TODO 

- [ ] recetter sur mon deck d'anglais (en cours)
- [ ] prendre en charge l'instruction delete
- [ ] ajouter du css pour les blocs de code
