import unittest
from Modified_mini_parking_functions import *

class TestModifiedMiniParkingFunctions(unitttest.TestCase):
	def test_that_is_slot_occupied_or_empty_returns_0_if_slot_is(self):
		actual = is_slot_occupied_or_empty([])
		expected = 0
		self.assertEqual(actual,expected) 