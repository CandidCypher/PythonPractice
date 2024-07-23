str1 = "Cameron Owens"
print(str1.split(" "))
my_list = ["This", "That", "another"]
str2 = "|"
str2.join(my_list)

str2 = ""
str3 = ""
for x in str1:
    # Reverses due to order of operations
    str2 = x + str2
    str3 = str3 + x
print(str2)
print(str3)

my_list = [1,2,3,4,5]
reversed_list = my_list[-1::-1]
print(reversed_list)


lst1 = ['W', 'a', 'w', 'b']
lst2 = ['e', ' ', 'riting', 'log']

lst3 = [x+y for x,y in zip(lst1, lst2)]
lst3

print(zip(lst1, lst2))

