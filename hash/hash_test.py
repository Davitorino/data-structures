from unittest import TestCase
from hash import Hash


class HashTest(TestCase):

    def test_incluir(self):
        hash_test = Hash(1000, 3)
        hash_test.incluir(1)
        self.assertEqual(hash_test.buscar(1), 1)
        hash_test.incluir(444)
        self.assertEqual(hash_test.buscar(444), 444)

    def test_excluir(self):
        hash_test = Hash(1000, 3)
        hash_test.incluir(1)
        hash_test.excluir(1)
        with self.assertRaises(Exception):
            hash_test.buscar(1)
        hash_test.incluir(444)
        hash_test.excluir(444)
        with self.assertRaises(Exception):
            hash_test.buscar(444)
