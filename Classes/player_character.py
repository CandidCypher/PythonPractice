
'''player_character module:

Classes:
PlayerCharacterData: Dataclass for cleaning up the PlayerCharacter initialization method
PlayerCharacter: Game Character'''


from dataclasses import dataclass
from enum import Enum

class WizzardTypes(Enum):
    """
    Info: Wizzard Types
    """
    BLACK = 1
    WHITE = 2
    RED = 3
    BLUE=4

@dataclass
class PlayerCharacterData:
    """
    Info: Player character dataclass for initializing a character
    """
    name:str
    age:int
    hit_points:int
    attack_strength:int
    defense_skill:int

@dataclass
class WizzardCharacterData(PlayerCharacterData):
    """
    Info: Wizzard character dataclass
    """
    magic_type = WizzardTypes.WHITE
    magic_points = 100
    cooldown_time = 10


@dataclass
class ArcherCharacterData(PlayerCharacterData):
    """
    Info: Archer character dataclass
    """
    bow_type:str="LongBow"
    arrows:int=100


class PlayerCharacter():
    """
    Info: Player character class

    Attributes
    --------------
    name: str
        Name of the character (single name)
    age: int
        Age of the character
    attack_strength: int
        Attack power of the character

    Methods
    ---------------

    """

    def __init__(self, name:str, age:int, hit_points=100, attack_strength=10, defense_skill=5):
        self.name = name
        self.age = age
        self.attack_strength = attack_strength
        self.hit_points = hit_points
        self.defense_skill = defense_skill

    def shout(self):
        """
        Info: Shout method to declare the character's name
        """
        print(f"I AM {self.name}!!")


    def attack(self, enemy):
        """
        Info: Attack method reduces the hit_points of a declared enemy
        """
        enemy.hit_points -= self.attack_strength


    def defend(self, enemy):
        """
        Info: Defense method to reduce the attack strength of an enemey
        """
        self.hit_points -= (100-self.defense_skill)/100 * enemy.attack_strength


    def run(self):
        """
        Info: Run away method
        """
        print("Running away!")


class Wizzard(PlayerCharacter):
    """
    Info: Extension of the player class
    """
    def __init__(self, name, age, magic_type=WizzardTypes.BLACK, magic_points=100, cooldown_time=10):
        super().__init__(name, age)
        self.magic_class = magic_type
        self.cooldown_time = cooldown_time
        self.magic_points = magic_points


    def attack(self, enemy:PlayerCharacter):
        super().attack(enemy=enemy)
        print("My power is diminishing!")
        self.magic_points -= 10


class Archer(PlayerCharacter):
    """
    Info: Archer class
    """
    def __init__(self, name, age, bow_type="LongBow"):
        super().__init__(name, age)
        self.bow_type = bow_type
        self.arrows = 100
    
    def attack(self, enemy):
        """
        Archer class. 
        """
        super().attack(enemy=enemy)
        print("I have used 1 arrow")
        self.arrows -= 1
