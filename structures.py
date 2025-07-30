print("*" * 20)
print("Hello ;)")
###
print("Which number is bigger")
print("*" * 20)
print("Please type two numbers:")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
if num1 > num2:
    print(" The first number is the biggest.")
elif num2 > num1:
    print(" The second number is the biggest.")
else:
    print(" The numbers are the same! ")
###
print("Type a number:")
num = int(input())
if num >= 1:
    square = num ** 0.5
    print(f"The square root of {num} is {square}")
elif num <= 0:
    print("INVALID NUMBER!")
###
print("Type a number:")
num = int(input())
if num >= 1:
    square = num ** 0.5
    squared = num ** 2
    print(f"The square root of {num} is {square}")
    print(f"{num} squared is {squared}")
elif num <= 0:
    print("INVALID NUMBER!")
