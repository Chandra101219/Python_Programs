
rows = int(input("Enter no of rows: "))

#sqaure pattern
for i in range(rows):
    for j in range(rows):
        print("*", end=' ')
    print()


#right angled Trianglular pattern
for i in range(rows):
    for j in range(i+1):
        print("*", end=' ')
    print()

#Inverted right angled Trianle

for i in range(rows):
    for j in range(rows-i):
        print("*", end=' ')
    print()

#Reversed inverted right angled Triangle

for i in range(rows):
    for j in range(i):
        print(" ", end=' ')
    for k in range(i,rows):
        print("*",end=' ')
    print()
#Reversed right angled Triangle
for i in range(rows):
    for j in range(i,rows-1):
        print(" ", end=' ')
    for k in range(i+1):
        print("*",end=' ')
    print()

#Triangle
for i in range(rows):
    for j in range(i,rows-1):
        print(" ", end=' ')
    for k in range(i):
        print("*",end=' ')
    for x in range(i+1):
        print("*", end=' ')
    print()

#Inverted Triangle

for i in range(rows):
    for j in range(i):
        print(" ", end=' ')
    for k in range(i,rows):
        print("*",end=' ')
    for x in range(i,rows-1):
        print("*", end=' ')
    print()

#rhombus
for i in range(rows-1):
    for j in range(i,rows-1):
        print(" ", end=' ')
    for k in range(i):
        print("*",end=' ')
    for x in range(i+1):
        print("*", end=' ')
    print()
for i in range(rows):
    for j in range(i):
        print(" ", end=' ')
    for k in range(i,rows):
        print("*",end=' ')
    for x in range(i,rows-1):
        print("*", end=' ')
    print()

#Pyramid
"""    * 
      * * 
     * * * 
    * * * * 
   * * * * * """

for i in range(rows):
    for j in range(rows-i-1):
        print(" ", end='')
    for k in range(i+1):
        print("* ",end='')
    print()

#Invrted pyramid
for i in range(rows):
    for j in range(i):
        print(" ", end='')
    for k in range(i,rows):
        print("* ",end='')
    print()



for i in range(rows):
    num = 0
    for j in range(rows):
        num+=1
        print(num, end=' ')
    print()


o_num = 0
for i in range(rows):
    num = o_num
    for j in range(rows):
        o_num+=1
        num+=1
        print(num, end=' ')
    print()


o_num=0
for i in range(rows):
    num = o_num
    for j in range(i+1):
        o_num += 1
        num += 1
        print(num, end=' ')
    print()
