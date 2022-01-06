import unittest
import src

test_1_data = [
            ('2207 876234', 'Василий Гупкин'),
            ('11-2', 'Геннадий Покемонов'),
            ('10006', 'Аристарх Павлов'),
            ('19568', None)
        ]

test_2_data = [('56789', 'report', 'Arcentiy Perdidze', '3')]

test_3_data = ["2207 876234", "11-2", "10006"]


class TestSRC(unittest.TestCase):

    def setUp(self) -> None:
        print('Create new_user')

    def test_get_doc_owner_name(self):
        for user_input, answer in test_1_data:
            with self.subTest():
                self.assertEqual(src.get_doc_owner_name(user_input), answer)

    def test_add_new_doc(self):
        for number, type_, name, shelf in test_2_data:
            with self.subTest():
                self.assertEqual(src.add_new_doc(number, type_, name, shelf), shelf)

    def test_delete_doc(self):
        for number in test_3_data:
            with self.subTest():
                self.assertTrue(src.delete_doc(number))

    def tearDown(self) -> None:
        print('Delete new_user')


if __name__ == '__main__':
    unittest.main()
