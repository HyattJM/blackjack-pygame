
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
        self.font = pygame.font.Font('assets/clacon.ttf', 40)
        # assign cards to images
        self.deck = Deck()
        self.deck.create()
        # text for menu
        self.menu_text = {
            "title": self.font.render('Blackjack', True, (255, 255, 255)),
            "new_game": self.font.render('New Game', True, (255, 255, 255)),
            "how_to_play": self.font.render('How to play', True, (255, 255, 255)),
            "exit": self.font.render('New Game', True, (255, 255, 255)),
        }

    def get_input(self):
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit("Thanks for playing!")

    def loop(self):
        while True:
            self.screen.fill((0, 128, 0))

            menu_text_x, menu_text_y = 20, 20
            for text in self.menu_text:
                self.screen.blit(
                    self.menu_text[text], (menu_text_x, menu_text_y))
                menu_text_y += 45

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.loop()
