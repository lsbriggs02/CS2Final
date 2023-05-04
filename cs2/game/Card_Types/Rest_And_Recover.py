from cs2.game.Cards import Card


class Rest_And_Recover(Card):

    def __init__(self):
        name = "Rest And Recover"
        type = "Skill"
        rarity = "Epic"
        energy = -1
        subject = "Player"
        heal = 5
        super().__init__(name, type, rarity, energy, subject, 0, 0, 0, 0, heal)
