import unittest
import main

class TestMain(unittest.TestCase):
    """
    Info Main test class
    """
    
    def test_addition(self):
        result = main.add_numbers(5,1)
        self.assertEqual(result, 6)


    def test_subtraction(self):
        result = main.subtract_numbers(5,1)
        self.assertEqual(result, 4)

    def test_subtraction_fail(self):
        result = main.subtract_numbers(10, 12)
        self.assertNotEqual(result, 0)

    
    
if __name__ == "__main__":
    unittest.main()