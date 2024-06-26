import unittest
from linked_list.list import List


class TestList(unittest.TestCase):

    def test_search_by_pos(self):
        lista = List()
        lista.insert_last(1)
        lista.insert_last(2)
        lista.insert_last(3)
        self.assertEqual(lista.get_by_pos(1), 1)
        self.assertEqual(lista.get_by_pos(2), 2)
        self.assertEqual(lista.get_by_pos(3), 3)

    def test_search_by_value(self):
        lista = List()
        lista.insert_last(1)
        lista.insert_last(2)
        lista.insert_last(3)
        self.assertTrue(lista.get_by_value(1))
        self.assertTrue(lista.get_by_value(2))
        self.assertTrue(lista.get_by_value(3))
        with self.assertRaises(Exception):
            lista.get_by_value(4)

    def test_insert_last(self):
        lista = List()
        lista.insert_last(1)
        self.assertEqual(lista.get_last(), 1)
        self.assertEqual(lista.get_first(), 1)
        lista.insert_last(2)
        self.assertEqual(lista.get_last(), 2)
        self.assertEqual(lista.get_first(), 1)
        lista.insert_last(3)
        self.assertEqual(lista.get_last(), 3)
        self.assertEqual(lista.get_first(), 1)

    def test_insert_first(self):
        lista = List()
        lista.insert_first(1)
        self.assertEqual(lista.get_last(), 1)
        self.assertEqual(lista.get_first(), 1)
        lista.insert_first(2)
        self.assertEqual(lista.get_last(), 1)
        self.assertEqual(lista.get_first(), 2)
        lista.insert_first(3)
        self.assertEqual(lista.get_last(), 1)
        self.assertEqual(lista.get_first(), 3)

    def test_insert_by_pos(self):
        lista = List()
        lista.insert_last(1)
        self.assertEqual(lista.get_last(), 1)
        self.assertEqual(lista.get_first(), 1)
        lista.insert_by_pos(1, 2)
        self.assertEqual(lista.get_last(), 1)
        self.assertEqual(lista.get_first(), 2)
        lista.insert_by_pos(2, 3)
        self.assertEqual(lista.get_by_pos(1), 2)
        self.assertEqual(lista.get_by_pos(2), 3)
        self.assertEqual(lista.get_by_pos(3), 1)
        lista.insert_by_pos(3, 4)
        self.assertEqual(lista.get_by_pos(1), 2)
        self.assertEqual(lista.get_by_pos(2), 3)
        self.assertEqual(lista.get_by_pos(3), 4)
        self.assertEqual(lista.get_by_pos(4), 1)

    def test_remove_first(self):
        lista = List()
        lista.insert_last(1)
        self.assertEqual(lista.remove_first(), 1)
        self.assertRaises(Exception, lista.get_first)
        lista.insert_last(1)
        lista.insert_last(2)
        lista.insert_last(3)
        self.assertEqual(lista.get_first(), 1)
        self.assertEqual(lista.get_last(), 3)
        self.assertEqual(lista.remove_first(), 1)
        self.assertEqual(lista.get_first(), 2)
        self.assertEqual(lista.get_last(), 3)
        self.assertEqual(lista.remove_first(), 2)
        self.assertEqual(lista.get_first(), 3)
        self.assertEqual(lista.get_last(), 3)
        self.assertEqual(lista.remove_first(), 3)
        self.assertRaises(Exception, lista.get_first)
        self.assertRaises(Exception, lista.get_last)

    def test_remove_last(self):
        lista = List()
        lista.insert_last(1)
        self.assertEqual(lista.remove_last(), 1)
        self.assertRaises(Exception, lista.get_first)
        lista.insert_last(1)
        lista.insert_last(2)
        lista.insert_last(3)
        self.assertEqual(lista.get_first(), 1)
        self.assertEqual(lista.get_last(), 3)
        self.assertEqual(lista.remove_last(), 3)
        self.assertEqual(lista.get_first(), 1)
        self.assertEqual(lista.get_last(), 2)
        self.assertEqual(lista.remove_last(), 2)
        self.assertEqual(lista.get_first(), 1)
        self.assertEqual(lista.get_last(), 1)
        self.assertEqual(lista.remove_last(), 1)
        self.assertRaises(Exception, lista.get_first)
        self.assertRaises(Exception, lista.get_last)

    def test_remove_by_pos(self):
        lista = List()
        lista.insert_last(1)
        lista.insert_last(2)
        lista.insert_last(3)
        lista.insert_last(4)
        self.assertEqual(lista.get_by_pos(1), 1)
        self.assertEqual(lista.get_by_pos(2), 2)
        self.assertEqual(lista.get_by_pos(3), 3)
        self.assertEqual(lista.get_by_pos(4), 4)
        self.assertEqual(lista.remove_by_pos(1), 1)
        self.assertEqual(lista.get_by_pos(1), 2)
        self.assertEqual(lista.get_by_pos(2), 3)
        self.assertEqual(lista.get_by_pos(3), 4)
        lista.insert_last(5)
        self.assertEqual(lista.remove_by_pos(2), 3)
        self.assertEqual(lista.get_by_pos(1), 2)
        self.assertEqual(lista.get_by_pos(2), 4)
        self.assertEqual(lista.get_by_pos(3), 5)
        self.assertEqual(lista.remove_by_pos(3), 5)
        self.assertEqual(lista.get_by_pos(1), 2)
        self.assertEqual(lista.get_by_pos(2), 4)
        with self.assertRaises(Exception):
            lista.get_by_pos(3)
        self.assertEqual(lista.remove_by_pos(1), 2)
        self.assertEqual(lista.remove_by_pos(1), 4)
        with self.assertRaises(Exception):
            lista.get_by_pos(1)
        self.assertRaises(Exception, lista.get_first)
        self.assertRaises(Exception, lista.get_last)

    def test_remove_by_value(self):
        lista = List()
        lista.insert_last(1)
        self.assertTrue(lista.remove_by_value(1))
        self.assertRaises(Exception, lista.get_first)
        lista.insert_last(1)
        lista.insert_last(2)
        lista.insert_last(3)
        self.assertTrue(lista.remove_by_value(2))
        self.assertEqual(lista.get_first(), 1)
        self.assertEqual(lista.get_last(), 3)
        self.assertTrue(lista.remove_by_value(3))
        self.assertEqual(lista.get_first(), 1)
        self.assertEqual(lista.get_last(), 1)
        with self.assertRaises(Exception):
            lista.remove_by_value(4)
        self.assertTrue(lista.remove_by_value(1))
        self.assertRaises(Exception, lista.get_first)
