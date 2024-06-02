from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.Mastermind

collection = db.conversation_english

conversations_english = [

        {
            #\n1. German\n2. English\n3. Shut up!
            "language": "In which language you wanna play:"
        },

        {
            #\n1. Computer\n2. Friend\n3. with myself
            "opponent": "Do you want to compete against a computer or friend:"
        },

        {
            "player1": "Player 1, what do you want to be called in the game?"
        },

        {
            "player2": "Player 2 now it's your turn"
        },

        {
            "language": "Very good, so you want to play the game in English,\nthen move on to the next question"
        },

        {
            "opponent_computer": "You play against the computer 🤖..."
        },

        {
            "opponent_friend": "Nice, so you want to play against a friend 👨‍🦳..."
        },

        {
            "narcissism": "I think this page might interest you:"
        },

        {
            "codemaker": "Okey, is the {self.opponent} Codemaker!"
        },

        {
            #\n1. Yes\n2. No
            "gamestart": "Would you like to start the game:"
        },

        {
            #\nwhy not?
            "kidding": "are you kidding me 🤬"
        },

        {
            "computercm": "The secret code has been generated,\nhave fun cracking the code 😄"
        },

        {
            "waiting": "I'm waiting"
        },

        {
            #\n1. Yes\n2. No
            "omr": "Don't you have enough yet? Do you want to play another round:"
        },

        {
            #\n 1. Yes\n2. No
            "set_change": "Do you want to change your settings:"
        },

        {
            #\n 1. Yes\n2. No
            "s_language": "Do you want to continue communicating in the same language:"
        },

        {
            "wincm": "Haha, apparently your code was too good to be cracked!\nHere's your reward:"
        },

        {
            "wincb": "Hehe, Mr. Codebreaker has struck again, congratulations!\nHere is your reward:"
        },

        {
            "next_time": "Too bad, see you next time!"
        },

        {
            "no_change": "Okay, then let's get started!"
        },

        {
            "change_set": "Okay, then let's change the other settings!"
        },

        {
            "change_set_ger": "Gut, dann lass uns mit den anderen Einstellungen fortfahren!"
        }
]
collection.insert_many(conversations_english)