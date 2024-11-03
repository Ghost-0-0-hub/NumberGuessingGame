import random

secret_number = random.randint(0,11)
user = int(input('Guess a Number between 0 - 11: '))

if user != secret_number:
    while user!= secret_number:
        user_input = int(input('Guess Again: '))
        if user_input == secret_number:
            print('you win!')
            break
else:
    print('you win!')
