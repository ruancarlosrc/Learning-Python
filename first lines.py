
print("Hello Word!")
print("*" * 10)
###
print("Type a number!")
number = input()
print("You wrote: %s " % number)
###
number = int(input("Type a number: "))
print(number)
###
decimal_num = float(input("Type a decimal number: "))
print("You wrote: %s " % decimal_num)
###
print("Type 3 numbers to make a sum: ")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
response = (num1+num2+num3)
print(f"The result is: {response}")
###
print("Type a number to see the square root: ")
number = float(input())
result = number ** 0.5
print(f"The result is {result}")
###
print("Type a number: ")
number = float(input())
result = number / 5
print(f"The fifth part of this number is: {result}")
###
print("Fahrenheit conversor")
print("*" * 20)
print("Type the Celsius temperature: ")
celsius = float(input())
fahre = celsius * (9.0/5.0)+32.0
print(f"The temperature is {fahre}")
###
print("Celsius converter")
print("*" * 17)
print("Type the Fahrenheit temperature:")
fahre = float(input())
celsius = 5.0 * (fahre - 32.0) / 9.0
print(f"The temperature is {celsius}")
###
print("Kelvin converter")
print("*" * 16)
print("Type the Kelvin temperature")
kelvin = float(input())
celsius = kelvin - 273.15
print(f"The temperature is {celsius}")
###
print("Miles converter")
print("If you use the mile system , this will help you in the next conversor!")
print("Type the speed in miles:")
ml = float(input())
km = 1.61 * ml
print(f"The speed in kilometers is {km} per second")
###
print("Kilometers per second to meters per second")
print("Type the kilometer")
km = float(input())
ms = km/3.6
print(f"The speed is {ms} per second")
###
