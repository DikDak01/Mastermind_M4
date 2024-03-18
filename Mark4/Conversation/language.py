from colorama import *
import emoji as em


class Conversion_Init_Language:
    def __init__(self):
        self.language_engl = 0


class Start_Language(Conversion_Init_Language):
    def language_q_engl(self):
        print("In which language you wanna play:\n1. German\n2. English\n3. Shut up!")
        self.language_engl = int(input("Enter the number corresponding to your preferred language:"))

