
# Script needs to be run from directory that script exists.
my_file = open("basic.txt")

print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(5)
print(my_file.read())

# file.read() reads whole file
# file.readline() goes line by line
my_file.seek(0)
for idx, line in enumerate(my_file):
    print(idx, line)

my_file.seek(0)
lines = my_file.readlines()
print(lines[1])

my_file.close()