my_tuple = (2,2,2,55, "string")
print(type(my_tuple))

my_tuple[3]
my_tuple[1]=5
my_tuple.count(2)
my_tuple.__contains__(1)

a,b,c, *others = my_tuple
others
a
