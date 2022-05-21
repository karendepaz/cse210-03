from jumper import Jumper
from director import Director
from check_guess import Check


director = Director()
jumper = Jumper()
check = Check()

word = director.random_word()
guess = director.make_guess()

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


