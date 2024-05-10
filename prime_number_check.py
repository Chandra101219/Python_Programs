# given number is prime or not
def isPrimeNumber(n):
    if n <= 1:
        return f"{n} is not a prime number"
    for i in range(2, n):
        if n % i == 0:
            return f"{n} is not a prime number"
        else:
            return f"{n} is a prime number"


n = int(input("Enter a number: "))
output = isPrimeNumber(n)
print(output)

#no of prime numbers available till num
def noOfPrimeNumbers(n):
    if num <= 1:
        print("no prime numbers")
    list = []
    for n in range(1,num):
        if n>1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                print(n)
                list.append(n)
    print(list)
num = int(input("Enter a number: "))
noOfPrimeNumbers(n)


