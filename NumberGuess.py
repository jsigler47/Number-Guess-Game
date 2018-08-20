import random

lowRange = 1 # Low range for secret number.
hiRange = 20 # High range for secret number.
numGuesses = 7 # Number of guesses before losing + 1.

number = random.randint(lowRange,hiRange)
print('I am thinking of a number from 1 to 20.')

for guesses in range(1,numGuesses):
    print('Take a guess, you have ' + str(7 - guesses) + ' guesses remaining.')
    guess = int(input())

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

if guess == number:
    print('Correct! You guessed it in ' + str(guesses) + ' guesses!')
else:
    print('Nope. The number I was thinking of is ' + str(number) + '.')
