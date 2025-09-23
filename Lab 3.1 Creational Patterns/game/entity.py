from typing import Any
from abc import ABC, abstractmethod
import random

class Entity(ABC):
    def __init__(self, name: str, max_health: int, health: int, strength: int):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.strength = strength
        self.defending = False
        self.turns = 0

    def take_damage(self, damage: int) -> bool:
        """Returns True if the entity died, otherwise False."""
        print(f"{self.name} takes {damage} points of damage!")
        adjusted = damage

        if self.defending:
            adjusted /= 2
            self.defending = False

        self.health = max(0, self.health - damage)

    def start_turn(self):
        print(f"\n-- {self.name}'s turn --")
        self.turns += 1

    def attack(self, other: "Entity"):
        damage = self.strength + random.randint(0, 3)
        print(f"{self.name} is attacking {other.name}!")
        other.take_damage(damage)

    def defend(self, other: "Entity"):
        print(f"{self.name} is defending against {other.name}!")
        self.defending = True

    def decide(self) -> Any:
        """By default, entities will always attack."""
        return self.attack
    
    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.get_type()}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Strength: {self.strength}")

    @abstractmethod
    def get_type(self) -> str:
        pass
    
    @staticmethod
    def get_random_name() -> str:
        return "Unknown"