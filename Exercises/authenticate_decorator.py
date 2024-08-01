# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    """
    Info: Generic wrapper template
    """

    def wrap_func(*args, **kwargs):
        if args[0]['valid']:
            print("User is authenticated")
            return fn(*args, **kwargs)
        else:
            return print("User is not authenticated")
    return wrap_func

    
  # code here

@authenticated # <- Decorator is called first before getting to the function
def message_friends(user:dict):
    """
    Info: Messaging function that sends messages.

    Input(dict): Dictonary object of {'name':str, 'valid':bool}

    """
    print(f"{user['name']}, your message has been sent")


if __name__ == "__main__":
    # Reminder: Order of operations is to hit the decorator with the
    # argument of the funciton (decorator(fucntion(*args, **kwargs)))
    message_friends(user1)
