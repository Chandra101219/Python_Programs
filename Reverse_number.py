num = int(input("Enter a number: "))

#using while loop
reversed_num = 0

while num != 0:  #condition
    digit = num % 10  #to get the reminder of the number
    reversed_num = reversed_num * 10 + digit  #to add the reminde*10 and digit and stor it in the reversed_num
    num //= 10  #increment/decrement

print("Reversed Number: " + str(reversed_num))

#by using function
def reverseNumber(num1):
    reverse_num = 0
    while num1 != 0:
        digit = num1 % 10
        reverse_num = reverse_num * 10 + digit
        num1 //= 10
    return reverse_num

output = reverseNumber(1254)
print(f"reversed number is: {output}")
