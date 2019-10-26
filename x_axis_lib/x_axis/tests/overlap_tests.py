import unittest
from ..overlap import overlapping

class TestXAxisOverlapping(unittest.TestCase):

    def test_overlapping(self):
        self.assertTrue(overlapping({1, 4}, {2, 10}))
        self.assertTrue(overlapping({3, 4}, {1, 10}))
        self.assertTrue(overlapping({12, 4}, {10, 3}))
        self.assertTrue(overlapping({8, 19}, {4, 20}))

    def test_not_overlapping(self):
        self.assertFalse(overlapping({1, 4}, {5, 10}))
        self.assertFalse(overlapping({3, 4}, {6, 10}))
        self.assertFalse(overlapping({12, 4}, {-10, 3}))
        self.assertFalse(overlapping({0, 1}, {2, 100}))


if __name__== "__maine__":
    unittest.main(verbosity=1)
