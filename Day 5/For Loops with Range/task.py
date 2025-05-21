# for number in range(1, 11, 3):
#     print(number)

# total_sum_of_numbers = 0
# for number in range(1, 101):
#     total_sum_of_numbers += number
# print(total_sum_of_numbers)

# number = 0
# for number in range(1, 101):
#     print(number)
#     if number % 3 == 0:
#         print("Fizz")
#         if number % 5 == 0:
#             print("Buzz")
#         elif number % 3 and number % 5:
#             print("FizzBuzz")
# else:
#     print(number)

number = 0
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)