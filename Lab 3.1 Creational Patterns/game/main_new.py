"""This file has the code for the text-based combat simulator
*with* design patterns.
"""

from enemy_factory import EnemyFactory
from player import Player

enemy_generator = EnemyFactory("easy")

print("---------")
player = Player("John Protagonist", 50, 50, 12)
player.print_details()
print("---------")

print("\nfaces off against\n")

print("---------")
enemy = enemy_generator.create_enemy()
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