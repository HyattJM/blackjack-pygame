
import os
import sys
import pygame
from pygame.locals import *
from random import randint, shuffle

from settings import *


class Deck:
    ''' contains settings for images and values of cards '''

    def __init__(self):
        self.values = [[11, 1], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cards = {0: {}, 1: {}, 2: {}, 3: {}}

    def create(self):
        suits = ["Clubs ", "Diamond ", "Hearts ", "Spades "]
        for suit in range(4):
            for card in range(1, 14):
                self.cards[suit][card] = pygame.image.load(
                    'assets/' + str(suits[suit]) + str(card) + '.png')


class Game:
    ''' game object - handles everything involved in the game process '''

    def __init__(self):
        # initialise pygame and set window values
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Blackjack")
        self.font = pygame.font.Font('assets/clacon.ttf', 50)
        # assign cards to images
        self.deck = Deck()
        self.deck.create()

        # text and settings for main menu
        self.main_menu = True
        self.menu_text = {
            "title": self.font.render('Blackjack', True, (255, 255, 255)),
            "divider": self.font.render('---------', True, (255, 255, 255)),
            "new_game": self.font.render('New Game', True, (255, 255, 255)),
            "how_to_play": self.font.render('How to play', True, (255, 255, 255)),
            "exit": self.font.render('Exit Game', True, (255, 255, 255)),
        }
        self.menu_selector = self.font.render('>', True, (255, 255, 255))
        self.menu_selector_x = 475
        self.menu_selector_y = 490

        # how to play
        self.how_to_play = False
        self.how_to_play_text = {
            0: "How to play Blackjack - simplified",
            1: "---------------------------------",
            2: " ",
            3: "Beat the dealer's hand without going over 21.",
            4: "'23465789' worth face value. 'JQK' = 10, 'A' = 1, 11.",
            5: "Each player starts with two cards.",
            6: "HIT gets another card, STAND keeps the hand you have.",
            7: "If you go over 21 you BUST, and the dealer wins.",
            8: "2 card total of 21 equals BLACKJACK.",
            10: "Dealer plays until their cards total 17 or higher.",
        }

        # new game
        self.new_game = False

    def get_input(self):
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            # back to main menu
            if event.key == pygame.K_ESCAPE:
                if not self.main_menu:
                    self.main_menu = True
                    self.new_game = False
                    self.how_to_play = False

            # main menu
            if self.main_menu:
                if event.key == pygame.K_DOWN:
                    if self.menu_selector_y < 580:
                        self.menu_selector_y += 45
                if event.key == pygame.K_UP:
                    if self.menu_selector_y > 490:
                        self.menu_selector_y -= 45

                if event.key == pygame.K_RETURN:
                    if self.menu_selector_y == 490:
                        self.main_menu = False
                        self.new_game = True
                        self.how_to_play = False
                    if self.menu_selector_y == 535:
                        self.main_menu = False
                        self.new_game = False
                        self.how_to_play = True
                    if self.menu_selector_y == 580:
                        pygame.quit()
                        sys.exit("Thanks for playing!")

    def render(self):
        # render main menu
        if self.main_menu:
            menu_text_x, menu_text_y = 500, 400
            for text in self.menu_text:
                self.screen.blit(
                    self.menu_text[text], (menu_text_x, menu_text_y))
                menu_text_y += 45
            self.screen.blit(self.menu_selector,
                             (self.menu_selector_x, self.menu_selector_y))

        # render how to play
        if self.how_to_play:
            x, y = 45, 45
            for text in self.how_to_play_text:
                self.screen.blit(self.render_font(self.how_to_play_text[text]), (x, y))
                y += 45

    def render_font(self, text):
        text_to_render=self.font.render(text, True, (255, 255, 255))
        return text_to_render

    def loop(self):
        while True:
            self.screen.fill((0, 128, 0))

            self.render()
            self.get_input()

            pygame.display.flip()


if __name__ == "__main__":
    game=Game()
    game.loop()
