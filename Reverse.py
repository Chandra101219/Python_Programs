#Rverse a number
#num = int(input("Enter a number: "))

#using while loop
# reversed_num = 0
#
# while num != 0:  #condition
#     digit = num % 10  #to get the reminder of the number
#     reversed_num = reversed_num * 10 + digit  #to add the reminde*10 and digit and stor it in the reversed_num
#     num //= 10  #increment/decrement
#
# print("Reversed Number: " + str(reversed_num))

#by using function
# def reverseNumber(num1):
#     reverse_num = 0
#     while num1 != 0:
#         digit = num1 % 10
#         reverse_num = reverse_num * 10 + digit
#         num1 //= 10
#     return reverse_num
#
# output = reverseNumber(1254)
# print(f"reversed number is: {output}")

#Reverse a String
#method1
string = "wednesday"
reversed_string = ""

for i in range(len(string),0,-1):
    reversed_string += string[i-1]

print(reversed_string)

#method2
reversed = ""
for i in string:
    reversed = i + reversed
print(reversed)

#function to reverse a string

# String = "Friday"
# reversed_string = ""
# def reverse_string():
#     global reversed_string
#     for i in range(len(String), 0, -1):
#         reversed_string += String[i - 1]
#     return reversed_string
#
# rs = reverse_string()
# print(rs)
