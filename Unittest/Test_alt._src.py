import unittest
from src import delete_doc, add_new_doc, get_doc_owner_name


class TestSRC(unittest.TestCase):

    def setUp(self):
        print('Create new_user')

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('2207 876234'), 'Василий Гупкин')

    def test_get_doc_owner_name_1(self):
        self.assertEqual(get_doc_owner_name('11-2'), 'Геннадий Покемонов')

    def test_get_doc_owner_name_2(self):
        self.assertEqual(get_doc_owner_name('10006'), 'Аристарх Павлов')

    def test_get_doc_owner_name_3(self):
        self.assertEqual(get_doc_owner_name('19568'), None)

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('56789', 'report', 'Arcadiy Pupkin', '3'), '3')

    def test_delete_doc(self):
        self.assertEqual(delete_doc('2207 876234'), ('2207 876234', True))

    def test_delete_doc_1(self):
        self.assertEqual(delete_doc('11-2'), ('11-2', True))

    def test_delete_doc_2(self):
        self.assertEqual(delete_doc('10006'), ('10006', True))

    def test_delete_doc_3(self):
        self.assertEqual(delete_doc('19568'), None)

    def tearDown(self):
        print('Delete new_user')


if __name__ == '__main__':
    unittest.main()