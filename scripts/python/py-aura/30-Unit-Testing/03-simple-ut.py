import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
	def test_is_five_prime(self):
		print ("I am in test_is_five_function")
		self.assertFalse(is_prime(9))

if __name__ == '__main__':
    unittest.main()
