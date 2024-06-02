import sys
import pprint as pp

sys.path.insert(0, '/Users/niknak/Documents/01_Projekte/Programming/Python/Games/Mark4/Mark4/Conversation')

from Mark4.Conversation import conversation_german as ger, conversation_english as engl


class Evaluation_Init:

    def __init__(self):
        pass


class Evaluation(Evaluation_Init):

    @staticmethod
    def language_switch():
        try:
            pp.pprint(engl.collection.find_one({"language": "In which language you wanna play:"}))
            language_options = "1. German\n2. English\n3. Shut up\nChoose your language: "
            language_answer = input(language_options)
        except KeyboardInterrupt:
            print("Wrong Input")

        match language_answer:
            case 'German' | '1':
                print("So so, du möchtest also das Spiel auf Deutsch spielen. Nächste Frage:")
            case 'English' | '2':
                print("So you want to play the game in English. Next question:")
            case 'Shut Up' | '3':
                print("Idiot")
                sys.exit()
