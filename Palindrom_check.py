num = int(input("Enter  number: "))
original_num = num
reverse_num = 0
while num != 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10
    print("reverse after each iterarion: ",reverse_num)
    print("num after each iterarion: ",num)
print(reverse_num)

if reverse_num == original_num:
    print("Number is Palindrome")
else:
    print("Number is not a Palindrome")



#numb we can take  number at runtime
#num is assigned to a original_num which is a temp var as num is not same after through a loop
#reverse_num is intially ero after through the loop reversed number stored in it