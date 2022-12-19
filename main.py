from random import randint
print('when you want to stop, enter "q".')
game = True
score = 0
while game:
    user_guess = input('Guess a number from 1 to 10:  ')
    number = randint(1,10)
    if user_guess == 'q':
        game = False
        print(f'Game over, your score is {score}')
    elif int(user_guess) == number:
        score += 10
        print('Good Job!')
        print(f'Your score is {score}')
    else:
        print('Wrong! the number was: ', number)


