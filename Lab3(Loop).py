for i in range(0,10):
    print(i)
    
for i in range(1,10,2):
    print(i)
    
name="Divya Joshi"
for i in  name:
    print(i)

arr=[10,20,30,40,50,60]
for i in arr:
    print(i)

for i in 'divya joshi':
    print(i)

name="Divya Joshi"
for i in range(len(name)):
    print(name[i])

#To find the largest
num=int(input("Enter a number : "))
digit=str(num)
count=1
largest=1

for a in range(1,len(digit)):
    if int(digit[a])==int(digit[a-1])+1:
        count=count+1
    else:
        count=1
    if count>largest:
        largest=count
print(count)


#To conert 24 hours format into 12 hours format
#Case I - 00:00    O/P - 12:00AM
#Case II - 12:00    O/P - 12:00PM
#Case III - 24:00    O/P - INVALID   if hours<=24 or min>=60
#           25:60    O/P - INVALID
#Case IV - 00:26    O/P - 12:26AM
#Case V - 13:20    O/P - 1:26PM

h=int(input("Enter hour: "))
m=int(input("Enter minutes: "))

if h>=24 or m>=60:
    print("INVALID TIME")

elif h<12 and m<=60:
    print(f'12 : {m} AM')

else:
    if h==12:
        print(f'12 : {m} PM')
    else:
        print(f'{h-12} : {m} PM')


#NESTED FOR LOOP PATTERNS
for i in range(5):
    for j in range(5):
        if i== j or i>j:
            print('*',end=" ")# print everything in one line end
    print()


for i in range(5):
    for j in range(5):
        if i== j or i<j:
            print('*',end=" ")# print everything in one line end
    print()

size=int(input("Enter size: "))
for i in range (size):
    for j in range(size):
        if i==0 or j==0 or i==size-1 or j==size-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

#To print 8 

size = int(input("Enter size: "))

for i in range(size):
    for j in range(size):
        if (i == 0 or i == size//2 or i == size-1) and (j > 0 and j < size-1):
            print("*", end=" ")
        elif j == 0 or j == size-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#window
size = int(input("Enter size: "))

for i in range(size):
    for j in range(size):
        if i == 0 or i == size-1 or j == 0 or j == size//2 or j == size-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#CROSS PATTERN
size = int(input("Enter size: "))

for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#PYRAMID
size = int(input("Enter size: "))

for i in range(size):
    for j in range(size - i - 1):
        print(" ", end=" ")

    for j in range(2 * i + 1):
        print("*", end=" ")

    print()

#WHILE LOOP

sum=0
while True:
    num=int(input("Enter number: "))
    sum=sum + num

    if num==0:
        break
print(f'Sum = {sum}')


#TO PRINT A NUMBER TILL YOU GET SINGLE DIGIT

n = int(input("Enter number: "))
while n >= 10:
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    n = sum
print("Single digit:", n)
    
