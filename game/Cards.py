from random import randint


class Card:

    def __init__(self, n, t, r, e, s, d=0, dd=0, b=0, bb=0, h=0, hh=0, c=0, inst=False, l=False):
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
            if self.heal_diff > 0:
                self.temp_heal = randint(self.heal - self.heal_diff, self.heal + self.heal_diff)
            else:
                self.temp_heal = self.heal
            self.temp_damage = 0
            self.temp_damage = randint(self.damage - self.damage_diff, self.damage + self.damage_diff)
            if self.leech:
                self.temp_heal = self.temp_damage
            self.temp_block = 0
            self.temp_block = randint(self.block - self.block_diff, self.block + self.block_diff)
            charac.health += self.temp_heal
            charac.shield += self.block
            charac.energy -= self.energy
            if self.insta_kill:
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
