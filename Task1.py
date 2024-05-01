#1
# pylist = [1,2,3,4,[5,6,7,8,[9,10,11,12,[13,14,15,16]]]]
#
# print(pylist)
# print(pylist[4][4][4][3])

#2

# r = lambda q: q * 2
# s = lambda q: q * 3
# x = 3
# x = r(x)    #x=3 & q=3 & 3*2=6 returns 36 x=6
# x = s(x)    #x=6 & q=6 & 6*3=18 returns x=18
# x = r(x)    #x=18 & q=18 & 18*2=36 returns x=36
# print(x,x)  #as x=36 so final output(36,36)

#3
# var1 = 'Hello CodingMasters!'
# var2 = "CodingHYD"
# print("var1[0]: ", var1[0]) #H
# print("var2[1:5]: ", var2[1:5])#odin

#4 What is the value of this expression: bin(10-2)+bin(12^4)

# x=bin(10-2)+bin(12^4) #concatenate the strings of both result (10-2) 8 the bin expr is 0b1000 and same with (12^4)
#
# print(x) #0b10000b1000
#
# print(oct(80))

#5
# print(['hello','morning'][bool('')]) #False'' returns 0 #True '1 o 0 or any value' returns 1
#6

# def count_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     vowel_count = 0
#
#     for char in input_string:
#         if char in vowels:
#             vowel_count += 1
#
#     return vowel_count
#
# input_string = input("Enter a string: ")
# num_vowels = count_vowels(input_string)
# print("Number of vowels:", num_vowels)

#no.of consonents in a String
# def count_consonents(input_string):
#     vowels = "aeiouAEIOU"
#     space = " "
#     consonents = 0
#
#     for char in input_string:
#         if char not in vowels and char not in space:
#             consonents += 1
#
#     return consonents
#
# input_string = input("Enter a string: ")
# num_consonents = count_consonents(input_string)
# print("Number of consonents:", num_consonents)

#7
# def count_digits_and_letters(input_string):
#     digit_count = 0
#     letter_count = 0
#
#     for char in input_string:
#         if char.isdigit():
#             digit_count += 1
#         elif char.isalpha():
#             letter_count += 1
#
#     return digit_count, letter_count
#
#
# input_string = input("Enter a string: ")
# num_digits, num_letters = count_digits_and_letters(input_string)
# print("Number of digits:", num_digits)
# print("Number of letters:", num_letters)

#8
# def is_prime(number):
#     if number <= 1:
#         return False
#     if number <= 3:
#         return True
#
#     if number % 2 == 0 or number % 3 == 0:
#         return False
#
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 6
#
#     return True
#
#
# input_number = int(input("Enter a number: "))
# if is_prime(input_number):
#     print(input_number, "is a prime number.")
# else:
#     print(input_number, "is not a prime number.")

#9

# for i in range(10):
#  if i == 5:
#     break
#  else:
#     print(i)
# else:
#  print("Here")

#10
# print('my_string'.isidentifier())

#11

# l=[2, 3, [4, 5]]
# l2=l.copy()  # copy the list and not it's reference loction so one list changes are not reflected to another
# l2[0]=88
# l[1] = 25
# print(l)
# print(l2)

#12

# l1=[10, 20, 30]
# l2=[-10, 20, -30]
# l3=[x+y for x, y in zip(l1, l2)]
# print(l3)

#13

# l1=[1,2,3]
# l2=[4,5,6]
# l3=[7,8,9]
# for x, y, z in zip(l1, l2, l3):
#     print(x, y, z)

#14
# a={}
# print(a.fromkeys([1,2,3],"check"))

#15
# a={1,2,3}
# b=a.add(4)
# print(b)

#print([[i+j for i in "abc"] for j in "def"])
# def is_palindrome(number):
#     original_number = number
#     reversed_number = 0
#
#     while number > 0:
#         digit = number % 10
#         reversed_number = reversed_number * 10 + digit
#         number //= 10
#
#     return original_number == reversed_number
#
#
# input_number = int(input("Enter a number: "))
# if is_palindrome(input_number):
#     print(input_number, "is a palindrome.")
# else:
#     print(input_number, "is not a palindrome.")



# def print_inverted_pyramid(rows):
#     for i in range(0, rows, 1):
#         print(" " * (rows - i) + "*" * (2 * i - 1))
#
# input_rows = int(input("Enter the number of rows for the inverted pyramid: "))
# print_inverted_pyramid(input_rows)

#while loop
# num = 1
# while num<=10:
#     print(num)
#     num+=1
#
# num = 10
# while num>=1:
#     print(num)
#     num-=1
#
# #for loop
#
# for i in range(1,11):
#     print(i)

# a=int(input("Enter the first number of the series "))
# b=int(input("Enter the second number of the series "))
# n=int(input("Enter the number of terms needed "))
# print(a,b,end=" ")
# while(n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")
#     n=n-1

nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
 # update values
        n1 = n2
        n2 = nth
        count += 1
