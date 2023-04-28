class Enemy:

    def __init__(self, round, boss=False, fboss=False):
        self.isboss = boss
        self.shield = 0
        self.health = 15 + round * 2
        if boss:
            self.health = 45 + round * 5
        self.shield_add = 5 + (round / 2)
        if boss:
            self.shield_add = 10 + round
        self.attack = 3 + round
        if boss:
            self.attack = 13 + round
        self.heal = 3 + (round / 4)
        if boss:
            self.heal = 5 + (round / 2)
        if boss:
            self.summon = round / 2

    def act(self, play, attack_num):
        if attack_num >= 3:
            if attack_num == 4 and self.isboss:
                New_Enem = Enemy(self.summon)
            elif play.shield == 0:
                play.health -= self.attack
            elif play.shield < self.attack:
                self.attack -= play.shield
                play.shield -= play.self.attack
            else:
                play.shield -= self.attack
        elif attack_num == 2:
            self.shield += self.shield_add
        elif attack_num >= 1:
            self.health += self.heal
