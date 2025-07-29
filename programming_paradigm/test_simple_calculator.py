import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a new SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()