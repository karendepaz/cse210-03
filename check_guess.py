from director import Director

class Check:
    #checks if guessed letter is in the word or not
    def __init__(self):
        self.guessed_letters = []
        return
        
    
    def check_letter(self, secret_word, guess):
        
        word_completion = '_' * len(secret_word)
        print(word_completion)
        
        if guess in secret_word:
            secret_word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(secret_word) if letter == guess]
            for index in indices:
                secret_word_as_list[index] = guess
            word_completion = "".join(secret_word_as_list)
            print()
            print(word_completion)
        else:
            print('loser')


    

    
    
