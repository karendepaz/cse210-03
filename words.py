import random

class Word_list:
    
    def __init__(self):
        self._word = ["summer", "heat", "pool", "sun"]
    
    def random_word(self):

        word = random.choice(self._word).upper()

        return word