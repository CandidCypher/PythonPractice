#! /usr/bin/env python3

#1. Wrap the above (reformatted to be below as comments below code is bad practice) code in a function called checkDriverAge(). 
# Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.


def checkDriverAge_1():
	"""
	Info: Blocking method that requests driver age
	"""
	age = input("What is your age: ")
	if int(age) < 18:
		print(f"I'm sorry but {age} is too young to drive. Powering off")
	else:
		print(f"Powering on. Enjoy the ride!")
		

def checkDriverAge_2(age:int)->bool:
	"""
	Info: Non bloocking immplementation that checks driver age
	Input:(int) age - driver's age in years
	Output:(bool) driver's age approved.
	"""
	if age < 18:
		print(f"I'm sorry but {age} yrs old is too young to drive. Powering Off")
		return False
	else:
		print("Powering on. Enjoy the ride!")
		return True

if __name__ == "__main__":
	checkDriverAge_1()
	powerOn = False
	while not powerOn:
		age = int(input("Driver, what is your age?: "))
		powerOn = checkDriverAge_2(age)