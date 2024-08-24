import unittest
import main

class TestMain(unittest.TestCase):
    """
    Info Main test class
    """
    
    def test_addition(self):
        result = main.add_numbers(5,1)
        self.assertEqual(result, 6)

    def test_addition_string(self):
        """
        Info: Test that passes a string to get a tpe error.
        """
        result = main.add_numbers(5, "string")
        print(result)
        self.assertIsInstance(result, TypeError)


    def test_subtraction(self):
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