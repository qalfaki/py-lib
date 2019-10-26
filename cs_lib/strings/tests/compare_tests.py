import unittest

from ..compare import compare
from ..custom_exceptions import InvalidValues


class TestCompareFunction(unittest.TestCase):

    def test_compare_equals(self):
        '''Test equality of the 2 versions'''
        self.assertEqual(
            compare('1.2.3', '1.2.3'),
            1,
            'returned value should be 1, since str1 = str2')

        self.assertEqual(
            compare('1.2.3.0', '1.2.3.0'),
            1,
            'it should return 1 since str1 = str2')

        self.assertEqual(
            compare('0', '0'),
            1,
            'it should return 1 since str1 = str2')

    def test_compare_greater_than(self):
        self.assertEqual(
            compare('011.2.3', '11.2.3'),
            0,
            'it should return 0 since str1 > str2')

        self.assertEqual(
            compare('11.2.3.0', '11.2.3'),
            0,
            'it should return 0 since str1 > str2')

        self.assertEqual(
            compare('11.2.4', '11.2.3'),
            0,
            'it should return 0 since str1 > str2')

    def test_compare_less_than(self):
        self.assertEqual(
            compare('1.2.3', '11.2.3'),
            -1,
            'it should return -1 since str1 < str2')

        self.assertEqual(
            compare('1.2.3', '1.2.3.0 0'),
            -1,
            'it should return -1 since str1 < str2')

        self.assertEqual(
            compare('1.2.3', '01.2.3'),
            -1,
            'it should return -1 since str1 < str2')

    def test_compare_invalid_params(self):
        for args in [['1.2.3', []], [{}, {}], [[], []], [None, map]]:
            with self.assertRaises(InvalidValues):
                compare(*args)


if __name__ == '__main__':
    unittest.main(verbosity=1)
