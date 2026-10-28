# A — Refuser l'inscription quand l'événement est complet

## Besoin

Une nouvelle inscription ne doit pas être acceptée lorsque le nombre d'inscrits a atteint la capacité de l'événement.

## Reproduction

Sur le code initial, `peut_inscrire(4, 4)` renvoie `True`, alors que l'événement est déjà complet.

## Résultat attendu

- `peut_inscrire(4, 4)` renvoie `False`.
- `peut_inscrire(2, 4)` renvoie `True`.
- `peut_inscrire(0, 0)` renvoie `False`.
- Les valeurs numériques hors domaine lèvent `ValueError`.

Le test de régression correspondant est dans [`tests/test_tp03_A.py`](../../tests/test_tp03_A.py).
