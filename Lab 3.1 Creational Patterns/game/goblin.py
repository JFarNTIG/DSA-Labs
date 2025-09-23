import random
from entity import Entity
from typing import Any

class Goblin(Entity):
    def __init__(self, name=None):
        if name is None:
            name = Goblin.get_random_name()
        super().__init__(name, 15, 15, 5)

    def decide(self) -> Any:
        if random.randint(1, 10) <= 3:
            # 3/10 random chance to defend
            return self.defend
        else:
            # otherwise attack
            return self.attack
        
    def get_type(self) -> str:
        return "Goblin"
        
    @staticmethod
    def get_random_name() -> str:
        GOBLIN_VOWELS = ["a", "e", "i", "u", "o"]
        GOBLIN_CONSONANTS = ["g", "n", "m", "r", "w", "v", "l", "p", "w"]
        letters = []
        for i in range(random.randint(4, 8)):
            if i % 2 == 0:
                letter = random.choice(GOBLIN_CONSONANTS)
            else:
                letter = random.choice(GOBLIN_VOWELS)

            if i == 0:
                letter = letter.upper()
            letters.append(letter)
        return "".join(letters)