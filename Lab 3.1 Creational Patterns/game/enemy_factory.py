import random
from entity import Entity
from kobold import Kobold
from goblin import Goblin
from paladin import Paladin
from wizard import Wizard

ENEMIES_EASY = [
    Kobold, Goblin
]

ENEMIES_MEDIUM = [
    Paladin, Wizard
]

class EnemyFactory:
    def __init__(self, difficulty="easy"):
        """Create a new EnemyFactory which generates
        enemies.

        Parameters:
        -- 
            difficulty : either "easy" or "medium".
        """
        self.difficulty = difficulty

        if self.difficulty == "easy":
            self.enemy_types = ENEMIES_EASY
        elif self.difficulty == "medium":
            self.enemy_types = ENEMIES_MEDIUM
        else:
            raise ValueError(f"Invalid difficulty '{self.difficulty}'")

    def create_enemy(self) -> Entity:
        enemy_type = random.choice(self.enemy_types)
        return enemy_type()
