# Import the necessary classes.
from secret_word import SecretWord
from jumper import Jumper

class Game:
    """
    The game that the player is currently playing.

    The responsibility of the Game is to have a SecretWord and
    a Jumper, to keep track of the letters that they player
    has guess, to keep track of the number of guesses that the
    player has gotten wrong, and whether or not the game is over.

    Attributes:
        secret_word: The SecretWord of this game.
        jumper: The Jumper of this game.
        game_over: A Boolean variable that tracks whether or
                   or not the game has ended.

    """
    def __init__(self):
        """
        Construct the object with necessary attributes.
        """
        pass

    def show_all(self):
        """
        Displays the current state of the Game's SecretWord and
        Jumper objects.
        """
        # Call the Jumper's 'show_jumper' method and the
        # SecretWord's 'show_word' method.
        pass
