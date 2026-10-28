# B — Refuser les entrées invalides pour les places restantes

## Besoin

Le calcul des places restantes ne doit pas masquer les données incohérentes : les valeurs numériques hors domaine doivent être refusées.

## Reproduction

Sur le code initial, `places_restantes(5, 4)` renvoie `-1`, alors que les inscrits dépassent la capacité.

## Résultat attendu

- `places_restantes(1, 4)` renvoie `3`.
- `places_restantes(0, 0)` renvoie `0`.
- `places_restantes(4, 4)` renvoie `0`.
- Une capacité négative, des inscrits négatifs ou des inscrits supérieurs à la capacité lèvent `ValueError`.

Le test de régression correspondant est dans [`tests/test_tp03_B.py`](../../tests/test_tp03_B.py).
