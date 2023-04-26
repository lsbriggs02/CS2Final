from random import randint

from cs2.game.Cards import Card


class Basic_Attack(Card):

    def __init__(self):
        name = "Basic Attack"
        type = "Attack"
        rarity = "Common"
        energy = 1
        subject = "Enemy"
        damage = 6
        damage_diff = 1
        super().__init__(name, type, rarity, energy, subject, damage, damage_diff)
