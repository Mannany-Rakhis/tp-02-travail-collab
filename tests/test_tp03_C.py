import unittest

from campus import normaliser_nom


class TestIncidentC(unittest.TestCase):
    def test_nom_avec_espaces_autour(self):
        self.assertEqual(normaliser_nom(" ALICE "), "alice")

    def test_espaces_interieurs_conserves(self):
        self.assertEqual(normaliser_nom("Anne Marie"), "anne marie")

    def test_nom_vide_refuse(self):
        for nom in ["", "   "]:
            with self.subTest(nom=nom):
                with self.assertRaises(ValueError):
                    normaliser_nom(nom)

    def test_espaces_ascii_autour_dun_nom_cas_original(self):
        self.assertEqual(normaliser_nom("\tÉlodie \n"), "élodie")


if __name__ == "__main__":
    unittest.main()
