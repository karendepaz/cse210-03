# Import the necessary libraries.
import random

class SecretWord:
    """
    A secret word that the player has to guess.

    The responsibility of the SecretWord is to select and store the
    word that the player has to guess.

    Attributes:
        __word: The secret word. Cannot be accessed outside of
                this class.
        guessed_letters: The list of letters the player has
                         already guessed
        letters_left: Keeps track of how many letters are left blank in
                      the SecretWord.
        guessed_wrong: The number of letters the player has
                       guessed wrong.

    """
    def __init__(self):
        """
        Construct the object with necessary attributes.
        """
        pass

    def set_word(self):
        """
        Selects and returns a random word from the list.
        """
        # Create the list of words that will be picked from.

        # Select and return a random word from the list.
        pass

    def show_word(self):
        """
        Displays the current state of the secret word, with
        correctly guessed letters filled in.
        """

        # Reset 'letters_left' attribute to 0 in order to get
        # a fresh count.
        

        # Print each letter in the word that has already been
        # guessed. Leave letters that have yet to be guessed
        # as '_'.
        print("The word is...")
        
                
            # If the letter has not been guessed, print '_'
            # and add 1 to the 'letters_left'.
            pass

    def check_guess(self, guess):

        # Check if the player has already guessed the letter that
        # they entered.
        

        # Else...
        

            # If the letter the player guessed is not in the secret word, inform
            # the player and add to their 'guessed_wrong' count. Add
            # the guessed letter to the 'guessed_letters' list.
            
                
            # If the letter the player guessed is in the secret word,
            # inform the player. Add the guessed letter to the 
            # 'guessed_letters' list.
            pass
