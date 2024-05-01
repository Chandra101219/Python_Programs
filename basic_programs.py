# #Addition of two number
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# sum = num1+num2
#
# print(f"sum of: {num1} and {num2} is {sum}")
#
# #division of two numbers
# num3 = int(input("Enter num3: "))
# num4 = int(input("Enter num4: "))
# div = num3/num4
#
# if num4==0:
#     print("Error: division with zero is not allowed")
# else:
#     print(f"division of: {num3} and {num4} is {div}")
#
# #area of the triangle
# # base, height and area = 0.5*base*height
#
# base = float(input("Enter base of the triangle: "))
# height = float(input("Enter height of the triangle: "))
# area = 0.5*base*height
#
# print("area of the triangle is: ",area)

# swapping of two numbers

# a = 5
# b = 6
# print(a,b) #5,6
# #without temporary variable
# a,b = b,a
# print(a,b) #6,5 swapped
# #by introducing a temerory variable
#
# c = a
# a = b
# b = c
# print(a,b) #agin swapped and 5,6
#
# #printing  random number
#
# import random
#
# print(random.randint(0,15))
#
#
# #converting kilometers into miles,meters and centimeters
#
# km = float(input("Enter number of kilometers: "))
#
# conv_miles = km/1.6093
# conv_meters = km*1000
# conv_cm = km*100000
#
# print(f"{km} kms equal to: {conv_miles} mi")
# print(f"{km} kms equal to: {conv_meters} m")
# print(f"{km} kms equal to: {conv_cm} cm")

# converting temperature from °F to °C and vice versa

# Farenheit = float(input("temerature in Farenheit: "))
# conversion = (Farenheit-32)*5/9
# print(Farenheit,"°F equals to: ",conversion, "°C")
# #°C to °F
# Celsius = float(input("temerature in Farenheit: "))
# conversion = (Celsius+32)*9/5
# print(Celsius,"°C equals to: ",conversion, "°F")

# printing calender of a selected month in a selcted year

# import calendar
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# cal = calendar.month(year, month)
# print(cal)

# check weather a number is positive or negative

# number = int(input("Enter a number: "))
#
# if number>0:
#     print(number,"is positive number")
# elif number==0:
#     print("number is zero")
# else:
#     print(number,"is negative number")

# check weather number is even or odd

# number = int(input("Enter a number: "))
#
# if number%2==0:
#     print("given number is even numbr")
# else:
#     print("given number is odd numbr")


# print generates the numbers in fibanocci series
# n = int(input("Enter the number of terms needed "))
# a, b = 0, 1
# count = 0
# list = []
# # print(a,b,end=" ")
# while count < n:
#     print(a)
#     nth = a + b
#     # update values
#     a = b
#     b = nth
#     list.append(a)
#     count += 1
#
# print(list)
# print(len(list))
# print(list[2])
# print(list[-1])


# Python Program to find the fibonacci series using recursion

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# n = int(input("Enter number of terms:"))
# print("Fibonacci sequence:")
# for i in range(n):
#     print(fibonacci(i))

list1 =[]
for i in range(10):
    list1.append(i)
print(list1)
print(len(list1))
#retriving the list elements
i=0
while i < len(list1):
    print(list1[i])
    i+=1
#retriving the list elements for loop
for i in list1:
    print(i)

list1.append(5)
print(list1)

list1[4] = 15
print(list1)

del list1[-1] #using position of the element
print(list1)

list1.remove(15)#using element
print(list1)

# list1.reverse()
# print(list1)

reversed = []
i = len(list1)-1
while i>=0:
    print(list1[i])
    reversed.append(list1[i])
    i-=1
print(reversed)