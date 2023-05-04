from random import randint

from cs2.game.Cards import Card


class Heavy_Shield(Card):

    def __init__(self):
        name = "Heavy Shield"
        type = "Skill"
        rarity = "Uncommon"
        energy = 2
        subject = "Player"
        block = 17
        block_diff = 3
        super().__init__(name, type, rarity, energy, subject, 0, 0, block, block_diff)
