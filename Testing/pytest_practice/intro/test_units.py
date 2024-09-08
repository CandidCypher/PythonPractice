import unittest

class TestsExample(unittest.TestCase):
    """
    Info: Test Class
    """

    def test_addition(self)->AssertionError:
        """
        Info: test method example
        """
        self.assertTrue(True)

    
    def test_two(self)->None:
        """
        Info: Test method example 2
        """
        self.assertFalse(False)



if __name__ == "__main__":
    unittest.main()