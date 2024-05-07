#sum of squares of n numbers
# def sumofSquares(n):
#     if n<0:
#         return -1
#     else:
#         sum = 0
#         list = []
#         for i in range(1, n):
#             square = i * i
#             sum = sum + square
#             print(sum)
#             list.append(sum)
#         print(list)
#         return sum
#
#
# sumofsquares = sumofSquares(5)
# print(sumofsquares)

#sum of squares of numbers in array

from array import *


# def sumofSquares(array):
#     sum = 0
#     for i in array:
#         square = i * i
#         sum = sum + square
#         print(sum)
#     return sum
#
# array = array('i',[1,2,3,4,5,6])
# sumofsquares = sumofSquares(array)
# print(sumofsquares)


#element in array has greater number than the giben number

def checktheNumber(n, array):
    if not len(array):
        return False

    for i in array:
        if i > n:
            return True

    return False

n=2
# n = int(input("Enter a number: "))
array = array('i', [])
number = checktheNumber(n, array)
print(number)
