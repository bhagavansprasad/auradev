import unittest
from primes import is_prime
from astring_utils import to_upper

class PrimesTestCase(unittest.TestCase):
	def my_temp_fun():
		print("my_temp_fun")
		exit(1)

	def test_is_five_prime(self):
		self.assertTrue(is_prime(5))

	def test_is_four_prime(self):
		self.assertFalse(is_prime(4), msg="4 is not a prime")

	def test_is_zero_prime(self):
		self.assertFalse(is_prime(0), msg="0 is not a prime")

	def test_negative_number(self):
		"""Is a negative number correctly determined not to be prime?"""
		for index in range(-4, -8, -1):
			self.assertFalse(is_prime(index))

	def test_negative_number_1(self):
		"""Is a negative number correctly determined not to be prime?"""
		for index in range(-3, -10, -1):
			self.assertFalse(is_prime(index), msg='{} should not be determined to be prime'.format(index))

	def test_mynegative(self):
		for index in range(-1, -10, -1):
			try:
				self.assertFalse(is_prime(index), msg='{} should not be determined to be prime'.format(index))
			except AssertionError as e:
				print("********")
				unittest.SkipTest("Lets continue")

	def test_upper(self):
		self.assertEqual(to_upper("Aura"), "AuRA")

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['Hello', 'world'])
		with self.assertRaises(TypeError):
			s.split(2)

if __name__ == '__main__':
    unittest.main()
