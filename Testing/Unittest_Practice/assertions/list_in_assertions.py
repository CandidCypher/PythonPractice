"""
Given a list of countries, write an assertion statement
to verify that a country code is within the list. 
"""

countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
try:
    assert "RUS" in countries, "Country not in lists"
    # AssertionErrors do not have   
except AssertionError as err:
    print(err)

