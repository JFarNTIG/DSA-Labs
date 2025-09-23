import random
from entity import Entity
from typing import Any

class Wizard(Entity):
    def __init__(self, name=None):
        if name is None:
            name = Wizard.get_random_name()
        super().__init__(name, 30, 30, 20)

    def decide(self) -> Any:
        if self.turns % 5 == 0:
            # every 5th turn, the wizard defends.
            return self.defend
        else:
            # otherwise, the wizard attacks.
            return self.attack
        
    def get_type(self) -> str:
        return "Wizard"
        
    @staticmethod
    def get_random_name() -> str:
        NAMES = [
            "Elratrix",
            "Cropius",
            "Stradium",
            "Inzalius",
            "Olophyx",
            "Unydae",
            "Uxea",
            "Exeor", 
            "Onaphior"
        ]
        return random.choice(NAMES)