print()
print('text',6+3,6>5,type(3.14))
print('vote' if 19>18 else 'you cannot')
print([i for i in range(0,5)])


name='Divya'
age=19
salary=48000
print('My name is',name,'and my age is',age,'with salary',salary)
print(f'My name is {name} and my age is {age} with salary {salary}')


print('''
--------------------------------------------------------------------
                        PNB BANK
--------------------------------------------------------------------
1--> ACCOUNT DETAILS
2--> ACCOUNT BALANCE
3--> LAST 5 TRANSACTIONS
4--> CHEQUE BOOK ISSUE
5--> FEEDBACK
-------------------------------------------------------------------
''')


a=6
pi=3.14
c=3+4j
print(a,pi,c)

what_inside_me= None
print(what_inside_me)

what_i_am= True
print(what_i_am)

#LITERALS - STRING,LIST,TUPLE,SET,DICTIONARY
name="Divya Joshi"
print(name)

arr=[10,20,30,'HELLO',[2,3,4]]
print(arr)
print(arr[3])
print(arr[4][2])

tup= (10,20,30,'HELLO')
print(tup)

set = {1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4}
print(set)

dict = {'Fruit' : ['Apple','Mango'],
        'Climate' : ['Cold','Hot'],
        'Price' : [120,80]}
print(dict)
print(dict['Fruit'])
print(dict['Price'][1])


name=input('Write your name:')
print(name)
print(type(name))
roll=int(input("Enter your roll number:"))
marks=float(input("Enter marks:"))
subject=eval(input("Enter subject name:"))                    #tuple/list  by default tuple
print(roll)
print(marks)
print(subject)


#multiple condition parenthesis if not can go without the parenthesis if elif else proper indentation(4 spaces/1 tab) multiple if forcefully have to check everything

if 5>3:
    print('I will be executed')
if 5>2:
    print('What will come')
elif 5>3:
    print('Elif will be executed')
else:
    print('BYE')


age=int(input('Enter your age:'))

if age>=18:
    print('You can vote')
    if age>55:
        print('Senior Citizen')
    else:
        print('Youth Citizen')
        
elif age<=18 and age>0:
    print("You can't vote")
    
else:
    print("Invalid Age")
