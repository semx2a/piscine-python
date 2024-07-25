import unittest
from load_csv import load

class TestLoad(unittest.TestCase):
	def test_load_wrong_path(self):
		pass

	def test_load_no_path(self):
		pass

	def test_load_right_path(self):
		load("../data/life_expctancy_years.csv")
