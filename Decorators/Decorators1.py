"""
Introduction to what decorators are

Decorators are the ability to wrap functions within other functions

"""


def hello():
    """
    Declaration of a simple function.
    Because functions are objects they have addresses
    in memory. When they are executed, their memory address
    is accessed. 
    """
    print(f"Hellooooo!!!")

print(f"Address of hello: {hello}")

greet = hello # <- Greet points to the memory of hello
del hello # <- removes the binding of the keyword 'hello' to the memorry address.

#print(f"Del address of hello: {hello}") <- The hello function is no longer defined

print(greet()) # <- You will notice that the address is the same as hello pre delete.