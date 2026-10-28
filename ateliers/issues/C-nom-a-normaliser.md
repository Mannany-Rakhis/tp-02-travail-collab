# C — Normaliser les noms sans perdre les espaces intérieurs

## Besoin

La normalisation doit rendre équivalents les noms avec des espaces périphériques, tout en conservant les espaces à l'intérieur du nom. Un nom vide après nettoyage doit être refusé.

## Reproduction

Sur le code initial, `normaliser_nom(" ALICE ")` conserve les espaces autour du nom, et `normaliser_nom("   ")` renvoie une chaîne vide au lieu de signaler une entrée invalide.

## Résultat attendu

- `normaliser_nom(" ALICE ")` renvoie `"alice"`.
- `normaliser_nom("Anne Marie")` renvoie `"anne marie"` : l'espace intérieur est conservé.
- Une chaîne vide ou composée uniquement d'espaces est refusée avec `ValueError`.
- Les espaces ASCII périphériques, y compris tabulations et retours à la ligne, sont retirés.

Le test de régression correspondant est dans [`tests/test_tp03_C.py`](../../tests/test_tp03_C.py).
