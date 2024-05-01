#Bubble Sort
# from range(len(list)-1 to 0)
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):                 #i value is (i-1) each iteration as previous i value sorted already
            if list[j]  > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

list = [5,4,3,8,7,9,2,1]
sort(list) # function call with rgument as list

print(list)


# from range(0 to len(list)-1)
def sorta(list1):
    for i in range(len(list1)-1):
        for j in range(0,len(list1)-i-1):
            if list1[j]  > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp

list1 = [5,4,3,8,7,9,2,1,10,11]
sorta(list1) # function call with rgument as list
print(list1)

#Selection Sort

def sort(list):
    for i in range(len(list)):
        minpos = i
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp


list = [5, 4, 3, 8, 7, 9, 2, 1]
sort(list)  # function call with argument as list
print(list)
