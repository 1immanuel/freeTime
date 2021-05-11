import random
run = True
game = True
chances = 5
magic_number = random.randint(1, 10)



print('Welcome. \nGuess a number: ')
number = int(input())

while game == True:
    if number != magic_number:
        chances = chances - 1
        number = int(input('Guess again: '))
    elif number == magic_number:
        print('Genius!!')
        game = False
    else:
        if chances == 0:
            game = False
            print('Better luck next time.')
else:
    if game == False:
        print('Thanks for playing.')

        
        
    


