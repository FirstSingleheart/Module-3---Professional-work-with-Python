import unittest
import Yandex_service as ya_disk


class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('start test')

    def test_success_create_folder(self):
        self.assertEqual(ya_disk.create_folder('test'), 201, 'Ошибка сервера')

    def test_passed_create_folder(self):
        self.assertEqual(ya_disk.create_folder('test_passed'), 409)

    def tearDown(self):
        ya_disk.delete_folder('test')
        print('end test')


if __name__ == '__main__':
    unittest.main()