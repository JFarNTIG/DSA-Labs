"""This file has the code for the text-based combat simulator
*without* design patterns.
"""

from player import Player
from kobold import Kobold
from goblin import Goblin
from paladin import Paladin
from wizard import Wizard
import random

difficulty = "easy"

print("---------")
player = Player("John Protagonist", 50, 50, 12)
player.print_details()
print("---------")

print("\nfaces off against\n")

print("---------")
if difficulty == "easy":
    enemies = [
        Kobold, Goblin
    ]
    enemy_type = random.choice(enemies)
    enemy = enemy_type()
elif difficulty == "medium":
    enemies = [
        Paladin, Wizard
    ]
    enemy_type = random.choice(enemies)
    enemy = enemy_type()
else:
    raise ValueError(f"Invalid difficulty '{difficulty}'")
enemy.print_details()
print("---------")

while True:
    player.start_turn()
    player_action = player.decide()
    player_action(enemy)

    if enemy.health <= 0:
        print("Enemy died!")
        break

    enemy.start_turn()
    enemy_action = enemy.decide()
    enemy_action(player)

    if player.health <= 0:
        print("You died!")
        break