from ascii_magic import *
from colorama import Fore


class Media_Init_ASCII:
    def __init__(self):
        self.gametitle = None
        self.cookie_reward = None
        self.beer_reward = None


class ASCII_ART:

    def mastermind_title(self):
        try:
            self.gametitle = AsciiArt.from_image('Pictures/mastermind.png')
            self.gametitle.to_ascii(columns=80, back=Back.BLACK)
            #wanna see the output? -> evaluation.py
            
        except FileNotFoundError as gametitle:
            print(Fore.RED + "Gametitle file not found!", gametitle)
            
    def cm_reward(self):
        try:
            self.cookie_reward = AsciiArt.from_image('Pictures/cookie_reward.png')
            self.cookie_reward.to_ascii(columns=60, monochrome=False)
            #wanna see the output? -> evaluation.py
                        
        except FileNotFoundError as cookie:
            print(Fore.RED + "Cookie file not found!", cookie)

    def cb_reward(self):
        try:
            self.beer_reward = AsciiArt.from_image('Pictures/beer_reward.png')
            self.beer_reward.to_ascii(columns=60, monochrome=False)
            #wanna see the output? -> evaluation.py
            
        except FileNotFoundError as beer:
            print(Fore.RED + "Beer file not found!", beer)
