"""
Introduction to what decorators are

Decorators are the ability to wrap functions within other functions

"""


def hello():
    print(f"Hellooooo!!!")

print(f"Address of hello: {hello}")

greet = hello # <- shallow copy of a function
del hello
#print(f"Del address of hello: {hello}") <- The hello function is no longer defined

print(greet()) # <- You will notice that the address is the same as hello pre delete.