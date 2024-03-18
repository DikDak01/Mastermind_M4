from colorama import *
import emoji as em




# All questions in german of the entire game are in these classes

class Conversation_Init_German:
    def __init__(self):
        self.opponent = 0
        self.player1_name = ''
        self.player2_name = ''
        self.codemaker_choice = 0

        self.gamestart_choice = 0
        self.kidding_choice = 0

        self.omround_choice = 0
        self.settings_choice = 0
        self.slanguage_choice = 0


class Start_Questions_German(Conversation_Init_German):

    def opponent_q_ger(self):
        print("Willst du gegen den Computer oder einen Freund spielen:\n1. Computer 🤖\n2. Freund 👨‍🦳\n3. mit mir selbst 👀")
        self.opponent = int(input("Geben Sie die Nummer ein, die Ihrem bevorzugten Gegner entspricht:"))
        
    def player1_q_ger(self):
        print("Player 1, wie möchtest du im Spiel heißen?")
        self.player1_name = input("Geben Sie den Namen ein, der Ihrem bevorzugten Spielernamen entspricht:")
        
    def player2_q_ger(self):
        print("Player 2, wie möchtest du im Spiel heißen?")
        self.player2_name = input("Geben Sie den Namen ein, der Ihrem bevorzugten Spielernamen entspricht:")
        
    def codemaker_q_ger(self):
        print(f"Who wants to be the codemaker?\n1. {self.player1_name}\n2. {self.player2_name}")
        self.codemaker_choice = int(input("Geben Sie die Nummer ein, die Ihrer bevorzugter Wahl entspricht:"))

class Start_Answers_German(Start_Questions_German):

    def computer_a_ger(self):
        print(em.emojize("Du spielst gegen den Computer 🤖..."))

    def friend_a_ger(self):
        print(em.emojize("Nice, Du willst also gegen einen Freund spielen 👨‍🦳..."))

    def narcissism_a_ger(self):
        print("Ich glaube diese Seite könnte dich interessieren:")

    #Player vs. Computer
    def codemaker_a_ger(self):
        print(f"Okey, {self.opponent} Codemacher!")

    #Player vs. Player
    #TODO: Vl. könnte man das nur in einer Funktion lösen
    def player1cm_a_ger(self):
        print(f"Okey, {self.player1_name} ist der Codemacher!")

    def player2cm_a_ger(self):
        print(f"Okey, {self.player2_name} ist der Codemacher!")

class Intermediate_Questions_German(Start_Answers_German):
    
    def gamestart_q_ger(self):
        #TODO: Du/Ihr mit Formatstrings einfügen?
        print("Möchtest du/ihr das Spiel starten:\n1. Ja\n2. Nein")
        self.gamestart_choice = int(input("Geben Sie die Nummer ein, die Ihrer bevorzugter Wahl entspricht:"))

    def kidding_q_ger(self):
        print(em.emojize("Wieso nicht? Willst du mich verarschen 🤬?"))

        
class Intermediate_Answers_German(Intermediate_Questions_German):
    
    def comuptercm_a_ger(self):
        print(em.emojize("Der geheime Code ist generiert,\nviel Spass beim Code knacken 😄"))

    def waiting_a_ger(self):
        #TODO: Waiting Animation hinzufügen
        print("Ich warte...")

            
class Final_Questions_German(Intermediate_Answers_German):
    
    #TODO: omround = one more round, vl. fällt mir noch ein besserer Name ein
    def omround_q_ger(self):
        print("Hast du noch nicht genug? Willst du noch eine Runde spielen:\n1. Ja\n2. Nein")
        self.omround_choice = int(input("Geben Sie die Nummer ein, die Ihrer bevorzugter Wahl entspricht:"))
        
    def settings_q_ger(self):
        print("Willst du deine Einstellungen ändern:\n 1. Ja\n2. Nein")
        self.settings_choice = int(input("Geben Sie die Nummer ein, die Ihrer bevorzugter Wahl entspricht:"))

    #TODO: slanguage = same language, vl. fällt mir noch ein besserer Name ein
    def slanguage_q_ger(self):
        print("Möchtest du weiterhin auf derselben Sprache kommunizieren:\n1. Ja\n2. Nein")
        self.slanguage_choice = int(input("Geben Sie die Nummer ein, die Ihrer bevorzugter Wahl entspricht:"))

class Final_Answers_German(Final_Questions_German):
    
    def wincm_a_ger(self):
        print("Haha, anscheinend war dein Code zu gut um geknackt zu werden!\nHier ist deine Belohnung:")

    def wincb_a_ger(self):
        print("Hehe, Mr. Codebrecher hat wieder zugeschlagen, herzlichen Glühstrumpf!\nHier ist deine Belohnung:")

    def nextime_a_ger(self):
        print("Schade, dann bis zum nächsten Mal!")

    def no_change_a_ger(self):
        print("Okay, dann legen wir los!")

    #set = settings
    def change_set_a_ger(self):
        print("Gut, dann lass uns die anderen Einstellungen ändern!")

    #set = settings
    def change_set_a_engl(self):
        print("Great, then we continue the other settings!")
