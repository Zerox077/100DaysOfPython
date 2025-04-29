import random

rock ='''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''

paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' 

'''

scissor = '''

   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
'''


index_user_choice = int(input('What do you choose ? Type 0 for Rock, Type 1 for Paper or Type 2 for Scissors.'))

game_options = [rock, paper, scissor]
index_computer_choice = random.randint(0,2)

print(f'User\'s choice {game_options[index_user_choice]}')
print(f'Computer\'s choice {game_options[index_computer_choice]}')
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

if index_user_choice == 0 and index_computer_choice == 2:
    print("You win")
elif index_user_choice == 2 and index_computer_choice == 0:
    print("Computer wins")
elif index_user_choice == 2 and index_computer_choice == 1:
    print("You win")
elif index_user_choice == 1 and index_computer_choice == 2:
    print("Computer wins")
elif index_user_choice == 1 and index_computer_choice == 0:
    print("You win")
elif index_user_choice == 0 and index_computer_choice == 1:
    print("Computer wins")
elif index_user_choice == index_computer_choice:
    print("Draw")
else:
    print("No result")