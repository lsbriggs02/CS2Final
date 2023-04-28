from random import randint


class Card:

    def __init__(self, n, t, r, e, s, d=0, dd=0, b=0, bb=0, h=0, hh=0, c=0, inst=0, l=False):
        self.name = n
        self.type = t
        self.rarity = r
        self.energy = e
        self.subject = s
        self.damage = d
        self.damage_diff = dd
        self.block = b
        self.block_diff = bb
        self.heal = h
        self.heal_diff = hh
        self.crit = c
        self.crit_true = False
        self.insta_kill = inst
        self.temp_damage = 0
        self.temp_block = 0
        self.temp_heal = 0
        self.leech = l
        self.is_not_used = True

    def act(self, charac, enem):
        if charac.energy - self.energy > -1 and self.is_not_used == True:
            self.is_not_used = False
            if self.heal > 0:
                self.temp_heal = randint(self.heal - self.heal_diff, self.heal + self.heal_diff)
            else:
                self.temp_heal = randint(0, self.heal + self.heal_diff)
            self.temp_damage = 0
            if self.damage > 0:
                self.temp_damage = randint(self.damage - self.damage_diff, self.damage + self.damage_diff)
            else:
                self.temp_damage = randint(0, self.damage + self.damage_diff)
            if self.leech:
                self.temp_heal = self.temp_damage * 0.5
            self.temp_block = 0
            if self.block_diff > 0:
                self.temp_block = randint(self.block - self.block_diff, self.block + self.block_diff)
            else:
                self.temp_block = randint(0, self.block + self.block_diff)
            charac.health += self.temp_heal
            charac.shield += self.block
            charac.energy -= self.energy
            if self.insta_kill > randint(0, 10):
                enem.shield -= enem.shield
                enem.health -= enem.health
            if self.crit > 0:
                if randint(0, 10) < self.crit:
                    self.crit_true = True
            if self.crit_true:
                if enem.shield == 0:
                    enem.health -= self.temp_damage * 2
                elif enem.shield < self.temp_damage * 2:
                    self.temp_damage -= enem.shield / 2
                    enem.shield -= enem.shield
                    enem.health -= self.temp_damage * 2
                else:
                    enem.shield -= self.temp_damage * 2
            else:
                if enem.shield == 0:
                    enem.health -= self.temp_damage
                elif enem.shield < self.temp_damage:
                    self.temp_damage -= enem.shield
                    enem.shield -= enem.shield
                    enem.health -= self.temp_damage
                else:
                    enem.shield -= self.temp_damage

    def __str__(self):
        a = str(self.name) + "\nType: " + str(self.type) + "\nRarity: "  + str(self.rarity) + "\nEnergy: " + str(self.energy)
        if self.damage != 0:
            a += "\nDamage: " + str(self.damage)
            if self.damage_diff != 0:
                a += " [±" + str(self.damage_diff) + " range]"
        else:
            if self.damage_diff != 0:
                a += "\nDamage: 0[+" + str(self.damage_diff) + " range]"
        if self.block != 0:
            a += "\nBlock: " + str(self.block)
            if self.block_diff != 0:
                a += " [±" + str(self.block_diff) + " range]"
        else:
            if self.block_diff != 0:
                a += "\nBlock: 0[+" + str(self.block_diff) + " range]"
        if self.heal != 0:
            a += "\nHeal: " + str(self.heal)
            if self.heal_diff != 0:
                a += " [±" + str(self.heal_diff) + " range]"
        else:
            if self.heal_diff != 0:
                a += "\nHeal: 0[+" + str(self.heal_diff) + " range]"
        if self.crit != 0:
            a += "\nCrit Chance: " + str(self.crit) + "0%"
        if self.insta_kill < 0:
            a += "\nInsta-Kill Chance: " + str(self.insta_kill) + "0%"
        if self.leech:
            a += "\nLife steal: 50%"
        return a


card = Card(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(card)
