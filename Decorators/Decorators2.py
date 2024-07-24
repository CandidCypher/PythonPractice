"""
Continuation of the topic of decorators
"""

def hello(func):
    func()

def greet():
    print("Hello, I'm still here")

a = hello(greet)

print(a)