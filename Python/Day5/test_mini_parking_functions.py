import unittest
from mini_parking_functions import *


class TestMiniParkingFunctions(unittest.TestCase):
	def test_that_is_empty_returns_0(self):
		actual = is_empty()
		expected = 0
		self.assertEqual(actual,expected)


	def test_that_is_occupied_returns_1(self):
		actual = is_occupied()
		expected = 1
		self.assertEqual(actual,expected)
		
	def test_that_enter_a_particular_Parking_lot_return_you_cannot_park_here_is_empty(self):
		car_name = "we"
		slot = [1,2,3,4,4,5,5,5,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,]
		actual = enter_parking_lot(slot,slot)
		expected = "No space"
		self.assertEqual(actual,expected)

	def test_that_is_leave_parking_lot_returns_No_car_here_if_slot_number_is_empty(self):
		actual = []
		slot_number = 1
		self.assertRaises(ValueError,leave_parking_lot,slot_number,actual)
		

	
	
		




