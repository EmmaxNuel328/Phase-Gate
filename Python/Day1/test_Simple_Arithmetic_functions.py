import unittest
from Simple_Arithmetic_functions import *


class TestSimpleArithmeticFunctions(unittest.TestCase):
	def test_that_generate_random_first_number_is_the_same(self):
		actual =  generate_random_first_number()
		expected = actual
		self.assertEqual(actual,expected)