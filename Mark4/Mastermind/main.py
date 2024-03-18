from Rules import web_backend
from Evaluation import evaluation

from colorama import *
import random
import time
import sqlite3



init(autoreset=True)

class Mastermind:
    def __init__(self):
        self.max_attempts = 7
        self.secret_code = None
        self.field = ['0', '1', '2', '3']
        self.players = []
        self.computer = []
        self.colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']


    def gametitle(self):
        with open('./ASCI-ART/Mastermind_Title.txt', 'r') as gametitle:
            print(gametitle.read())


class Gamelogic():


    
    def add_player(self, player, computer):
        self.players.append(player, computer)

    def playground(self):
        print("|".join(self.field))
        
    def play_game(self):
        self.introduction()

        for player in self.players:
            player.setup()

        while self.max_attempts > 0:
            self.playground()
            self.generate_secret_code()

            for player in self.players:
                player.make_move()

                if player.check_win(self.secret_code):
                    print(Fore.GREEN + f"Congratulations, {player.name}! You've cracked the code!")
                    return

            self.max_attempts -= 1

        print(Fore.RED + "Sorry, you've run out of attempts. The secret code was:", self.secret_code)

    def check_win(self, secret_code):
        return self.choice == secret_code


    def setup_cb(self):
        print(f"Welcome, {self.name}! You are a Codebreaker.")
        self.choice = input(f"{self.name}, enter your code: ")

    def setup_cm(self):
        print(f"Welcome, {self.name}! You are a Codemaker.")
        self.choice = random.sample(self.colors_cm_cb, 4)





if __name__ == "__main__":
    game_instance = Mastermind()


    
