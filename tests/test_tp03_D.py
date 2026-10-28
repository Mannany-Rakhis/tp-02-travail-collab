import unittest

from campus import taux_remplissage


class TestIncidentD(unittest.TestCase):
    def test_taux_nominal(self):
        self.assertEqual(taux_remplissage(2, 4), 50.0)

    def test_capacite_nulle_et_evenement_vide(self):
        self.assertEqual(taux_remplissage(0, 0), 0.0)

    def test_taux_remplissage_cas_original(self):
        self.assertEqual(taux_remplissage(1, 2), 50.0)

    def test_entrees_hors_domaine_refusees(self):
        for inscrits, capacite in [(-1, 4), (5, 4), (0, -1)]:
            with self.subTest(inscrits=inscrits, capacite=capacite):
                with self.assertRaises(ValueError):
                    taux_remplissage(inscrits, capacite)


if __name__ == "__main__":
    unittest.main()
