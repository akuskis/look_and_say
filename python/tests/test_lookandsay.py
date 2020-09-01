import unittest
from parameterized import parameterized

from src.common import lookandsay as common_lookandsay
from src.cosmo import lookandsay as cosmo_lookandsay


class TestLookAndFeel(unittest.TestCase):

    @parameterized.expand([[1, 1],
                           [2, 2],
                           [3, 2],
                           [30, 4462]])
    def test_get_length_of_sequence(self, index: int, expected: int):
        self.assertEqual(expected, common_lookandsay.get_length_of_sequence(index))
        self.assertEqual(expected, cosmo_lookandsay.get_length_of_sequence(index))

    def test_get_sequence(self):
        self.assertEqual(common_lookandsay.get_sequence(15),
                         "311311222113111231131112132112311321322112111312211312111322212311322113212221")

    def test_that_behavior_of_different_implementations_is_the_same(self):
        for i in range(1, 50):
            self.assertEqual(common_lookandsay.get_length_of_sequence(i), cosmo_lookandsay.get_length_of_sequence(i))
