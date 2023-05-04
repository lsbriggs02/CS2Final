from cs2.game.Cards import Card


class Basic_Shield(Card):

    def __init__(self):
        name = "Basic Shield"
        type = "Skill"
        rarity = "Common"
        energy = 1
        subject = "Player"
        block = 6
        block_diff = 1
        super().__init__(name, type, rarity, energy, subject, 0, 0, block, block_diff)
