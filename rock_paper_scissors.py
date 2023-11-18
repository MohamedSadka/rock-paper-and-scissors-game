# start the game
# ask the user to choose between (r , p , s)
# ask the computer to choose between them randomly
# if user == pc => a tie
# elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or  (user == 's' and pc == 'p') => you won 
# else (you lose)

import random

choices = {'r', 'p', 's'}

user_choice = input('Choose "r" for rock, "s" for scissors, or "p" for paper: ').lower()
pc_choice = random.choice(('r', 'p', 's'))

if user_choice in choices:
    print('Your choice is ' + user_choice)
    print('PC choice is ' + pc_choice)

    if user_choice == pc_choice:
        print("It's a tie")
    elif (user_choice == 'p' and pc_choice == 'r') or (user_choice == 'r' and pc_choice == 's') or (user_choice == 's' and pc_choice == 'p'):
        print('You win')
    else:
        print("You lose")
else:
    print("Choose a letter between (r, s, p) to make sense")
