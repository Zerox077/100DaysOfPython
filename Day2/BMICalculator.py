'''
The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
bmi is equal to the person's weight divided by the person's height squared.
Convert this sentence into code on line 6.
'''

weight = 84
height = 1.65

bmi = weight / (height ** 2)

print(bmi)

#round the number to whole number
print(round(bmi))

# print to two decimal points
print(round(bmi, 2))

score = 0
height = 2.2
is_winning = True

print(f"Your score is = {score}, \nyour height is {height}, \nyou are winning is {is_winning}")