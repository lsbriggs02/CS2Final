import pygame
import random
from random import randint
from new_tree_dict import CS2TreeDict

from cs2.game.Card_Types.Advanced_Attack import Advanced_Attack
from cs2.game.Card_Types.Basic_Attack import Basic_Attack
from cs2.game.Card_Types.Basic_Heal import Basic_Heal
from cs2.game.Card_Types.Basic_Shield import Basic_Shield
from cs2.game.characters.Enemy import Enemy
from cs2.game.Card_Types.Healing_Shield import Healing_Shield
from cs2.game.Card_Types.Heavy_Shield import Heavy_Shield
from cs2.game.Card_Types.Leeching_Attack import Leeching_Attack
from cs2.game.Card_Types.Rest_And_Recover import Rest_And_Recover
from cs2.game.Card_Types.Unstable_Potions import Unstable_Potions


class _Button:
    def __init__(self, rect, label):
        self.rect = rect
        self.hover = False
        self.label = label


# Setting up and init variables
class Enviro:
    def __init__(self, play):
        pygame.init()
        self.player = play
        self.exD = 0
        self.exS = 0
        self.exH = 0
        self.exE = 0
        self.enemy_move = 0
        self.enemove = ""
        self.curdeck = [Basic_Attack(), Basic_Attack(), Basic_Attack(), Basic_Attack(), Basic_Shield(), Basic_Shield(),
                        Basic_Shield(), Basic_Shield(), Basic_Heal(), Basic_Heal()]
        self.gendeck = [Basic_Attack(), Basic_Attack(), Basic_Attack(), Basic_Attack(), Basic_Attack(), Basic_Attack(),
                        Basic_Attack(), Basic_Attack(), Basic_Heal(), Basic_Heal(), Basic_Heal(), Basic_Heal(),
                        Basic_Heal(),
                        Basic_Heal(), Basic_Heal(), Basic_Heal(), Basic_Shield(), Basic_Shield(), Basic_Shield(),
                        Basic_Shield(), Basic_Shield(), Basic_Shield(), Basic_Shield(), Basic_Shield(),
                        Advanced_Attack(),
                        Advanced_Attack(), Advanced_Attack(), Advanced_Attack(), Advanced_Attack(), Advanced_Attack(),
                        Heavy_Shield(), Heavy_Shield(), Heavy_Shield(), Heavy_Shield(), Heavy_Shield(), Heavy_Shield(),
                        Healing_Shield(), Healing_Shield(), Healing_Shield(), Healing_Shield(), Leeching_Attack(),
                        Leeching_Attack(), Leeching_Attack(), Leeching_Attack(), Rest_And_Recover(), Rest_And_Recover(),
                        Unstable_Potions(), Unstable_Potions()]
        self.world = CS2TreeDict()
        self.hand = []
        self.add_cards = []
        self.encounter_deck = self.curdeck[:]
        self.enemy_list = []
        self.discard_deck = []
        self.screen = None
        self.card_num1 = None
        self.card_num2 = None
        self.card_num3 = None
        self.card_num4 = None
        self.card_num5 = None
        self.next_butt = None
        self.pcard_1 = None
        self.pcard_2 = None
        self.pcard_3 = None
        self.pcard_4 = None
        self.roundCount = None
        self.choosing = False
        self.boss_Lvl = False
        self.backs = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
        self.round = 1

    @staticmethod
    def render_button(screen, button, color, backcolor=(255, 255, 255)):
        text = pygame.font.SysFont('Ariel', 30)
        pygame.draw.rect(screen, backcolor, button.rect, 0, 4)
        pygame.draw.rect(screen, (0, 0, 0), button.rect, 1, 4)
        Enviro.box_text(screen, text, button.rect[0], button.rect[0] + button.rect[2], button.rect[1], button.label,
                        color)
        pygame.display.update()

    @staticmethod
    def box_text(surface, font, x_start, x_end, y_start, text, colour):
        x = x_start + 10
        y = y_start + 5
        words = text.split('\n')

        for word in words:
            word_t = font.render(word, True, colour)
            if word_t.get_width() + x <= x_end:
                surface.blit(word_t, (x, y))
                x += word_t.get_width() * 1.1
            else:
                y += word_t.get_height() * 1.1
                x = x_start + 10
                surface.blit(word_t, (x, y))
                x += word_t.get_width() * 1.1

    @staticmethod
    def inside(point, rect):
        return rect[0] <= point[0] <= rect[0] + rect[2] and rect[1] <= point[1] <= rect[1] + rect[3]

    # Handles what happens when user presses next button
    def next(self):
        self.screen.fill((255, 255, 255))
        _ = 0
        # Reset acting deck with current deck
        if len(self.encounter_deck) <= 5:
            self.encounter_deck = self.curdeck[:]
        # Fill up add cards while removing from encounter deck
        while _ < 5:
            rand_card_num = randint(0, (len(self.encounter_deck) - 1))
            self.add_cards.append(self.encounter_deck[rand_card_num])
            self.encounter_deck.remove(self.encounter_deck[rand_card_num])
            _ += 1
        # Reset hand with the new cards
        self.hand = self.add_cards[:]
        # Reset add cards to none
        self.add_cards = []
        # Enemy makes a move
        self.enemy_list[0].act(self.player, self.enemy_move)
        self.enemy_move = random.randint(0, 5)
        self.enemove = ""
        if self.enemy_move == 1:
            self.enemove = "Heal"
        if self.enemy_move == 2:
            self.enemove = "Shield"
        if self.enemy_move >= 3:
            self.enemove = "Attack"
        em = _Button((550, 180, 250, 30), "Next move: " + str(self.enemove))
        Enviro.render_button(self.screen, em, (0, 0, 0))
        self.roundCount = _Button((300, 20, 140, 30), "Round: " + str(self.round))
        Enviro.render_button(self.screen, self.roundCount, (0, 0, 0))
        # Reset play stats and update screen
        self.player.energy = 3 + self.exE
        self.player.shield = 0
        self.player_stats(self.player, self.enemy_list[0], self.screen)
        # Reset names with new cards
        _ = 0
        while _ < 5:
            if self.hand[_].rarity == "Common":
                self.backs[_] = (201, 201, 201)
            elif self.hand[_].rarity == "Uncommon":
                self.backs[_] = (64, 194, 70)
            elif self.hand[_].rarity == "Rare":
                self.backs[_] = (33, 96, 163)
            elif self.hand[_].rarity == "Epic":
                self.backs[_] = (143, 43, 214)
            _ += 1

        self.card_num1 = _Button((000, 450, 13 * len(self.hand[0].name + "-" + str(self.hand[0].energy)), 30),
                                 self.hand[0].name + "-(" + str(self.hand[0].energy) + ")")
        self.card_num2 = _Button((140, 550, 13 * len(self.hand[1].name + "-" + str(self.hand[1].energy)), 30),
                                 self.hand[1].name + "-(" + str(self.hand[1].energy) + ")")
        self.card_num3 = _Button((280, 450, 13 * len(self.hand[2].name + "-" + str(self.hand[2].energy)), 30),
                                 self.hand[2].name + "-(" + str(self.hand[2].energy) + ")")
        self.card_num4 = _Button((420, 550, 13 * len(self.hand[3].name + "-" + str(self.hand[3].energy)), 30),
                                 self.hand[3].name + "-(" + str(self.hand[3].energy) + ")")
        self.card_num5 = _Button((560, 450, 13 * len(self.hand[4].name + "-" + str(self.hand[4].energy)), 30),
                                 self.hand[4].name + "-(" + str(self.hand[4].energy) + ")")
        self.next_butt = _Button((710, 550, 80, 30), 'Next')
        # Reset buttons to render with the new names
        Enviro.render_button(self.screen, self.card_num1, (0, 0, 0), self.backs[0])
        Enviro.render_button(self.screen, self.card_num2, (0, 0, 0), self.backs[1])
        Enviro.render_button(self.screen, self.card_num3, (0, 0, 0), self.backs[2])
        Enviro.render_button(self.screen, self.card_num4, (0, 0, 0), self.backs[3])
        Enviro.render_button(self.screen, self.card_num5, (0, 0, 0), self.backs[4])
        Enviro.render_button(self.screen, self.next_butt, (0, 0, 0))

        self.hand[0].is_not_used = True
        self.hand[1].is_not_used = True
        self.hand[2].is_not_used = True
        self.hand[3].is_not_used = True
        self.hand[4].is_not_used = True

    @staticmethod
    def player_stats(play, enem, screen):
        h = _Button((0, 225, 140, 30), "Health: " + str(play.health))
        e = _Button((0, 175, 140, 30), "Energy: " + str(play.energy))
        s = _Button((0, 275, 140, 30), "Shield: " + str(play.shield))
        eh = _Button((550, 225, 250, 30), "Enemy Health: " + str(enem.health))
        es = _Button((550, 275, 250, 30), "Enemy Shield: " + str(enem.shield))

        Enviro.render_button(screen, h, (0, 0, 0))
        Enviro.render_button(screen, e, (0, 0, 0))
        Enviro.render_button(screen, s, (0, 0, 0))
        Enviro.render_button(screen, eh, (0, 0, 0))
        Enviro.render_button(screen, es, (0, 0, 0))

    # What happens when all enemies die and new cards are chosen between levels
    def choose_cards(self):
        self.screen.fill((255, 255, 255))
        self.choosing = True

        self.card_num1 = _Button((0, 0, 0, 0), '')
        self.card_num2 = _Button((0, 0, 0, 0), '')
        self.card_num3 = _Button((0, 0, 0, 0), '')
        self.card_num4 = _Button((0, 0, 0, 0), '')
        self.card_num5 = _Button((0, 0, 0, 0), '')
        self.next_butt = _Button((0, 0, 0, 0), '')
        if not self.boss_Lvl:
            # increase rarity of potential card picks
            if self.round < len(self.gendeck) - 10:
                bob = self.round
            else:
                bob = len(self.gendeck) - 10
            if bob - 10 < 0:
                star = 0
            else:
                star = 10
            for _ in range(4):
                self.add_cards.append(self.gendeck[randint(bob - star, len(self.gendeck) - 10)])

            _ = 0
            while _ < 4:
                if self.add_cards[_].rarity == "Common":
                    self.backs[_] = (201, 201, 201)
                elif self.add_cards[_].rarity == "Uncommon":
                    self.backs[_] = (64, 194, 70)
                elif self.add_cards[_].rarity == "Rare":
                    self.backs[_] = (33, 96, 163)
                elif self.add_cards[_].rarity == "Epic":
                    self.backs[_] = (143, 43, 214)
                _ += 1

            self.pcard_1 = _Button((50, 50, 225, 200), str(self.add_cards[0]))
            self.pcard_2 = _Button((50, 300, 225, 200), str(self.add_cards[1]))
            self.pcard_3 = _Button((475, 50, 225, 200), str(self.add_cards[2]))
            self.pcard_4 = _Button((475, 300, 225, 200), str(self.add_cards[3]))

            Enviro.render_button(self.screen, self.pcard_1, (0, 0, 0), self.backs[0])
            Enviro.render_button(self.screen, self.pcard_2, (0, 0, 0), self.backs[1])
            Enviro.render_button(self.screen, self.pcard_3, (0, 0, 0), self.backs[2])
            Enviro.render_button(self.screen, self.pcard_4, (0, 0, 0), self.backs[3])
        else:
            self.pcard_1 = _Button((50, 50, 225, 200), "+1 Extra Damage\n'A little extra muscle never\n hurt anything "
                                                       "but your enemies'")
            self.pcard_2 = _Button((50, 300, 225, 200), "+1 Extra Shielding\n'One step closer to becoming\n a truly "
                                                        "immortal hero'")
            self.pcard_3 = _Button((475, 50, 225, 200), "+1 Extra Healing\n'The light beckons to you, \n a tiny bit "
                                                        "more warmth to help you,\n in these dark, cold times'")
            self.pcard_4 = _Button((475, 300, 225, 200), "+1 Extra Energy\n'Some stamina to help you try, \n No "
                                                         "longer will you have to be sly,\n For as you slay, "
                                                         "without needing to lie,\n Time will speed on by'")

            Enviro.render_button(self.screen, self.pcard_1, (0, 0, 0), self.backs[0])
            Enviro.render_button(self.screen, self.pcard_2, (0, 0, 0), self.backs[1])
            Enviro.render_button(self.screen, self.pcard_3, (0, 0, 0), self.backs[2])
            Enviro.render_button(self.screen, self.pcard_4, (0, 0, 0), self.backs[3])
        Enviro.render_button(self.screen, self.card_num1, (0, 0, 0))
        Enviro.render_button(self.screen, self.card_num2, (0, 0, 0))
        Enviro.render_button(self.screen, self.card_num3, (0, 0, 0))
        Enviro.render_button(self.screen, self.card_num4, (0, 0, 0))
        Enviro.render_button(self.screen, self.card_num5, (0, 0, 0))
        Enviro.render_button(self.screen, self.next_butt, (0, 0, 0))

    def spawn_level(self, roundnum):
        self.screen.fill((255, 255, 255))
        self.roundCount = _Button((300, 20, 140, 30), "Round: " + str(self.round))
        Enviro.render_button(self.screen, self.roundCount, (0, 0, 0))
        # Set up encounter deck(for easy mutation of cards)
        self.encounter_deck = self.curdeck[:]
        self.enemy_list = []
        roundrn = int(roundnum)
        if roundrn % 5 != 0:
            while roundrn > 0:
                self.enemy_list.append(Enemy(roundnum))
                roundrn -= 1
                self.boss_Lvl = False
        else:
            while roundrn > 0:
                self.enemy_list.append(Enemy(roundnum, True))
                roundrn -= 5
                self.boss_Lvl = True

        # Create discard deck
        self.discard_deck = []
        # Create list for cards to choose from to add to curdeck
        self.add_cards = []

        _ = 0
        while _ < 5:
            rand_card_num = random.randint(0, (len(self.encounter_deck) - 1))
            self.add_cards.append(self.encounter_deck[rand_card_num])
            self.encounter_deck.remove(self.encounter_deck[rand_card_num])
            _ += 1
        self.hand = self.add_cards[:]
        self.player.energy = 3
        self.player.shield = 0

        _ = 0
        while _ < 5:
            if self.hand[_].rarity == "Common":
                self.backs[_] = (201, 201, 201)
            elif self.hand[_].rarity == "Uncommon":
                self.backs[_] = (64, 194, 70)
            elif self.hand[_].rarity == "Rare":
                self.backs[_] = (33, 96, 163)
            elif self.hand[_].rarity == "Epic":
                self.backs[_] = (143, 43, 214)
            _ += 1

        # define buttons
        self.card_num1 = _Button((000, 450, 13 * len(self.hand[0].name + "-" + str(self.hand[0].energy)), 30),
                                 self.hand[0].name + "-(" + str(self.hand[0].energy) + ")")
        self.card_num2 = _Button((140, 550, 13 * len(self.hand[1].name + "-" + str(self.hand[1].energy)), 30),
                                 self.hand[1].name + "-(" + str(self.hand[1].energy) + ")")
        self.card_num3 = _Button((280, 450, 13 * len(self.hand[2].name + "-" + str(self.hand[2].energy)), 30),
                                 self.hand[2].name + "-(" + str(self.hand[2].energy) + ")")
        self.card_num4 = _Button((420, 550, 13 * len(self.hand[3].name + "-" + str(self.hand[3].energy)), 30),
                                 self.hand[3].name + "-(" + str(self.hand[3].energy) + ")")
        self.card_num5 = _Button((560, 450, 13 * len(self.hand[4].name + "-" + str(self.hand[4].energy)), 30),
                                 self.hand[4].name + "-(" + str(self.hand[4].energy) + ")")
        self.next_butt = _Button((710, 550, 80, 30), 'Next')

        self.pcard_1 = _Button((0, 0, 0, 0), '')
        self.pcard_2 = _Button((0, 0, 0, 0), '')
        self.pcard_3 = _Button((0, 0, 0, 0), '')
        self.pcard_4 = _Button((0, 0, 0, 0), '')

        # add buttons
        Enviro.render_button(self.screen, self.card_num1, (0, 0, 0), self.backs[0])
        Enviro.render_button(self.screen, self.card_num2, (0, 0, 0), self.backs[1])
        Enviro.render_button(self.screen, self.card_num3, (0, 0, 0), self.backs[2])
        Enviro.render_button(self.screen, self.card_num4, (0, 0, 0), self.backs[3])
        Enviro.render_button(self.screen, self.card_num5, (0, 0, 0), self.backs[4])
        Enviro.render_button(self.screen, self.next_butt, (0, 0, 0))

        Enviro.render_button(self.screen, self.pcard_1, (0, 0, 0))
        Enviro.render_button(self.screen, self.pcard_2, (0, 0, 0))
        Enviro.render_button(self.screen, self.pcard_3, (0, 0, 0))
        Enviro.render_button(self.screen, self.pcard_4, (0, 0, 0))

        self.player_stats(self.player, self.enemy_list[0], self.screen)

        self.hand[0].is_not_used = True
        self.hand[1].is_not_used = True
        self.hand[2].is_not_used = True
        self.hand[3].is_not_used = True
        self.hand[4].is_not_used = True

    def show(self):
        # calculate some convenient variables

        running = True

        # Setting up decks
        # Starter deck
        self.curdeck = [Basic_Attack(), Basic_Attack(), Basic_Attack(), Basic_Attack(), Basic_Shield(), Basic_Shield(),
                        Basic_Shield(), Basic_Shield(), Basic_Heal(), Basic_Heal()]
        # Deck of cards to be pulled for choices
        self.gendeck = [Basic_Attack(), Basic_Attack(), Basic_Attack(), Basic_Attack(), Basic_Attack(), Basic_Attack(),
                        Basic_Attack(), Basic_Attack(), Basic_Heal(), Basic_Heal(), Basic_Heal(), Basic_Heal(),
                        Basic_Heal(), Basic_Heal(), Basic_Heal(), Basic_Heal(), Basic_Shield(), Basic_Shield(),
                        Basic_Shield(), Basic_Shield(), Basic_Shield(), Basic_Shield(), Basic_Shield(), Basic_Shield(),
                        Advanced_Attack(), Advanced_Attack(), Advanced_Attack(), Advanced_Attack(), Advanced_Attack(),
                        Advanced_Attack(), Heavy_Shield(), Heavy_Shield(), Heavy_Shield(), Heavy_Shield(),
                        Heavy_Shield(), Heavy_Shield(), Healing_Shield(), Healing_Shield(), Healing_Shield(),
                        Healing_Shield(), Leeching_Attack(), Leeching_Attack(), Leeching_Attack(), Leeching_Attack(),
                        Rest_And_Recover(), Rest_And_Recover(), Unstable_Potions(), Unstable_Potions()]

        # set up initial display
        screen2 = pygame.display.set_mode((800, 600))
        screen2.fill((255, 255, 255))
        self.screen = screen2
        self.spawn_level(self.round)

        hover_color = (100, 100, 100)
        default_color = (0, 0, 0)
        used_color = (100, 100, 100)
        used_hover_color = (150, 150, 150)

        while running:
            # check for close box
            for event in pygame.event.get():
                # handle hover effects
                if event.type == pygame.MOUSEMOTION:
                    if self.choosing:
                        if Enviro.inside(event.pos, self.pcard_1.rect):
                            Enviro.render_button(screen2, self.pcard_1, hover_color, self.backs[0])
                        else:
                            Enviro.render_button(screen2, self.pcard_1, default_color, self.backs[0])
                        if Enviro.inside(event.pos, self.pcard_2.rect):
                            Enviro.render_button(screen2, self.pcard_2, hover_color, self.backs[1])
                        else:
                            Enviro.render_button(screen2, self.pcard_2, default_color, self.backs[1])
                        if Enviro.inside(event.pos, self.pcard_3.rect):
                            Enviro.render_button(screen2, self.pcard_3, hover_color, self.backs[2])
                        else:
                            Enviro.render_button(screen2, self.pcard_3, default_color, self.backs[2])
                        if Enviro.inside(event.pos, self.pcard_4.rect):
                            Enviro.render_button(screen2, self.pcard_4, hover_color, self.backs[3])
                        else:
                            Enviro.render_button(screen2, self.pcard_4, default_color, self.backs[3])

                    if Enviro.inside(event.pos, self.card_num1.rect):
                        if not self.card_num1.hover:
                            if self.hand[0].is_not_used:
                                Enviro.render_button(screen2, self.card_num1, hover_color, self.backs[0])
                            else:
                                Enviro.render_button(screen2, self.card_num1, used_hover_color)
                            self.card_num1.hover = True
                    elif self.card_num1.hover:
                        if self.hand[0].is_not_used:
                            Enviro.render_button(screen2, self.card_num1, default_color, self.backs[0])
                        else:
                            Enviro.render_button(screen2, self.card_num1, used_color)
                        self.card_num1.hover = False

                    if Enviro.inside(event.pos, self.card_num2.rect):
                        if not self.card_num2.hover:
                            if self.hand[1].is_not_used:
                                Enviro.render_button(screen2, self.card_num2, hover_color, self.backs[1])
                            else:
                                Enviro.render_button(screen2, self.card_num2, used_hover_color)
                            self.card_num2.hover = True
                    elif self.card_num2.hover:
                        if self.hand[1].is_not_used:
                            Enviro.render_button(screen2, self.card_num2, default_color, self.backs[1])
                        else:
                            Enviro.render_button(screen2, self.card_num2, used_color)
                        self.card_num2.hover = False

                    if Enviro.inside(event.pos, self.card_num3.rect):
                        if not self.card_num3.hover:
                            if self.hand[2].is_not_used:
                                Enviro.render_button(screen2, self.card_num3, hover_color, self.backs[2])
                            else:
                                Enviro.render_button(screen2, self.card_num3, used_hover_color)
                            self.card_num3.hover = True
                    elif self.card_num3.hover:
                        if self.hand[2].is_not_used:
                            Enviro.render_button(screen2, self.card_num3, default_color, self.backs[2])
                        else:
                            Enviro.render_button(screen2, self.card_num3, used_color)
                        self.card_num3.hover = False

                    if Enviro.inside(event.pos, self.card_num4.rect):
                        if not self.card_num4.hover:
                            if self.hand[3].is_not_used:
                                Enviro.render_button(screen2, self.card_num4, hover_color, self.backs[3])
                            else:
                                Enviro.render_button(screen2, self.card_num4, used_hover_color)
                            self.card_num4.hover = True
                    elif self.card_num4.hover:
                        if self.hand[3].is_not_used:
                            Enviro.render_button(screen2, self.card_num4, default_color, self.backs[3])
                        else:
                            Enviro.render_button(screen2, self.card_num4, used_color)
                        self.card_num4.hover = False

                    if Enviro.inside(event.pos, self.card_num5.rect):
                        if not self.card_num5.hover:
                            if self.hand[4].is_not_used:
                                Enviro.render_button(screen2, self.card_num5, hover_color, self.backs[4])
                            else:
                                Enviro.render_button(screen2, self.card_num5, used_hover_color)
                            self.card_num5.hover = True
                    elif self.card_num5.hover:
                        if self.hand[4].is_not_used:
                            Enviro.render_button(screen2, self.card_num5, default_color, self.backs[4])
                        else:
                            Enviro.render_button(screen2, self.card_num5, used_color)
                        self.card_num5.hover = False

                    if Enviro.inside(event.pos, self.next_butt.rect):
                        if not self.next_butt.hover:
                            Enviro.render_button(screen2, self.next_butt, hover_color)
                            self.next_butt.hover = True
                    elif self.next_butt.hover:
                        Enviro.render_button(screen2, self.next_butt, default_color)
                        self.next_butt.hover = False

                # handle mouse clicks in buttons
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.choosing:
                        if not self.boss_Lvl:
                            if Enviro.inside(event.pos, self.pcard_1.rect):
                                self.curdeck.append(self.add_cards[0])
                                self.choosing = False
                                self.spawn_level((self.round + 2)//2)
                            if Enviro.inside(event.pos, self.pcard_2.rect):
                                self.curdeck.append(self.add_cards[1])
                                self.choosing = False
                                self.spawn_level((self.round + 2)//2)
                            if Enviro.inside(event.pos, self.pcard_3.rect):
                                self.curdeck.append(self.add_cards[2])
                                self.choosing = False
                                self.spawn_level((self.round + 2)//2)
                            if Enviro.inside(event.pos, self.pcard_4.rect):
                                self.curdeck.append(self.add_cards[3])
                                self.choosing = False
                                self.spawn_level((self.round + 2)//2)
                        else:
                            if Enviro.inside(event.pos, self.pcard_1.rect):
                                self.exD += 1
                                self.choosing = False
                                self.spawn_level((self.round + 2)//2)
                            if Enviro.inside(event.pos, self.pcard_2.rect):
                                self.exS += 1
                                self.choosing = False
                                self.spawn_level((self.round + 2)//2)
                            if Enviro.inside(event.pos, self.pcard_3.rect):
                                self.exH += 1
                                self.choosing = False
                                self.spawn_level((self.round + 2)//2)
                            if Enviro.inside(event.pos, self.pcard_4.rect):
                                self.exE += 1
                                self.choosing = False
                                self.spawn_level((self.round + 2)//2)

                    if Enviro.inside(event.pos, self.card_num1.rect):
                        self.hand[0].act(self.player, self.enemy_list[0], self.exD, self.exS, self.exH)
                        if self.enemy_list[0].health <= 0:
                            self.enemy_list.remove(self.enemy_list[0])
                        if len(self.enemy_list) == 0:
                            self.choose_cards()
                        else:
                            self.player_stats(self.player, self.enemy_list[0], screen2)

                    elif Enviro.inside(event.pos, self.card_num2.rect):
                        self.hand[1].act(self.player, self.enemy_list[0], self.exD, self.exS, self.exH)
                        if self.enemy_list[0].health <= 0:
                            self.enemy_list.remove(self.enemy_list[0])
                        if len(self.enemy_list) == 0:
                            self.choose_cards()
                        else:
                            self.player_stats(self.player, self.enemy_list[0], screen2)

                    elif Enviro.inside(event.pos, self.card_num3.rect):
                        self.hand[2].act(self.player, self.enemy_list[0], self.exD, self.exS, self.exH)
                        if self.enemy_list[0].health <= 0:
                            self.enemy_list.remove(self.enemy_list[0])
                        if len(self.enemy_list) == 0:
                            self.choose_cards()
                        else:
                            self.player_stats(self.player, self.enemy_list[0], screen2)

                    elif Enviro.inside(event.pos, self.card_num4.rect):
                        self.hand[3].act(self.player, self.enemy_list[0], self.exD, self.exS, self.exH)
                        if self.enemy_list[0].health <= 0:
                            self.enemy_list.remove(self.enemy_list[0])
                        if len(self.enemy_list) == 0:
                            self.choose_cards()
                        else:
                            self.player_stats(self.player, self.enemy_list[0], screen2)

                    elif Enviro.inside(event.pos, self.card_num5.rect):
                        self.hand[4].act(self.player, self.enemy_list[0], self.exD, self.exS, self.exH)
                        if self.enemy_list[0].health <= 0:
                            self.enemy_list.remove(self.enemy_list[0])
                        if len(self.enemy_list) == 0:
                            self.round += 1
                            self.choose_cards()
                        else:
                            self.player_stats(self.player, self.enemy_list[0], screen2)

                    elif Enviro.inside(event.pos, self.next_butt.rect):
                        Enviro.next(self)

                # handle close box
                if event.type == pygame.QUIT:
                    running = False
