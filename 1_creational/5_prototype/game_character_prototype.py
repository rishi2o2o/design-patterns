import copy

class GameCharacter:
    def __init__(self, name, weapons, health):
        self.name = name
        self.weapons = weapons
        self.health = health
        # In a real app, this might involve heavy DB queries or file loading
        print(f"Initializing {self.name}...")

    def clone(self):
        # deepcopy ensures nested lists (like weapons) 
        # are copied and not just referenced.
        print(f"Cloning {self.name}...")
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.name} [Health: {self.health}, Weapons: {self.weapons}]"


if __name__ == "__main__":

    # Create the prototype (master copy)
    warrior_prototype = GameCharacter("Basic Warrior", ["Sword", "Shield"], 100)

    # Clone the prototype to make new characters instantly
    knight = warrior_prototype.clone()
    knight.name = "Knight"
    knight.health = 150 

    berserker = warrior_prototype.clone()
    berserker.name = "Berserker"
    berserker.weapons.append("Giant Axe") 

    print(warrior_prototype)
    print(knight)
    print(berserker)


