# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
    # print("You can ride the rollercoaster")
# else:
    # print("Sorry you have to grow taller before you can ride.")
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal")
elif bmi >= 25 and bmi < 30:
    print("overweight")
elif bmi >= 30:
    print("obese")