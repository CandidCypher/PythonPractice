my_dict = dict(this=10, that=100, the_other=500, banggers=[1,2,4,5])
my_dict.get('age',12.456789)
my_dict

my_dict["size"] =["32x32"]
print("32x32" in my_dict)

print(my_dict.items())
my_dict.clear()
another_dict = my_dict.copy()
my_dict.clear()
my_dict
another_dict
data = my_dict.pop("size")
my_dict
data