import unittest
from generate_prime_numbers import generate_prime_numbers

class PrimeNumberGenerator(unittest.TestCase):
	def test_generate_prime_numbers_returns_prime_numbers(self):
		self.assertEqual(generate_prime_numbers(13), [2, 3, 5, 7, 11, 13], "Fail: The function is not working!")

	def test_generate_prime_numbers_rejects_negative_numbers(self):
		self.assertEqual(generate_prime_numbers(-10), "Please enter a positive integer", "Fail: No handling of negative numbers!")

	def test_generate_prime_numbers_checks_for_integers_only(self):
		self.assertEqual(generate_prime_numbers(53.34), "That is not an integer. Please enter a number without a decimal", "Fail: No handling of non integers like decimals")

	def test_generate_prime_numbers_produces_a_list(self):
		self.assertEqual(isinstance(generate_prime_numbers(13), list), True, "Fail: Output is NOT in a list format")

if __name__ == '__main__':
	unittest.main()