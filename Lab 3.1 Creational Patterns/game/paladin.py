import random
from entity import Entity
from typing import Any

class Paladin(Entity):
    def __init__(self, name=None):
        if name is None:
            name = Paladin.get_random_name()
        super().__init__(name, 50, 50, 20)

    def decide(self) -> Any:
        if self.turns % 2 == 0:
            # every other turn, the paladin attacks.
            return self.attack
        else:
            # otherwise, the paladin defends.
            return self.defend
        
    def get_type(self) -> str:
        return "Paladin"
        
    @staticmethod
    def get_random_name() -> str:
        NAMES = [
            "Jebediah",
            "Ezekiel",
            "Celeste",
            "Noah",
            "Hope",
            "Seraphina",
            "Gunther",
            "Samuel", 
            "Raynard"
        ]
        return random.choice(NAMES)