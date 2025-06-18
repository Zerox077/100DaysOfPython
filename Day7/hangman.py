import random
from word_list import word_list


chosen_word = random.choice(word_list)
print(chosen_word)
game_over = False
while not game_over:

    guess = input("Guess a letter: ").lower()
    print(guess)

#
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

placeholder = ""


#     for letter in chosen_word:
#         while placeholder != "_":
#             if letter == guess:
#                 placeholder += letter
#         else:
#                 placeholder += "_"
#
# print(placeholder)
#
# # if "_" not in placeholder:
#

