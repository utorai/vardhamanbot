import json
import re

from rasa_nlu.model import Interpreter

# Custom Components
class SemesterExtractor:
    @staticmethod
    def process(text):
        words = text.split(" ")
        ordinal_values = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7, "eigth": 8}
        semester = None

        for word in words:
            pattern = re.compile(r"\d+(st|nd|rd|th)")
            if pattern.search(word):
                semester = int(word[:-2])

        for word in words:
            word = word.lower()
            pattern = re.compile(r"(first|second|third|fourth|fifth|sixth|seventh|eigth)")
            if pattern.search(word):
                semester = ordinal_values[word]
        
        if semester != None:
            data = [{'entity': 'semester', 'value': semester}]
            return data

        return semester
# End of Custom Components

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
        semester_data = SemesterExtractor.process(self.text)
        if semester_data != None:
            self.data['entities'] += semester_data
        return dict(map((lambda x : (x['entity'], x['value'])), self.data['entities']))
            
class Engine:
    def __init__(self, models_path = "./models/vardhamanbot/nlu"):
        self.interpreter = Interpreter.load(models_path)
    
    def parse(self, message):
        message = message.strip(" \n\t\r.")
        return Data(message, self.interpreter.parse(message))