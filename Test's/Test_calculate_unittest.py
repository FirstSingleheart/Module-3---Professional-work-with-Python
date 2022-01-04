import unittest
from main import multiplication_int, multiplication_string


class TestCalculateUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('connect DB')

    def setUp(self) -> None:
        print('setUp create user')

    def test_multiplication_int(self):
        self.assertEqual(multiplication_int(3, 3), 9, 'значения не совпали')

    def test_multiplication_string(self):
        self.assertEqual(multiplication_string('чпуньк', 3), 'чпунькчпунькчпуньк')

    def tearDown(self) -> None:
        print('tearDown delete user')

    @classmethod
    def tearDownClass(cls) -> None:
        print('disconnect DB')


if __name__ == '__main__':
    unittest.main()