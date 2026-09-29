print()
print("text here")
print("Divya Joshi",63)
print("Divya Joshi",63,6+9)
print("Divya Joshi",63,3+6,True)
print("Divya Joshi",63,3+6,False,3<6)
print("Divya Joshi",63,3+6,False,3<6,type(3+4j))

age=19
print("Vote" if age >=18 else "Not Vote")

print('''
---------------------------
  Welcome to Cherry Hotel
---------------------------
        Menu Card
S.No.     Item       Rate
1         Samosa      15
2         Jalebi      30
3         Poha        15
----------------------------------------
Please choose the item no. for order :
-----------------------------------------
''')


a = 6
pi = 3.14
complex = 3+5j
print (f'int is {a} \nfloat is {pi} \nand complex is {complex}')


what_i_am = True
print(what_i_am)

what_inside_me = None
print(what_inside_me)

name = 'Divya Joshi'
print(f'My name is {name}')

arr = [1,2,3,4]
print(arr)

arr1=[1,2.4,'HELLO']
print(arr1)

a1=[1,2,3,[5,6,7]]
print(a1)
print(a1[3])
print(a1[3][1])

ar = (1,2,3,4,5)
print(ar)


s1 = { 1,1,2,2,2,3,3,}
print(s1)

d1 = {
    'Fruit' : ["Apple","Mango"],
    'Climate' : ["Cold","Simmer"],
    'Price' : [120,80],
    'State' : ["kashmir","MP"]
}
print(d1)
print(d1['Fruit'][0])

a=6
print(f'whats inside {a} and datatype {type(a)}')

a=6.3
print(f'whats inside {a} and datatype {type(a)}')

a=[]
print(f'whats inside {a} and datatype {type(a)}')

a={'name':'divya'}
print(f'whats inside {a} and datatype {type(a)}')

a=6
b=6
c=6
d=a*1
a=10
print(f'a={a}and address is {id(a)}')
print(f'b={b}and address is {id(b)}')
print(f'c={c}and address is {id(c)}')
print(f'd={d}and address is {id(d)}')
print(f'a={a}and address is {id(a)}')


name=input('Enter your name')
print(f'Name is {name}')
roll = int(input('Enter roll number'))
print(roll)
marks=float(input('Enter marks'))
print(marks)
subject=eval(input('Enter subjects'))
print(subject)