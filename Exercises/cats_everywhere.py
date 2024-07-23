#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats <- Typo? Is this to be 3 different cats?
cat1 = Cat("Fluffy", 5)
cat2 = Cat("Simon", 2)
cat3 = Cat("Albus", 4)

cats= [cat1, cat2, cat3]
# 2 Create a function that finds the oldest cat
def find_oldest_cat(cats:list)->Cat:
    oldest = None
    for cat in cats:
        if oldest == None:
            oldest = cat
        if cat.age > oldest.age:
            oldest = cat
    return oldest

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
elderlycat = find_oldest_cat(cats)
print(f"The oldest cat, {elderlycat.name}, is {elderlycat.age} years old")