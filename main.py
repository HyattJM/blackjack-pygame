
import os
import sys
import pygame
from pygame.locals import *
from random import randint, shuffle

# constants
WINDOW_SIZE = WIDTH, HEIGHT = 1200, 960


class Card:
    ''' settings for a card object - image, value '''

    def __init__(self, image, value):
        self.image = image
        self.value = value

    def is_ace(self, total):
        if total < 11:
            total += 11
        else:
            total += 1


class Deck:
    ''' contains settings for images and values of cards '''

    def __init__(self):
        # 0: clubs 1: diamonds  2: hearts 3: spades
        self.cards = {0: {}, 1: {}, 2: {}, 3: {}}
        # values are assigned to their position in the created deck
        # ace is at position 0, deal with it in play.calculate_hands
        self.values = [False, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def create(self):
        suits = ["Clubs ", "Diamond ", "Hearts ", "Spades "]
        # populate self cards with the appropriate images
        for suit in range(4):
            for card in range(1, 14):
                self.cards[suit][card] = Card(
                    pygame.image.load(
                        'assets/' + str(suits[suit]) + str(card) + '.png'),
                    self.values[card - 1]
                )


class Total:
    ''' holds totals and updates to screen '''

    def __init__(self):
        self.total = 0

    def update(self, value):
        self.total += value


class Play:
    ''' object to handle the main game being played '''

    def __init__(self):
        # hands
        self.player_hand = []
        self.dealer_hand = []

        # gui
        self.player_text = "Player: "
        self.dealer_text = "Dealer: "
        self.player_text_x = 135
        self.player_text_y = 435
        self.dealer_text_x = 135
        self.dealer_text_y = 235
        self.display_keys = [
            pygame.image.load("assets/KeyboardButtonsDir_up.png"),
            pygame.image.load("assets/KeyboardButtonsDir_down.png"),
            pygame.image.load("assets/KeyboardButtonsDir_left.png"),
            pygame.image.load("assets/KeyboardButtonsDir_right.png"),
        ]
        self.display_keys_text = {
            0: "Hit",
            1: "New Game",
            2: "Stay",
            3: "Null",
        }

        # action
        self.player = True

    def get_card(self, hand, number=1):
        for get_card in range(number):
            suit, card = randint(0, 3), randint(1, 13)
            hand.append(game.deck.cards[suit][card])
        self.calculate_hands(self.player_hand, player)
        self.calculate_hands(self.dealer_hand, dealer)

    def calculate_hands(self, hand, total):
        total.total = 0
        for card in range(len(hand)):
            # cards
            if hand[card].value:
                total.total += hand[card].value
            # aces
            else:
                pass

    def dealer_action(self):
        while dealer.total < 17:
            self.get_card(self.dealer_hand)

    def player_stay(self):
        self.player = False
        self.dealer_action()

    def display_hands(self):
        # cards
        x, y = 500, 200
        for card in range(len(self.dealer_hand)):
            game.screen.blit(self.dealer_hand[card].image, (x, y))
            x += 40
            y += 15
        x, y = 500, 390
        for card in range(len(self.player_hand)):
            game.screen.blit(self.player_hand[card].image, (x, y))
            x += 40
            y += 15
        # totals
        game.screen.blit(game.render_font(
            self.player_text + str(player.total)), (self.player_text_x, self.player_text_y))
        game.screen.blit(game.render_font(
            self.dealer_text + str(dealer.total)), (self.dealer_text_x, self.dealer_text_y))

    def display_gui(self):
        x, y = 45, 690
        for key in range(len(self.display_keys)):
            game.screen.blit(self.display_keys[key], (x, y)
                             )
            y += 55
        x, y = 105, 695
        for text in self.display_keys_text:
            game.screen.blit(game.render_font(
                self.display_keys_text[text]), (x, y)
            )
            y += 55

    def initialise(self):
        self.get_card(self.player_hand, 2)
        self.get_card(self.dealer_hand, 1)

    def loop(self):
        game.get_input()
        self.display_gui()
        self.display_hands()
        pygame.display.flip()

    def reset(self):
        # reset game to 0
        self.player_hand = []
        self.dealer_hand = []
        player.total = 0
        dealer.total = 0
        self.player = True
        self.initialise()


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
            0: "Blackjack",
            1: " ",
            2: "New Game",
            3: "How to play",
            4: "Exit Game",
        }
        self.menu_selector = '>'
        self.menu_selector_x = 475
        self.menu_selector_y = 490

        # how to play
        self.how_to_play = False
        self.how_to_play_text = {
            0: "How to play Blackjack - simplified",
            1: " ",
            2: "Beat the dealer's hand without going over 21.",
            3: "'23465789' are worth their face value.",
            4: "'JQK' = 10, 'A' = 1, 11 depending on best hand.",
            5: "Each player starts with two cards.",
            6: "HIT gets another card, STAND keeps the hand you have.",
            7: "If you go over 21 you BUST, and the dealer wins.",
            8: "2 card total of 21 equals BLACKJACK.",
            9: "Dealer plays until their cards total 17 or higher.",
        }

        # new game
        self.new_game = False

    # handle any player key presses
    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # back to main menu
                if event.key == pygame.K_ESCAPE:
                    if not self.main_menu:
                        self.main_menu = True
                        self.new_game = False
                        self.how_to_play = False
                        play.reset()

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
                            play.initialise()
                        if self.menu_selector_y == 535:
                            self.main_menu = False
                            self.new_game = False
                            self.how_to_play = True
                        if self.menu_selector_y == 580:
                            pygame.quit()
                            sys.exit("Thanks for playing!")

                # new game
                if self.new_game:
                    if event.key == pygame.K_UP:
                        play.get_card(play.player_hand)
                    if event.key == pygame.K_DOWN:
                        play.reset()
                    if event.key == pygame.K_RIGHT:
                        play.player_stay()

    # render all game objects
    def render(self):
        # render main menu
        if self.main_menu:
            menu_text_x, menu_text_y = 500, 400
            for text in self.menu_text:
                self.screen.blit(self.render_font(
                    self.menu_text[text]), (menu_text_x, menu_text_y))
                menu_text_y += 45
            self.screen.blit(self.render_font(self.menu_selector),
                             (self.menu_selector_x, self.menu_selector_y))

        # render how to play
        if self.how_to_play:
            x, y = 45, 45
            for text in self.how_to_play_text:
                self.screen.blit(self.render_font(
                    self.how_to_play_text[text]), (x, y))
                y += 45
            # display cards
            x, y = 45, 500
            for suit in range(0, 2):
                for card in self.deck.cards[suit]:
                    self.screen.blit(self.deck.cards[suit][card].image, (x, y))
                    x += 40
            x, y = 45, 600
            for suit in range(2, 4):
                for card in self.deck.cards[suit]:
                    self.screen.blit(self.deck.cards[suit][card].image, (x, y))
                    x += 40

    # function that will render font to blit
    def render_font(self, text):
        text_to_render = self.font.render(text, True, (255, 255, 255))
        return text_to_render

    # main game loop
    def loop(self):
        while True:
            self.screen.fill((0, 128, 0))

            self.render()
            self.get_input()

            if self.new_game:
                play.loop()

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    play = Play()
    player = Total()
    dealer = Total()
    game.loop()
