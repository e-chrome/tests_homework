import unittest
from data import documents, directories

from functions import get_name_by_number, get_shelf_by_number, get_docs_list, add_new_doc, \
    delete_doc, move_doc_to_another_shelf, add_shelf, get_shelfs_list


class TestFunctions(unittest.TestCase):
    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_get_name_by_number(self):
        self.assertEqual(get_name_by_number(documents, '11-2'), 'Геннадий Покемонов')

    def test_get_shelf_by_number(self):
        self.assertEqual(get_shelf_by_number(directories, '11-2'), '1')

    def test_get_docs_list(self):
        self.assertEqual(get_docs_list(documents), documents)

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('passport', '1', 'Илья Огурцов', '1'), 'success')

    def test_delete_doc(self):
        self.assertEqual(delete_doc('2207 876234'), 'success')

    def test_move_doc_to_another_shelf(self):
        self.assertEqual(move_doc_to_another_shelf('11-2', '3'), 'success')

    def test_add_shelf(self):
        self.assertEqual(add_shelf('4'), 'success')

    def test_get_shelfs_list(self):
        self.assertEqual(get_shelfs_list(directories), 'success')


if __name__ == '__main__':
    unittest.main()