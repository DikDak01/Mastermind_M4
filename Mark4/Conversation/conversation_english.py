
from colorama import *
import emoji as em


#^ All questions of the entire game are in these classes

class Conversion_Init:
    
    def __init__(self) -> None:
        self.opponent = 0
        self.player1_name = ''
        self.player2_name = ''
        self.codemaker_choice = 0

        self.gamestart_choice = 0
        self.kidding_choice = 0

        self.omround_choice = 0
        self.settings_choice = 0
        self.slanguage_choice = 0

                 

class Start_Questions_English(Conversion_Init):

    def opponent_q_engl(self):
        print("Do you want to compete against a computer or friend:\n1. Computer\n2. Friend\n3. with myself")
        self.opponent = int(input("Enter the number corresponding to your preferred opponent:"))
        
    def player1_q_engl(self):
        print("Player 1, what do you want to be called in the game?")
        self.player1_name = input("Enter the name corresponding to your preferred playername:")
        
    def player2_q_engl(self):
        print("Player 2 now it's your turn")
        self.player2_name = input("Enter the name corresponding to your preferred playername:")
        
    def codemaker_q_engl(self):
        print(f"Who wants to be the codemaker?\n1. {self.player1_name}\n2. {self.player2_name}")
        self.codemaker_choice = int(input("Enter the number corresponding to your preferred opponent:"))


class Start_Answers_English(Start_Questions_English):

    def computer_a_engl(self):
        print(em.emojize("You play against the computer 🤖..."))

    def friend_a_engl(self):
        print(em.emojize("Nice, so you want to play against a friend 👨‍🦳..."))

    def narcissism_a_engl(self):
        print("I think this page might interest you:")

    # Player vs. Computer
    def codemaker_a_engl(self):
        print(f"Okey, {self.opponent} Codemaker!")

    # Player vs. Player
    # TODO: Vl. könnte man das nur in einer Funktion lösen
    def player1cm_a_engl(self):
        print(f"Okey, {self.player1_name} is the Codemaker!")

    def player2cm_a_engl(self):
        print(f"Okey, {self.player2_name} is the Codemaker!")


class Intermediate_Questions_English(Start_Answers_English):

    def gamestart_q_engl(self):
        # TODO: Du/Ihr mit Formatstrings einfügen?
        print("Would you like to start the game:\n1. Yes\n2. No")
        self.gamestart_choice = int(input("Enter the number that corresponds to your preferred choice:"))

    def kidding_q_engl(self):
        print(em.emojize("are you kidding me 🤬?"))
        self.kidding_choice = input("why not?")


class Intermediate_Answers_English(Intermediate_Questions_English):

    def comuptercm_a_engl(self):
        print(em.emojize("The secret code has been generated,\nhave fun cracking the code 😄"))

    def waiting_a_engl(self):
        # TODO: Waiting Animation hinzufügen
        print("I'm waiting...")


class Final_Questions_English(Intermediate_Answers_English):

    # TODO: omround = one more round, vl. fällt mir noch ein besserer Name ein
    def omround_q_engl(self):
        print("Don't you have enough yet? Do you want to play another round:\n1. Yes\n2. No")
        self.omround_choice = int(input("Enter the number that corresponds to your preferred choice:"))

    def settings_q_engl(self):
        print("Do you want to change your settings:\n 1. Yes\n2. No")
        self.settings_choice = int(input("Enter the number that corresponds to your preferred choice:"))

    # slanguage = same language, vl. fällt mir noch ein besserer Name ein
    def slanguage_q_engl(self):
        print("Do you want to continue communicating in the same language:\n 1. Yes\n2. No")
        self.slanguage_choice = int(input("Enter the number that corresponds to your preferred choice:"))


class Final_Answers_English(Final_Questions_English):

    def wincm_a_engl(self):
        print("Haha, apparently your code was too good to be cracked!\nHere's your reward:")

    def wincb_a_engl(self):
        print("Hehe, Mr. Codebreaker has struck again, congratulations!\nHere is your reward:")

    def nextime_a_engl(self):
        print("Too bad, see you next time!")

    def no_change_a_engl(self):
        print("Okay, then let's get started!")


    def change_set_a_engl(self):
       print("Okay, then let's change the other settings!")


    def change_set_a_ger(self):
        print("Gut, dann lass uns mit den anderen Einstellungen fortfahren!")
