from Conversation import conversation_german as ger, language, conversation_english as engl

import random
import sys
import time

class Evaluation_Init:

    def __init__(self):
        self.answer = ''
        self.it_is = None
        self.colors = ['red', 'green', 'blue', 'magenta', 'yellow', 'cyan']
        self.language = ''
        self.decision = ''
class Start_Decisions(Evaluation_Init):

    def language_decision(self):

        self.language = language.Start_Language.language_q_engl()
        language_options = {'German': 1, 'English': 2, 'Shut up': 3}

        for i in range(1000000):
            if language in language_options:
                self.decision = language_options[language]
            else:
                self.decision = 3

        if language.Start_Language.language_q_engl == 1:
            print("Sehr gut, du willst also das Spiel auf Deutsch spielen,\ndann gehts weiter mit der nächsten Frage:")
                 
        elif language.Start_Language.language_q_engl == 2:
            print("Very good, so you want to play the game in English,\nthen move on to the next question")
        
        elif language.Start_Language.language_q_engl == 3:
            self.answer = 'idiot'

    def opponent_d_ger(self):
        if ger.Start_Questions_German.opponent_q_ger == 1:
            print("Du spielst gegen den Computer, zeigs ihm!")
                 
        elif ger.Start_Questions_German.opponent_q_ger == 2:
            print("Du spielst also gegen ein Freund, möge der bessere gewinnen!")
           
        elif ger.Start_Questions_German.opponent_q_ger == 3:
            self.answer = 'goodbye'
                 
    def opponent_d_engl(self):
        if engl.Start_Questions_English.opponent_q_engl == 1:
            print("You're playing against the computer, show it what you've got!")


        elif engl.Start_Questions_English.opponent_q_engl == 2:
            print("So, you're playing against a friend, may the better one win!")
           
        elif engl.Start_Questions_English.opponent_q_engl == 3:
            self.answer = 'goodbye'

    def playernames_d_ger(self):
        try:
            str(ger.Start_Questions_German.player1_q_ger and ger.Start_Questions_German.player2_q_ger)
            self.it_is = True
            print("Es hat funktioniert, weitermachen!")

        except ValueError:
            self.it_is = False
            print("Was zum Fick, du hast Zahlen eingegeben???")

    def playernames_d_engl(self):
        try:
            str(engl.Start_Questions_English.player1_q_engl and engl.Start_Questions_English.player2_q_engl)
            self.it_is = True
            print("It worked, keep going!")

        except ValueError:
            self.it_is = False
            print("What the fuck, you entered numbers???")
    
    def codemaker_d_ger(self):
        if ger.Start_Questions_German.codemaker_q_ger == 1:
            print("Okey, du bist der Codemacher.\nKleiner Tipp: Mach einfach ein bombastischen Code!")
                 
        elif ger.Start_Questions_German.codemaker_q_ger == 2:
            print("Okey, der Computer ist der Codemacher,\nsei also bereit den Code zu knacken")
            self.secret_code = random.sample(self.colors, 4)

    def codemaker_d_engl(self):
        if engl.Start_Questions_English.codemaker_q_engl == 1:
            print("Okey, you are the code maker.\nLittle tip: Just create a bombastic code!!")
                 
        elif engl.Start_Questions_English.codemaker_q_engl == 2:
            print("Okey, the computer is the codemaker,\nso be ready to crack the code")
            self.secret_code = random.sample(self.colors, 4)

class Intermediate_Decisions(Start_Decisions):

    def gamestart_d_ger(self):
        if ger.Intermediate_Questions_German == 1:
            print("nice, wünsche viel Spass!")

        elif ger.Intermediate_Questions_German == 2:
            ger.Intermediate_Answers_German.kidding_q_ger()
            input("Wieso nicht du Lusche?")
            time.sleep(5)
            sys.exit()
    def gamestart_d_engl(self):
        if engl.Intermediate_Questions_English == 1:
            print("nice, have Fun!")

        elif engl.Intermediate_Questions_English == 2:
            engl.Intermediate_Answers_English.kidding_q_engl()
            input("Why not you slut?")
            time.sleep(5)
            sys.exit()

class Final_Decisions(Intermediate_Decisions):

    #TODO: The End hinzufügen aber wo und wie?
    def omround_d_ger(self):
        if ger.Final_Questions_German.omround_q_ger == 1:
            print("lass knacken!")
            ger.Final_Questions_German.settings_q_ger()

        elif ger.Final_Questions_German.omround_q_ger == 2:
            ger.Final_Answers_German.nextime_a_ger()
            self.answer = 'goodbye'
            time.sleep(5)
            sys.exit()

    def omround_d_engl(self):
        if engl.Final_Questions_English.omround_q_engl == 1:
            print("hit it!")
            engl.Final_Questions_English.settings_q_engl()

        elif engl.Final_Questions_English.omround_q_engl == 2:
            engl.Final_Answers_English.nextime_a_engl()
            self.answer = 'goodbye'
            time.sleep(5)
            sys.exit()


    def settings_d_ger(self):
        if ger.Final_Questions_German.settings_q_ger == 1:
            ger.Final_Answers_German.no_change_a_ger()

        elif ger.Final_Questions_German.settings_q_ger == 2:
            ger.Final_Questions_German.slanguage_q_ger()


    def settings_d_engl(self):
        if engl.Final_Questions_English.settings_q_engl == 1:
            engl.Final_Answers_English.no_change_a_engl()

        elif engl.Final_Questions_English.settings_q_engl == 2:
            engl.Final_Questions_English.slanguage_q_engl()

    def slanguage_d_ger(self):
        if ger.Final_Questions_German.slanguage_q_ger == 1:
            ger.Final_Answers_German.change_set_a_ger()

        elif ger.Final_Questions_German.slanguage_q_ger == 2:
            ger.Final_Answers_German.change_set_a_engl()

    def slanguage_d_engl(self):
        if engl.Final_Questions_English.slanguage_q_engl == 1:
            engl.Final_Answers_English.change_set_a_engl()

        elif engl.Final_Questions_English.slanguage_q_engl == 2:
            engl.Final_Answers_English.change_set_a_ger()



