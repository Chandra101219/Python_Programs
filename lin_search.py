pos = 0

# #declaring the function using while loop

def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals() ['pos'] = i
            return True
        i += 1
    return False

# #declaring the function using for loop
def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10


if search(list, n):
    print("Found position of n at: ", pos)
else:
    print("not found")
#


