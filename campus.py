"""Règles métier de Campus Events."""


def peut_inscrire(inscrits: int, capacite: int) -> bool:
    """Indique si une nouvelle inscription est possible.

    Lève ValueError si les inscrits ou la capacité sont hors du domaine valide.
    """
    if capacite < 0 or inscrits < 0 or inscrits > capacite:
        raise ValueError("inscrits et capacité doivent être dans le domaine valide")
    return inscrits < capacite
