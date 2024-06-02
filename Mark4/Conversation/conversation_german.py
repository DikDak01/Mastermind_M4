from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.Mastermind

collection = db.conversation_german

conversations_german = [

        {
            #1. Computer\n2. Freund\n3. mit mir
            "opponent": "Möchten Sie gegen einen Computer oder einen Freund antreten:"
        },

        {
            "player1": "Spieler 1, wie möchtest du im Spiel heißen?"
        },

        {
            "player2": "Jetzt ist Spieler 2 an der Reihe"
        },

        {
            "language": "Sehr gut, Sie möchten das Spiel also auf Englisch spielen und dann mit der nächsten Frage fortfahren"
        },

        {
            "opponent_computer": "Du spielst gegen den Computer 🤖..."
        },

        {
            "opponent_friend": "Schön, dass du also Lust hast, gegen einen Freund zu spielen 👨‍  ..."
        },

        {
            "narcissism": "Ich denke, diese Seite könnte Sie interessieren:"
        },

        {
            "codemaker": "Okey, {self.opponent} ist der Codemaker!"
        },

        {
            #\n1. Ja\n2. Nein
            "gamestart": "Möchten Sie das Spiel starten:"
        },

        {
            #\nWarum nicht?
            "kidding": "Machst du Witze 🤬"
        },

        {
            "computercm": "Der Geheimcode wurde generiert,\nviel Spaß beim Knacken des Codes 😄"
        },

        {
            "waiting": "I'm waiting"
        },

        {
            #\n1. Ja\n2. Nein
            "omr": "Hast du noch nicht genug? Möchten Sie eine weitere Runde spielen:"
        },

        {
            #\n 1. Ja\n2. Nein
            "set_change": "Möchten Sie Ihre Einstellungen ändern:"
        },

        {
            #\n 1. Ja\n2. Nein
            "s_language": "Möchten Sie weiterhin in derselben Sprache kommunizieren:"
        },

        {
            "wincm": "Haha, anscheinend war dein Code zu gut, um geknackt zu werden!\nHier ist deine Belohnung:"
        },

        {
            "wincb": "Haha, Mr. Codebreaker hat wieder zugeschlagen, herzlichen Glückwunsch!\nHier ist deine Belohnung:"
        },

        {
            "next_time": "Schade, bis zum nächsten Mal!"
        },

        {
            "no_change": "Okay, dann fangen wir mal an!"
        },

        {
            "change_set": "Okay, dann ändern wir jetzt die anderen Einstellungen!"
        },

        {
            "change_set_ger": "Well, let's continue with the other settings!"
        }
]
collection.insert_many(conversations_german)