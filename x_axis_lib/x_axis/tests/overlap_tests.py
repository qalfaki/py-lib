import unittest
from ..overlap import (
    overlapping,
    InvalidValues,
)


class TestXAxisOverlapping(unittest.TestCase):

    def test_overlapping(self):
        self.assertTrue(overlapping({1, 4}, {2, 10}))
        self.assertTrue(overlapping({3, 4}, {1, 10}))
        self.assertTrue(overlapping({12, 4}, {10, 3}))
        self.assertTrue(overlapping({8, 19}, {4, 20}))

    def test_not_overlapping(self):

        # sets
        self.assertFalse(overlapping({1, 4}, {5, 10}))
        self.assertFalse(overlapping({3, 4}, {6, 10}))

        # Tuples
        self.assertFalse(overlapping((0, 1,), (2, 100,)))

        # lists
        self.assertFalse(overlapping([12, 4], [-10, 3]))
        self.assertFalse(overlapping([0, 1], [2, 100]))

    def test_invalid_params(self):
        with self.assertRaises(InvalidValues):
            overlapping({'a': 1, 'b': 3}, {'c': 4, 'd': 5})

        with self.assertRaises(InvalidValues):
            overlapping('a', 'b')

        with self.assertRaises(InvalidValues):
            overlapping(12, 17)


if __name__ == '__maine__':
    unittest.main(verbosity=1)
