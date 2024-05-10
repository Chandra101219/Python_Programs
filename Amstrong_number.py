def isAmstrongNumber(num):
    original_num = num
    num_digits = len(str(num))
    sum = 0

    while num > 0:
        digit = num % 10
        sum += digit ** num_digits
        num = num // 10
    print(sum)

    if original_num == sum:
        print("Number is armstrong number")
    else:
        print("Number is not an armstrong number")


num = int(input("Enter a number: "))
isAmstrongNumber(num)


#without defining function
num = 15
original_num = num
num_digits = len(str(num))
sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit ** num_digits
    num = num // 10
print(sum_of_digits)

if original_num == sum_of_digits:
    print("Number is armstrong number")
else:
    print("Number is not an armstrong number")
