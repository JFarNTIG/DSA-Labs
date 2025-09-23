from entity import Entity
from typing import Any

class Player(Entity):
    def decide(self) -> Any:
        choice = input("What would you like to do? (a=attack, d=defend) ")

        if choice == "a":
            return self.attack
        elif choice == "d":
            return self.defend
        
    def get_type(self) -> str:
        return "Player"