from cs2.game.Cards import Card


class Unstable_Potions(Card):

    def __init__(self):
        name = "Unstable Potions"
        type = "Skill"
        rarity = "Epic"
        energy = -3
        subject = "Player"
        heal = -10
        super().__init__(name, type, rarity, energy, subject, 0, 0, 0, 0, heal)
