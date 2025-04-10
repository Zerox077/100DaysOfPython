print("Welcome to Pizza deliveries !!")

size = input("What size of pizza do you want ? S = $15, M = $20 or L: $25 ")
pepperoni = input("Do you want pepperoni on your pizza? \nSmall: $2\nMedium or large: $3 \nY or N: ")
extra_cheese = input("Do you want extra cheese on your pizza ? +$1 for any size Y or N: ")

total_price = 0

if size == "S":
    total_price =  15
elif size == "M":
    total_price = 20
elif size == "L":
    total_price = 25
else:
    print("Invalid Choice")
    print("Thank you for visiting")

if pepperoni == "Y":
    if size == "S":
        total_price += 2
    else:
        total_price += 3

if extra_cheese =="Y":
    total_price +=1

print(f"You pay : {total_price}")




