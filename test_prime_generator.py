import unittest
from generate_prime_numbers import generate_prime_numbers

class PrimeNumberGenerator(unittest.TestCase):
	def test_generate_prime_numbers_returns_prime_numbers(self):
		self.assertEqual(generate_prime_numbers(13), [2, 3, 5, 7, 11, 13], "Fail: The function is not working!")

if __name__ == '__main__':
	unittest.main()