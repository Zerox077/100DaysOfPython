# 10 April 2025
print("Welcome to the tip calculator")

bill_amount = float(input("What was the total bill: $ "))
tip_percent = float(input("How much tip would you like to give: 10, 12 or 15"))
number_of_people = int(input("How many people would you like to split it with: "))

total_bill = (bill_amount * (tip_percent / 100 ) ) + bill_amount

split_amount = float(round(total_bill / number_of_people, 2))

print(f"Each person should pay: ${split_amount}")