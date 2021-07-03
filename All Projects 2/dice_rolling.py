

import random

# def roll_dice():

#     x = random.randint(1,6)
#     print(x)



# def guess_dice(guess):

#     random_generated_dice = random.randint(1,6)
#     guessed = guess

#     while guessed != random_generated_dice:
#         guessed = int(input('guess again: '))

#         if guessed == random_generated_dice:
#             print('You guessed it!')


        
def max_dice(min, max, guess):

    generated_dice = random.randint(min, max)

    if min > guess:
        question = f"Your guess is lower than your provided min which is {min}"
        print(question)

        guess = int(input('Please, choose a number that corresponds to your range'))
        print(guess)

    elif guess > max:
        question = f"Your guess is higher than your provided max which is {max}"
        print(question)
        
        guess = int(input('Please, choose a number that corresponds to your range'))
        print(guess)

    guessed = guess

    while guessed != generated_dice:

        if guessed > generated_dice:
            guess = int(input(f'Go lower: '))
            guessed = guess
        elif guessed < generated_dice:
            guess = int(input(f'Go higher: '))
            guessed = guess
        
    print(f"You guessed it.. ")



