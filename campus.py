"""Règles métier de Campus Events."""


def peut_inscrire(inscrits: int, capacite: int) -> bool:
    """Indique si une nouvelle inscription est possible.

    Lève ValueError si les inscrits ou la capacité sont hors du domaine valide.
    """
    if capacite < 0 or inscrits < 0 or inscrits > capacite:
        raise ValueError("inscrits et capacité doivent être dans le domaine valide")
    return inscrits < capacite


def places_restantes(inscrits: int, capacite: int) -> int:
    """Calcule les places disponibles après validation du domaine métier."""
    if capacite < 0 or inscrits < 0 or inscrits > capacite:
        raise ValueError("inscrits et capacité doivent être dans le domaine valide")
    return capacite - inscrits


def normaliser_nom(nom: str) -> str:
    """Met le nom en minuscules et retire les espaces périphériques."""
    nom_normalise = nom.strip().lower()
    if not nom_normalise:
        raise ValueError("le nom ne peut pas être vide")
    return nom_normalise
