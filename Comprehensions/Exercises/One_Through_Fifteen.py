#! /usr/evn/bin python


"""
Exercises 1 - 15 to warm up to list comprehension practices. 

"""


#1 Write a basic list comprehension that has numbers in the range 1-1000
exr_one = [x for x in range(1000)]


#2 Write a basic list comprehension that has the multiples of 5 in the range of 1-1000
exr_two = [x for x in range(1000) if x%5 == 0]


#3 Write a basic list comprehension that has the same as above but multiplies each multiple by 3.14159265
exr_three = [x*3.14159265 for x in range(1000) if x%5==0]


#4 Create a list comprehension that combines the following two list to create a list of tuples
names = ["Fred", "Allison", "Rebecca", "Samuel", "Dave", "Brent"]
scores = [85, 93, 82, 97, 78, 89]
exr_four = [(name, score) for name,score in zip(names, scores)]


#5, Create a dictionary comprehension that turns the following into a dictionary
names = ["Fred", "Allison", "Rebecca", "Samuel", "Dave", "Brent"]
heights = ["6'1", "5'8", "5'5", "6'3", "5'10", "5'11"]
exr_five = {key:value for key,value in zip(names, heights)}


#6 Create the same dictionary as above but also include the sex, age, and location of each person
# hint {"fred":{location:Phoenix,sex:male,age:29}
locations = ["Phoenix", "Seatle", "Austin", "Dallas", "San Diego", "Palm Beach"]
sex = ["Male", "Female", "Female", "Male", "Male", "Male"]
#First zip all the data together
exr_six = {k:{"height":a, "location":b, "sex":c} for k,a,b,c in zip(names, heights, locations, sex)}

#7 Create a mapping of numeric values to a color scale. First create a random list of numbers using
# a list comprehension. Then map those values to a RGB value
from random import randint
random_values = [randint(0,100) for x in range(1000)]

from matplotlib import cm, colors

def map_value(value:int)->tuple:
    norm = colors.Normalize(vmin=min(random_values), vmax=max(random_values), clip=True)
    mapper = cm.ScalarMappable(norm=norm, cmap=cm.Greys_r)
    return (mapper.to_rgba(value)[0], mapper.to_rgba(value)[1], mapper.to_rgba(value)[2])
            
color_list = list(map(map_value, random_values))
color_values = [(value, color) for value, color in zip(random_values, color_list)]