#Print a number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Entered Number is Even")
else:
    print("Entered Number is Odd")

#Even or Odd using List

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

even = []
odd = []
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#number is positve,negative or Zero

num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


#Even or Odd using function

def evenOdd(lst):
    even_count = 0
    odd_count = 0

    for i in lst:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


lst = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even, odd = evenOdd(lst)
print("Even count is: {} Odd count is: {} ".format(even, odd))


# Lambda function

lst = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# filter(function,list)
evens = list(filter(lambda n:n%2==0 ,lst))
odds = list(filter(lambda n:n%2!=0 ,lst))
print("lst of even numbers",evens)
print("lst of odd numbers",odds)

#map(function,list)

squares = list(map(lambda n:n*n,evens))
print("lst of squares of even numbers",squares)