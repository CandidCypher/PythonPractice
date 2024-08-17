
# More python method of opening files is the following. As the object
# falls out of scope, it closes the file.

with open("basic.txt", mode="r+") as my_file:
    # Mode 'r' or 'r+' reads file
    # The + adds ability to write as well however
    # cursor is at index 0
    print(my_file.readlines())

with open("basic.txt", mode="w") as write_file:
    # Mode 'w' treats the file as a 'new' file and
    # erases anything in the file with whatever is
    # written. 
    write_file.write("Some string")

with open("basic.txt") as read_file:
    print(read_file.readlines())


with open("basic.txt", mode='a') as append_file:
    #mode 'a' for append, writes at the end of the file
    append_file.write("\nend of file")


# # Script needs to be run from directory that script exists.
# my_file = open("basic.txt")

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(5)
# print(my_file.read())

# # file.read() reads whole file
# # file.readline() goes line by line
# my_file.seek(0)
# for idx, line in enumerate(my_file):
#     print(idx, line)

# my_file.seek(0)
# lines = my_file.readlines() #<- Returns list of lines
# print(lines[1])

## Explicitly close the file when done.
# my_file.close()