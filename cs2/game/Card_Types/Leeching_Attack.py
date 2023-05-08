from random import randint

from cs2.game.Cards import Card


class Leeching_Attack(Card):

    def __init__(self):
        name = "Leeching Attack"
        type = "Attack"
        rarity = "Rare"
        energy = 3
        subject = "Enemy"
        attack = 8
        attack_diff = 2
        crit = 5
        leech = True
        super().__init__(name, type, rarity, energy, subject, attack, attack_diff, 0, 0, 0, 0, crit, False, leech)
