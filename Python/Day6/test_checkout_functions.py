import unittest
from checkout_functions import *

class TestCheckOutFunctions(unittest.TestCase):
	def test_that_calculate_vat_is_correct(self):
		actual = calculate_vat(380000.00)
		expected = 28500
		self.assertEqual(actual,expected)


	def test_that_calculate_vat_raise_value_error(self):
		actual = -1000
		self.assertRaises(ValueError,calculate_vat,actual)

	
	def test_that_add_vat_with_subtotal_returns_correct_value(self):
		actual = add_vat_with_subtotal(380000,28500)
		expected = 408500
		self.assertEqual(actual,expected)


	def test_that_add_vat_with_subtotal_does_not_return_negative_values(self):
		subtotal = -1000
		vat_amount = -1
		self.assertRaises(ValueError,add_vat_with_subtotal,subtotal,vat_amount)

	
	def test_that_give_balance_returns_correct_value(self):
		actual = give_balance(410000,408500)
		expected = 1500
		self.assertEqual(actual,expected)

	def test_that_give_balance_raises_value_error_if_paid_amount_is_less_than_grand_total(self):
		paid = 410
		grand_total = 1500
		self.assertRaises(ValueError,give_balance,paid,grand_total)

	
	