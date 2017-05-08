import unittest
from prime_numbers import Prime_Numbers

class Test_Prime_Numbers(unittest.TestCase):

	def setUp(self):
		self.prime_numbers = Prime_Numbers()

	def test_correct_prime_numbers(self):
		self.assertEqual(self.prime_numbers.prime_numbers(10), [2,3,5,7])
		self.assertEqual(self.prime_numbers.prime_numbers(25), [2,3,5,7,11,13,17,19,23])

	def is_input_an_integer(self):
		self.assertEqual(self.prime_numbers.prime_numbers("4"), "Not an integer!!")

	def input_is_not_less_than_zero(self):
		self.assertEqual(self.prime_numbers.prime_numbers(-1), "Input is less than zero")