from random import randint

from cs2.game.Cards import Card


class Basic_Heal(Card):

    def __init__(self):
        name = "Basic Heal"
        type = "Skill"
        rarity = "Common"
        energy = 1
        subject = "Player"
        heal = 3
        super().__init__(name, type, rarity, energy, subject, 0, 0, 0, 0, heal)
