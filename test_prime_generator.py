import unittest
from generate_prime_numbers import generate_prime_numbers

class PrimeNumberGenerator(unittest.TestCase):
	# Tests whether it returns expected prime numbers
	def test_generate_prime_numbers_returns_prime_numbers(self):
		self.assertEqual(generate_prime_numbers(13), [2, 3, 5, 7, 11, 13], "Fail: The function is not working!")

	#Tests whether it rejects negative numbers and responds with appropriate instructions
	def test_generate_prime_numbers_rejects_negative_numbers(self):
		self.assertEqual(generate_prime_numbers(-10), "Please enter a positive integer", "Fail: No handling of negative numbers!")

	#Tests whether it rejects numbers with decimals and responds with appropriate instructions
	def test_generate_prime_numbers_checks_for_integers_only(self):
		self.assertEqual(generate_prime_numbers(53.34), "That is not an integer. Please enter a number without a decimal", "Fail: No handling of non integers like decimals")

	#Tests whether the return value is of the list type
	def test_generate_prime_numbers_produces_a_list(self):
		self.assertEqual(isinstance(generate_prime_numbers(13), list), True, "Fail: Output is NOT in a list format")

	#Tests to see if the prime numbers produced have a maximum limit of the given N
	def test_generate_prime_numbers_if_the_upper_limit_is_N(self):
		self.assertEqual(generate_prime_numbers(20)[-1] <= 20, True, "Fail: Limit is wrong")

if __name__ == '__main__':
	unittest.main()