# print(9/0)

# use try except block 

try:
    print(9/0)
except ZeroDivisionError:
    print("you can't divide by zero")


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)
    
while True:
    number_one = input("\n number one: ")
    if number_one == "q":
        break
    number_two = input("\n number two: ")
    if number_two == "q":
        break
    try:
        answer = int(number_one) / int(number_two)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
        


    