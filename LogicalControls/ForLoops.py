for element in (1,2,3,4,5):
    for x in ['a', 'b', 'c', 'd']:
        print(element, x)


users = {'name': 'Colem',
         'age': 10,
         'can_swim': False}

for item in users.items():
    print(item)