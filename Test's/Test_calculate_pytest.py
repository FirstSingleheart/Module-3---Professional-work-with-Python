import pytest
from main import multiplication_int, multiplication_string

parametrize_list = [(3, 3, 9), (1.5, 3, 4.5), (-5, 2, -10), (0, 5, 0), (1, 5, 5)]


class TestCalculatePytest:

    @classmethod
    def setup_class(cls):
        print('connect DB')

    def setup(self):
        print('Create user')

    @pytest.mark.parametrize('a, b, expected_result', parametrize_list)
    def test_multiplication_int(self, a, b, expected_result):
        assert multiplication_int(a, b) == expected_result

    def test_multiplication_string(self):
        assert multiplication_string('чпоньк', 3) == 'чпонькчпонькчпоньк'

    def teardown(self):
        print(' delete user')

    @classmethod
    def teardown_class(cls):
        print('disconnect DB')




        print('disconnect DB')