import unittest
from src import get_doc_owner_name, add_new_doc, delete_doc
from parameterized import parameterized

test_1_data = [
            ("2207 876234", "Василий Гупкин"),
            ("11-2", "Геннадий Покемонов"),
            ("10006", "Аристарх Павлов"),
            ("19568", None)
        ]

test_2_data = ('56789', 'report', 'Arcadiy Pupkin', '3')

test_3_data = ("2207 876234", "11-2", "10006", "19568")


class TestSRC(unittest.TestCase):
    def setUp(self) -> None:
        print('Create new_user')

    @parameterized.expand(test_1_data)
    def test_get_doc_owner_name(self, user_input, answer):
        self.assertEqual(get_doc_owner_name(user_input), answer)

    @parameterized.expand(test_2_data)
    def test_add_new_doc(self, number, type_, name, shelf):
        self.assertEqual(add_new_doc(number, type_, name, shelf), shelf)

    @parameterized.expand(test_3_data)
    def test_delete_doc(self, number):
        self.assertTrue(delete_doc(number))

    def tearDown(self) -> None:
        print('Delete new_user')


if __name__ == '__main__':
    unittest.main()
