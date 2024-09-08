"""
Module Docstring Here
"""

def test_widget_functions_as_expected() -> None:
    """
    Info: Test function to be found by pytest.
    """
    assert True

def test_widget_functions_fails() -> AssertionError:
    """
    Info: Failure test function to be found by pytest.
    """
    assert False

def some_convenience_function() -> None:
    """
    Info: Non test function
    """
    print("I am doin' stuff ma!")