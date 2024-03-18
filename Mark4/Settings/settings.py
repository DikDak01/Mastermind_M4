
import Conversation
import Evaluation
import Settings
import Media
import Gameresults

from pymongo import *
import datetime as dt


#^ The player's settings are stored in this database

class Database_Evalution:
    
    def __init__(self) -> None:
        pass
    
    client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000", 2708)
    db = client.Resultsdb
    decisions = db.decisions    
        
    def datetime(self):
        self.actually_datetime = dt.datetime.now()    
    
    def save_results(self):
        self.user_decision = self.decisions.insert_one({"time": self.actually_datetime, "language:": self.language, "opponent:": self.opponent, "player1 name:": self.player1_name, "player2 name:": self.player2_name, "codemaker:": self.codemaker_choice})
        print("Results saved successfully.")
    
        for self.db.decisions in self.db.decisions.find():
            print(self.user_decision)