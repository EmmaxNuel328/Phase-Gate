import unittest
from Day4_functions import *

class TestDay4Functions(unittest.TestCase):
	def test_that_is_perfect_square_returns_boolean(self):
		list = 21
		actual = is_perfect_square(list)
		expected = False
		self.assertEqual(actual,expected)