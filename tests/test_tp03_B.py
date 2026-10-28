import unittest

from campus import places_restantes


class TestIncidentB(unittest.TestCase):
    def test_places_restantes_cas_normal(self):
        self.assertEqual(places_restantes(1, 4), 3)

    def test_evenement_vide_sans_capacite(self):
        self.assertEqual(places_restantes(0, 0), 0)

    def test_places_restantes_cas_original(self):
        with self.assertRaises(ValueError):
            places_restantes(5, 4)

    def test_frontiere_capacite_atteinte(self):
        self.assertEqual(places_restantes(4, 4), 0)

    def test_entrees_hors_domaine_refusees(self):
        for inscrits, capacite in [(-1, 4), (5, 4), (0, -1)]:
            with self.subTest(inscrits=inscrits, capacite=capacite):
                with self.assertRaises(ValueError):
                    places_restantes(inscrits, capacite)


if __name__ == "__main__":
    unittest.main()
