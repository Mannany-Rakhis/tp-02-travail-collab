import unittest

from campus import peut_inscrire


class TestIncidentA(unittest.TestCase):
    def test_inscription_possible_si_une_place_reste(self):
        self.assertTrue(peut_inscrire(2, 4))

    def test_inscription_refusee_quand_evenement_complet(self):
        self.assertFalse(peut_inscrire(4, 4))

    def test_inscription_refusee_si_capacite_nulle(self):
        self.assertFalse(peut_inscrire(0, 0))

    def test_entrees_hors_domaine_refusees(self):
        for inscrits, capacite in [(-1, 4), (5, 4), (0, -1)]:
            with self.subTest(inscrits=inscrits, capacite=capacite):
                with self.assertRaises(ValueError):
                    peut_inscrire(inscrits, capacite)


if __name__ == "__main__":
    unittest.main()
