import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers =['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['~', '@', '#', '$', '%', '^', '&', '(', ')']

start_pos = 0
char = ""
nr_letters = int(input("How many letters do you want in your password: "))
nr_numbers = int(input("How many numbers do you want in your password: "))
nr_symbols = int(input("How many symbols do you want in your password: "))

for letter in range(start_pos, nr_letters):
    char+=letters[letter]

for letter in range(start_pos, nr_numbers):
    char+=numbers[letter]

for letter in range(start_pos, nr_symbols):
    char+=symbols[letter]



pass_list = list(char)
print(f"{pass_list}")

random.shuffle(pass_list)
shuffled_string = "".join(pass_list)
print(f"shuffled string: {shuffled_string}")
