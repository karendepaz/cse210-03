from check_guess import Check
from words import Word_list
from jumper import Jumper

class Director:
    """
    gets random word
    asks a player to guess a letter
    """
    def __init__(self):
        self.is_game_over = False

        
        self.current_word = Word_list()

    def start_game(self):
        print('Welcome to the Jumper game')

        #
        self.current_word.random_word()
        while self.is_game_over == False:
            self.make_guess()

    def make_guess(self):
        guess = input("Guess a letter [a-z]: ").upper()
        return guess

    
    jumper = Jumper()
    check = Check()
    

    #prints the word in order to make sure that the call to the function
    #director.random_word() worked properly
    print(word)

    # calls the check_letter function through the Check class in check_guess.py
    # requires the word and the guess
    # sees if the guess is in the word and print out word completion
    letter = check.check_letter(word, guess)





    #this print statement is here in order to test out the jumper
    # and to make sure that he prints correctly
    #starting at index 0 and going to 4 you can cycle through
    #the different stages of the jumper and his parachute
    print(jumper._stages[4])