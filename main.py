     #importing random module
import random

     #Correct Guess Number
guess_number=9
user_input=int(input('Enter guess a number(1-20)'))
if user_input==guess_number:
    print('Guesser was correct')
else:
    print('Guesser was wrong')   

# abc=random.randint(1, 10)
# print(abc)