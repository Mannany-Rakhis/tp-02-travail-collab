# D — Calculer le taux d'un événement vide sans capacité

## Besoin

Un événement sans inscrit et de capacité nulle est valide ; son taux de remplissage doit être `0.0` au lieu d'interrompre le calcul.

## Reproduction

Sur le code initial, `taux_remplissage(0, 0)` déclenche `ZeroDivisionError`.

## Résultat attendu

- `taux_remplissage(0, 0)` renvoie `0.0`.
- Pour une capacité positive, le taux est calculé correctement en pourcentage.
- Les entrées numériques hors domaine lèvent `ValueError`.

Le test de régression correspondant est dans [`tests/test_tp03_D.py`](../../tests/test_tp03_D.py).
