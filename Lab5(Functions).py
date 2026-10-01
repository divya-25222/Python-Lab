#void function --> return
# non void function --> return
'''def function_name(parameter,...):
    statement
'''

def sum (a,b):   #a=10 b=20  arugument is given position wise
    sum=a+b
    print(sum)
    return sum

#main
result=sum(10,20)
print(sum(10,20))

result=sum(b=20,a=200)

def result(a,b):
    sum=a+b
    multi=a*b
    return sum,multi
r1=result(10,20)   #answer in tuple form
print(r1)
r1,r2=result(10,20)
print(r1)
print(r2)

def Employee(Emp_ID, Emp_Name):
    print(f'Employee ID: {Emp_ID} / Employee Name: {Emp_Name}')

Employee(Emp_Name='Divya', Emp_ID=101)


#* -- Multiple values (packing unpacking operator used when tuple or list form )
#No multiple * parameter def sum(*element,*values):
def sum(*element):
    sum=0
    for a in element:    #To iterate
        sum=sum+a
    return sum
r1=sum(1,20,30,40,50,60,70)
print(r1)


#ERROR
def error_log(first,*all):    #Take 1st element remaining will go in all, cannot declare a varilable after *all
    print(f'[{first}]',*all) 
error_log('2026-10-1','esp32 connection failed','time out')


#TAKING N NUMBER OF VALUES BUT THE OUTPUT SHOULD COME IN MINUS
def sum(*all,sign=1):
    sum = 0
    for a in all:
        sum = sum + a
    return sign * sum
r=sum(10,20,30,40,50,60,80,sign=-1)
print(r)
print(sum())


#TO CHECK WHETHER THE NUMBER IS PRIME NUMBER OR NOT
def prime(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
n = int(input("Enter a number: "))
print(prime(n))

#** Didnt called dictionary but passed multiple values
def print_anything(**data):
    for key, value in data.items():
        print(f'{key} = {value}')
print_anything(Name='Divya Joshi')
print_anything(ID=101, E_Name='Divya Joshi', Company='TCS', Salary=10000000)


#What is lamda funtion - a function with name lambda and has only one expression
# mostly used -- map,filter and sort
#object = lambda p1,p2,...:expression

sum=lambda a,b: a+b
print(sum(10,20))

sqrt=lambda a: a*a
print(sqrt(5))

greater = lambda a,b : a if a>b else b
print(greater(25,20))

greater = lambda a, b, c: a if a > b and a > c else b if b > c else c
print(greater(25, 20, 30))

#SQRT of every element in the list
l1 = [10, 20, 30, 40, 50, 60]
l2 = list(map(lambda n: n*n, l1))   #mapping with l1   or pipelining
print(l2)         


#FILTER  will only include the useful things
l1=[1,2,3,4,5,6]
l2=list(filter(lambda n:n%2==0,l1))
print(l2)

#List with elements greater than 50
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
l2 = list(filter(lambda n: n > 50, l1))
print(l2)
