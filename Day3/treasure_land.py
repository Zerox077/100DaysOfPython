print("Welcome to treasure island !\nYour mission is to find the treasure !")

walk = input("Do you want to go left or right? Type L or R ")

if walk == "R":
    print("Game Over")
elif walk == "L":
    swim = input("Do you want to swim or wait? S or W")
    if swim == "S":
        print("Game over")
    elif swim == "W":
        door = input("Do you want to choose red or blue door ? R or B or Y")
        if door == "R":
            print("Game over")
        elif door == "B":
            print("Game over")
        else:
            print("You won")
    else:
        print("Invalid Choice")
else:
    print("Invalid Choice")


