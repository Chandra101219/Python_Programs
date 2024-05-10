List = [2, 5, 8, 7, 5, 4]
#using sum() function
x = sum(List)
print(x)

#by running loop over list
sum = 0
for i in range(len(List)):
    sum += List[i]
print(sum)


#sum of digits in a number

def sumofDigits(n):
    if n < 10:
        return n
    sum = 0
    while n > 0:
        sum += n % 10      #which adds reminder of each itration
        n = n // 10        #which elemenates the last digit of each iteration
    return sum


n = int(input("Enter a number: "))
sumofdigits = sumofDigits(n)
print("sum of digits of a number: ", sumofdigits)


#Min.no.of flips

def minNoofFlipe(pwd):
    flips = 0
    for i in range(0, len(pwd), 2):
        if pwd[i] != pwd[i + 1]:
            flips += 1
    return flips


result = minNoofFlipe("01010110")
print(result)

result = minNoofFlipe("00010011")
print(result)

result = minNoofFlipe("11010010")
print(result)
