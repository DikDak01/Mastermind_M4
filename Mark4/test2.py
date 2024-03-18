from colorama import *
import sys
import time
import random


#TODO: evaluation.py überarbeiten siehe hier

class Game:
    language_texts = {
        'german': {
            'language_decision': "Sehr gut, du willst also das Spiel auf Deutsch spielen,\ndann gehts weiter mit der nächsten Frage:",
            'opponent_texts': ["Du spielst gegen den Computer, zeigs ihm!", "Du spielst also gegen ein Freund, möge der bessere gewinnen!"],
            'playername_texts': ["Es hat funktioniert, weitermachen!", "Was zum Fick, du hast Zahlen eingegeben???"]
        },
        'english': {
            'language_decision': "Very good, so you want to play the game in English,\nthen move on to the next question",
            'opponent_texts': ["You're playing against the computer, show it what you've got!", "So, you're playing against a friend, may the better one win!"],
            'playername_texts': ["It worked, keep going!", "What the fuck, you entered numbers???"]
        }
    }

    def __init__(self):
        self.language = ''
        self.opponent = ''
        self.players = []
        self.codemaker = ''

    def choose_language(self):
        print("Choose your language:")
        print("1. German")
        print("2. English")
        self.language = input("Enter your choice: ")
        print(Game.language_texts['german' if self.language == '1' else 'english']['language_decision'])

    def choose_opponent(self):
        print("Choose your opponent:")
        print("1. Computer")
        print("2. Friend")
        self.opponent = input("Enter your choice: ")
        print(Game.language_texts['german' if self.language == '1' else 'english']['opponent_texts'][int(self.opponent) - 1])

    def enter_player_names(self):
        self.players.append(input("Enter player 1 name: "))
        self.players.append(input("Enter player 2 name: "))
        try:
            int(self.players[0]) or int(self.players[1])
            print(Game.language_texts['german' if self.language == '1' else 'english']['playername_texts'][1])
        except ValueError:
            print(Game.language_texts['german' if self.language == '1' else 'english']['playername_texts'][0])

    def choose_codemaker(self):
        if self.opponent == '1':
            self.codemaker = random.choice(self.players)
            print(f"{self.codemaker} is the codemaker.")
        else:
            print("The computer is the codemaker.")

    def start_game(self):
        self.choose_language()
        self.choose_opponent()
        self.enter_player_names()
        self.choose_codemaker()

if __name__ == "__main__":
    game = Game()
    game.start_game()

