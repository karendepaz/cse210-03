import random

class Director:
    """
    gets random word
    asks a player to guess a letter
    """

    def __init__(self):
        self.word = ["summer", "heat", "pool", "sun"]
    
    def random_word(self):

        word = random.choice(self.word).upper()

        return word

    def make_guess(self):
        guess = input("Guess a letter [a-z]: ").upper()
        return guess