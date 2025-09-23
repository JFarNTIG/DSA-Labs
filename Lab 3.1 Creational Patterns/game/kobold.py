import random
from entity import Entity
from typing import Any

class Kobold(Entity):
    def __init__(self, name=None):
        if name is None:
            name = Kobold.get_random_name()
        super().__init__(name, 10, 10, 5)

    def get_type(self) -> str:
        return "Kobold"
        
    @staticmethod
    def get_random_name() -> str:
        GOBLIN_VOWELS = ["a", "e", "i", "u", "o"]
        GOBLIN_CONSONANTS = ["g", "z", "x", "n", "m", "r", "w"]
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