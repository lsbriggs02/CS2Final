import pygame
import random
from random import randint

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


class Enviro:
    def __init__(self, play):
        pygame.init()
        self.player = play
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
        self.choosing = False

    @staticmethod
    def render_button(screen, button, color):
        text = pygame.font.SysFont('Ariel', 30)
        pygame.draw.rect(screen, color, button.rect, 0, 4)
        pygame.draw.rect(screen, (0, 0, 0), button.rect, 1, 4)
        text.render_multi_line(button.rect[0], button.rect[1], 30)
        pygame.display.update()

    @staticmethod
    def inside(point, rect):
        return rect[0] <= point[0] <= rect[0] + rect[2] and rect[1] <= point[1] <= rect[1] + rect[3]

    add_cards = []

    def next(self):
        _ = 0
        # Reset acting deck with current deck
        if len(self.encounter_deck) <= 5:
            self.encounter_deck = self.curdeck[:]
        # Fill up add cards while removing from encounter deck
        while _ < 5:
            rand_card_num = randint(0, (len(self.encounter_deck) - 1))
            print(self.curdeck)
            self.add_cards.append(self.encounter_deck[rand_card_num])
            self.encounter_deck.remove(self.encounter_deck[rand_card_num])
            _ += 1
        # Reset hand with the new cards
        self.hand = self.add_cards[:]
        # Reset add cards to none
        self.add_cards = []
        # Enemy makes a move
        self.enemy_list[0].act(self.player, random.randint(0, 5))
        # Reset play stats and update screen
        self.player.energy = 3
        self.player.shield = 0
        self.player_stats(self.player, self.enemy_list[0], self.screen)
        # Reset names with new cards
        self.card_num1 = _Button((0, 550, 140, 30), self.hand[0].name)
        self.card_num2 = _Button((140, 550, 140, 30), self.hand[1].name)
        self.card_num3 = _Button((280, 550, 140, 30), self.hand[2].name)
        self.card_num4 = _Button((420, 550, 140, 30), self.hand[3].name)
        self.card_num5 = _Button((560, 550, 140, 30), self.hand[4].name)
        # Reset buttons to render with the new names
        Enviro.render_button(self.screen, self.card_num1, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num2, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num3, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num4, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num5, (255, 255, 255))

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

        Enviro.render_button(screen, h, (255, 255, 255))
        Enviro.render_button(screen, e, (255, 255, 255))
        Enviro.render_button(screen, s, (255, 255, 255))
        Enviro.render_button(screen, eh, (255, 255, 255))
        Enviro.render_button(screen, es, (255, 255, 255))

    def choose_cards(self):
        self.screen.fill((255, 255, 255))
        self.choosing = True

        self.card_num1 = _Button((0, 0, 0, 0), '')
        self.card_num2 = _Button((0, 0, 0, 0), '')
        self.card_num3 = _Button((0, 0, 0, 0), '')
        self.card_num4 = _Button((0, 0, 0, 0), '')
        self.card_num5 = _Button((0, 0, 0, 0), '')
        self.next_butt = _Button((0, 0, 0, 0), '')

        for _ in range(4):
            self.add_cards.append(self.gendeck[randint(0, len(self.gendeck) - 1)])

        self.pcard_1 = _Button((100, 250, 140, 200), str(self.add_cards[0]))
        self.pcard_2 = _Button((250, 250, 140, 200), str(self.add_cards[1]))
        self.pcard_3 = _Button((400, 250, 140, 200), str(self.add_cards[2]))
        self.pcard_4 = _Button((550, 250, 140, 200), str(self.add_cards[3]))

        Enviro.render_button(self.screen, self.card_num1, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num2, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num3, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num4, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num5, (255, 255, 255))
        Enviro.render_button(self.screen, self.next_butt, (255, 255, 255))

        Enviro.render_button(self.screen, self.pcard_1, (255, 255, 255))
        Enviro.render_button(self.screen, self.pcard_2, (255, 255, 255))
        Enviro.render_button(self.screen, self.pcard_3, (255, 255, 255))
        Enviro.render_button(self.screen, self.pcard_4, (255, 255, 255))

    def print_cards_undo(self):
        pass

    def spawn_level(self, enemy_list):
        self.screen.fill((255, 255, 255))
        # Set up encounter deck(for easy mutation of cards)
        self.encounter_deck = self.curdeck[:]
        self.enemy_list = enemy_list[:]
        # Create discard deck
        self.discard_deck = []
        # Create list for cards to choose from to add to curdeck
        self.add_cards = []

        _ = 0
        while _ < 5:
            rand_card_num = random.randint(0, (len(self.encounter_deck)-1))
            self.add_cards.append(self.encounter_deck[rand_card_num])
            self.encounter_deck.remove(self.encounter_deck[rand_card_num])
            _ += 1
        self.hand = self.add_cards[:]
        self.player.energy = 3
        self.player.shield = 0

        # define buttons
        self.card_num1 = _Button((0, 550, 140, 30), self.hand[0].name)
        self.card_num2 = _Button((140, 550, 140, 30), self.hand[1].name)
        self.card_num3 = _Button((280, 550, 140, 30), self.hand[2].name)
        self.card_num4 = _Button((420, 550, 140, 30), self.hand[3].name)
        self.card_num5 = _Button((560, 550, 140, 30), self.hand[4].name)
        self.next_butt = _Button((710, 550, 80, 30), 'Next')

        self.pcard_1 = _Button((0, 0, 0, 0), '')
        self.pcard_2 = _Button((0, 0, 0, 0), '')
        self.pcard_3 = _Button((0, 0, 0, 0), '')
        self.pcard_4 = _Button((0, 0, 0, 0), '')

        # add buttons
        Enviro.render_button(self.screen, self.card_num1, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num2, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num3, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num4, (255, 255, 255))
        Enviro.render_button(self.screen, self.card_num5, (255, 255, 255))
        Enviro.render_button(self.screen, self.next_butt, (255, 255, 255))

        Enviro.render_button(self.screen, self.pcard_1, (255, 255, 255))
        Enviro.render_button(self.screen, self.pcard_2, (255, 255, 255))
        Enviro.render_button(self.screen, self.pcard_3, (255, 255, 255))
        Enviro.render_button(self.screen, self.pcard_4, (255, 255, 255))

        self.player_stats(self.player, self.enemy_list[0], self.screen)

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
        self.spawn_level([Enemy(0)])

        hover_color = (200, 200, 200)
        default_color = (255, 255, 255)
        used_color = (100, 100, 100)
        used_hover_color = (150, 150, 150)

        while running:
            # check for close box
            for event in pygame.event.get():
                # handle hover effects
                if event.type == pygame.MOUSEMOTION:
                    if self.choosing:
                        if Enviro.inside(event.pos, self.pcard_1.rect):
                            Enviro.render_button(screen2, self.pcard_1, hover_color)
                        else:
                            Enviro.render_button(screen2, self.pcard_1, default_color)
                        if Enviro.inside(event.pos, self.pcard_2.rect):
                            Enviro.render_button(screen2, self.pcard_2, hover_color)
                        else:
                            Enviro.render_button(screen2, self.pcard_2, default_color)
                        if Enviro.inside(event.pos, self.pcard_3.rect):
                            Enviro.render_button(screen2, self.pcard_3, hover_color)
                        else:
                            Enviro.render_button(screen2, self.pcard_3, default_color)
                        if Enviro.inside(event.pos, self.pcard_4.rect):
                            Enviro.render_button(screen2, self.pcard_4, hover_color)
                        else:
                            Enviro.render_button(screen2, self.pcard_4, default_color)

                    if Enviro.inside(event.pos, self.card_num1.rect):
                        if not self.card_num1.hover:
                            if self.hand[0].is_not_used:
                                Enviro.render_button(screen2, self.card_num1, hover_color)
                            else:
                                Enviro.render_button(screen2, self.card_num1, used_hover_color)
                            self.card_num1.hover = True
                    elif self.card_num1.hover:
                        if self.hand[0].is_not_used:
                            Enviro.render_button(screen2, self.card_num1, default_color)
                        else:
                            Enviro.render_button(screen2, self.card_num1, used_color)
                        self.card_num1.hover = False

                    if Enviro.inside(event.pos, self.card_num2.rect):
                        if not self.card_num2.hover:
                            if self.hand[1].is_not_used:
                                Enviro.render_button(screen2, self.card_num2, hover_color)
                            else:
                                Enviro.render_button(screen2, self.card_num2, used_hover_color)
                            self.card_num2.hover = True
                    elif self.card_num2.hover:
                        if self.hand[1].is_not_used:
                            Enviro.render_button(screen2, self.card_num2, default_color)
                        else:
                            Enviro.render_button(screen2, self.card_num2, used_color)
                        self.card_num2.hover = False

                    if Enviro.inside(event.pos, self.card_num3.rect):
                        if not self.card_num3.hover:
                            if self.hand[2].is_not_used:
                                Enviro.render_button(screen2, self.card_num3, hover_color)
                            else:
                                Enviro.render_button(screen2, self.card_num3, used_hover_color)
                            self.card_num3.hover = True
                    elif self.card_num3.hover:
                        if self.hand[2].is_not_used:
                            Enviro.render_button(screen2, self.card_num3, default_color)
                        else:
                            Enviro.render_button(screen2, self.card_num3, used_color)
                        self.card_num3.hover = False

                    if Enviro.inside(event.pos, self.card_num4.rect):
                        if not self.card_num4.hover:
                            if self.hand[3].is_not_used:
                                Enviro.render_button(screen2, self.card_num4, hover_color)
                            else:
                                Enviro.render_button(screen2, self.card_num4, used_hover_color)
                            self.card_num4.hover = True
                    elif self.card_num4.hover:
                        if self.hand[3].is_not_used:
                            Enviro.render_button(screen2, self.card_num4, default_color)
                        else:
                            Enviro.render_button(screen2, self.card_num4, used_color)
                        self.card_num4.hover = False

                    if Enviro.inside(event.pos, self.card_num5.rect):
                        if not self.card_num5.hover:
                            if self.hand[4].is_not_used:
                                Enviro.render_button(screen2, self.card_num5, hover_color)
                            else:
                                Enviro.render_button(screen2, self.card_num5, used_hover_color)
                            self.card_num5.hover = True
                    elif self.card_num5.hover:
                        if self.hand[4].is_not_used:
                            Enviro.render_button(screen2, self.card_num5, default_color)
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
                        if Enviro.inside(event.pos, self.pcard_1.rect):
                            self.curdeck.append(self.pcard_1)
                            self.choosing = False
                            self.spawn_level([Enemy(0)])
                        if Enviro.inside(event.pos, self.pcard_2.rect):
                            self.curdeck.append(self.pcard_2)
                            self.choosing = False
                            self.spawn_level([Enemy(0)])
                        if Enviro.inside(event.pos, self.pcard_3.rect):
                            self.curdeck.append(self.pcard_3)
                            self.choosing = False
                            self.spawn_level([Enemy(0)])
                        if Enviro.inside(event.pos, self.pcard_4.rect):
                            self.curdeck.append(self.pcard_4)
                            self.choosing = False
                            self.spawn_level([Enemy(0)])

                    if Enviro.inside(event.pos, self.card_num1.rect):
                        self.hand[0].act(self.player, self.enemy_list[0])
                        if self.enemy_list[0].health <= 0:
                            self.enemy_list.remove(self.enemy_list[0])
                        if len(self.enemy_list) == 0:
                            self.choose_cards()
                        else:
                            self.player_stats(self.player, self.enemy_list[0], screen2)

                    elif Enviro.inside(event.pos, self.card_num2.rect):
                        self.hand[1].act(self.player, self.enemy_list[0])
                        if self.enemy_list[0].health <= 0:
                            self.enemy_list.remove(self.enemy_list[0])
                        if len(self.enemy_list) == 0:
                            self.choose_cards()
                        else:
                            self.player_stats(self.player, self.enemy_list[0], screen2)

                    elif Enviro.inside(event.pos, self.card_num3.rect):
                        self.hand[2].act(self.player, self.enemy_list[0])
                        if self.enemy_list[0].health <= 0:
                            self.enemy_list.remove(self.enemy_list[0])
                        if len(self.enemy_list) == 0:
                            self.choose_cards()
                        else:
                            self.player_stats(self.player, self.enemy_list[0], screen2)

                    elif Enviro.inside(event.pos, self.card_num4.rect):
                        self.hand[3].act(self.player, self.enemy_list[0])
                        if self.enemy_list[0].health <= 0:
                            self.enemy_list.remove(self.enemy_list[0])
                        if len(self.enemy_list) == 0:
                            self.choose_cards()
                        else:
                            self.player_stats(self.player, self.enemy_list[0], screen2)

                    elif Enviro.inside(event.pos, self.card_num5.rect):
                        self.hand[4].act(self.player, self.enemy_list[0])
                        if self.enemy_list[0].health <= 0:
                            self.enemy_list.remove(self.enemy_list[0])
                        if len(self.enemy_list) == 0:
                            self.choose_cards()
                        else:
                            self.player_stats(self.player, self.enemy_list[0], screen2)

                    elif Enviro.inside(event.pos, self.next_butt.rect):
                        Enviro.next(self)

                # handle close box
                if event.type == pygame.QUIT:
                    running = False
