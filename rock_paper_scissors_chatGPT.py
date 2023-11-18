
import random

choices = {'r', 'p', 's'}

while True:
    user_choice = input('Choose "r" for rock, "s" for scissors, or "p" for paper (or type "quit" to exit): ').lower()
    
    if user_choice == 'quit':
        print("Thanks for playing! Goodbye.")
        break  # Exit the loop if the user chooses to quit

    if user_choice in choices:
        pc_choice = random.choice(('r', 'p', 's'))
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
