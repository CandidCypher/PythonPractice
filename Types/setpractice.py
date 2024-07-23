a_set = {1,2,3,99,10,10, 100, 33}
type(a_set)
a_set

my_set = {}
your_set =  {}

def update_sets():
    global my_set
    global your_set
    my_set = { 1,2,3,4,5}
    your_set = {4,5,6,7,8,9,10}
    return


update_sets()
my_set
my_set.difference(your_set) 

my_set.discard(5)
print(my_set)

my_set.difference_update(your_set)
type(my_set)

flag = False
second_flag = False

if flag:
    print("flag is set to true")
elif not second_flag:
    print("not second flag")
else:
    print("The world is ending...")
 