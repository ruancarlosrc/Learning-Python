"""
print("Odd or even!")
print("Please, type a number: ")
num = int(input())
result = num % 2
if result == 1:
    print("ODD!")
elif result == 0:
    print("Even!")
###
"""
print("type two numbers:")
num1 = int(input("Type the first number: "))
num2 = int(input("Type the seconde number: "))
if num1 > num2:
    print("The first number is bigger")
elif num2 > num1:
    print("The seconde number is bigger")
elif num1 == num2:
    print("The numbers are the same!")
dif = num1 - num2
print(f"The difference between the numbers are {dif}")
