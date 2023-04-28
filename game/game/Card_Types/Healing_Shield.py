from random import randint

from cs2.game.Cards import Card


class Healing_Shield(Card):

    def __init__(self):
        name = "Healing Shield"
        type = "Skill"
        rarity = "Rare"
        energy = 1
        subject = "Player"
        heal = 4
        heal_diff = 2
        block = 10
        super().__init__(name, type, rarity, energy, subject, 0, 0, block, 0, heal, heal_diff)
