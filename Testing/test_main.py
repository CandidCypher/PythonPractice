"""
Tests for the main module.
"""
import unittest
import main

class TestMain(unittest.TestCase):
    """
    Info Main test class
    """
    def test_addition(self):
        """
        Info: Test method for the add_numbers pass case. 
        """
        result = main.add_numbers(5,1)
        self.assertEqual(result, 6)
        self.assertIsInstance(result, int)


    def test_addition_string(self):
        """
        Info: Test that passes a string to verify that type checking is being performed. On called function
        """
        result = main.add_numbers(5, "string")
        self.assertIsInstance(result, TypeError)


    def test_subtraction(self):
        """
        Info: Test method for the subtraction function pass case. 
        """
        result = main.subtract_numbers(5,1)
        self.assertEqual(result, 4)

    def test_subtraction_fail(self):
        """
        Info: Subtraction test.
        """
        result = main.subtract_numbers(10, 12)
        self.assertNotEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
