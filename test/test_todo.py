import unittest
from src.todo import ajouter, lister, marquer_faite, supprimer, taches


class TestTodo(unittest.TestCase):
    def setUp(self):
        # Réinitialiser les tâches avant chaque test
        taches.clear()

    def test_ajouter(self):
        ajouter("Apprendre Python")
        self.assertEqual(len(taches), 1)
        self.assertEqual(taches[0]["titre"], "Apprendre Python")
        self.assertFalse(taches[0]["faite"])

    def test_lister_vide(self):
        # Capture l'affichage si aucune tâche
        from io import StringIO
        import sys

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            lister()
            output = out.getvalue().strip()
            self.assertEqual(output, "Aucune tâche.")
        finally:
            sys.stdout = saved_stdout

    def test_marquer_faite(self):
        ajouter("Lire un livre")
        marquer_faite(1)
        self.assertTrue(taches[0]["faite"])

    def test_supprimer(self):
        ajouter("Faire du sport")
        supprimer(1)
        self.assertEqual(len(taches), 0)


if __name__ == "__main__":
    unittest.main()
