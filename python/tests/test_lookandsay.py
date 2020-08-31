import unittest
from parameterized import parameterized

from src import lookandsay


class TestLookAndFeel(unittest.TestCase):

    @parameterized.expand([[0, 0],
                           [1, 1],
                           [2, 2],
                           [3, 2],
                           [30, 4462]])
    def test_get_length_of_sequence(self, index: int, expected: int):
        self.assertEqual(expected, lookandsay.get_length_of_sequence(index))

    def test_get_sequence(self):
        self.assertEqual(lookandsay.get_sequence(15),
                         "311311222113111231131112132112311321322112111312211312111322212311322113212221")
