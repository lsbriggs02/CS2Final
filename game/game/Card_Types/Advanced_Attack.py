from random import randint

from cs2.game.Cards import Card


class Advanced_Attack(Card):

    def __init__(self):
        name = "Advanced Attack"
        type = "Attack"
        rarity = "Uncommon"
        energy = 1
        subject = "Enemy"
        damage = 9
        damage_diff = 3
        crit = 4
        super().__init__(name, type, rarity, energy, subject, damage, damage_diff, 0, 0, 0, 0, crit)
