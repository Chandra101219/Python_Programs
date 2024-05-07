def fact(n):
    if n < 0:
        return "undefined"
    if n == 0:
        return 1
    else:
        f = 1
    for i in range(1, n + 1):
        f = f * i
        print(f)
    return f


n = int(input("Enter a number: "))
result = fact(n)
print(f"Factorail of {n} is: {result}")


# using recursion

def facto(n):
    if n == 0:
        return 1

    fact = n * facto(n - 1)
    return fact


result = facto(n)
print(f"Factorail of {n} is: {result}")
