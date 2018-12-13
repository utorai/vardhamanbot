import json

from rasa_nlu.model import Interpreter

class Data:
    def __init__(self, text, data):
        self.text = text
        self.data = data
    
    def __repr__(self):
        return str(self.data)

    def get_intent(self):
        if self.text == "Get Started":
            return "start"
        else:
            return self.data['intent']['name']
    
    def get_confidence(self):
        return self.data['intent']['confidence']

    def get_entities(self):
        return dict(map((lambda x : (x['entity'], x['value'])), self.data['entities']))
            
class Engine:
    def __init__(self, models_path = "./models/vardhamanbot/nlu"):
        self.interpreter = Interpreter.load(models_path)
    
    def parse(self, message):
        message = message.strip(" \n\t\r.")
        return Data(message, self.interpreter.parse(message))