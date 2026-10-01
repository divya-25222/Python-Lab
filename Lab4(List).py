l1=[] #empty list
l2=[1,2,3,4,5] #list with elements
print(l1,l2)

print(2 in l2)
print(2 not in l2)

#Iterate each element
for a in l2:
    print(a)

for a in range(0, len(l2)): #BY POSITION
    print(l2[a])

#OPEARTION ON LIST
#ADDITION
l1=[4,5,6,7,8]
l3=l1+l2
print(l3)
l4=l2+l1
print(l4)

#MULTIPLICATION
l5=l2 * 3
print(l5)

l1.pop()
print(l1)

#APPEND
l1.append(50)
print(l1)

#REMOVE
l1.remove(5)
print(l1)

#COUNT
l2=[1,2,3,4,4,4,5,6]
print(l2.count(4))

#MAXIMUM AND MINIMUM
print(max(l2))
print(min(l2))

#SORTING
print(l2.sort())

#LIST COMPREHENSION
l1=[5,6,7,8,9] #NORMAL METHOD
l2=[]
for a in l1:
    l2.append(a*a)
print(l2)

#SQUARE OF EACH ELEMENT USING LIST COMPREHENSION
my_list=[a*a for a in l1]
print(my_list)

#SQUARE OF EVEN NUMBERS ONLY
my_list=[a*a for a in l1 if a%2==0]
print(my_list)

#SLICING list[start:stop:step]

list=[10,20,30,40,50,60]
print(list[-2])
print(list[1:4])     #start=1 stop=3
print(list[:5])      #start=0 stop=4
print(list[3:])      #start=3 stop=last
print(list[1:5:2])   #star=1 stop=4 step=2
print(list[::-1])    #will reverse the elements
print(list[-6:-2])
print(list[-2:-6])   #Can't read output empty list
print(list)



#DATA STRUCTURE QUESTION

list=[10,20,30,40,50,60]
li1=list[:2:-1]
print(li1)
li2=list[:3]
print(li2)
li3=li2 + li1
print(li3)

l=list[0:3] + list[3:] [::-1]
print(l)

k=int(input("Enter k = "))
k=len(list)%k
l2=list[:k]+list[k:][::-1]
print(l2)

lst = [10, 20, 30, 40, 50, 60]
k = 3
output = lst[-k:] + lst[:-k]
print(output)

#TO REMOVE DUPLICATE VALUES IN A LIST
lst = [10, 20, 20, 30, 40, 40, 50, 50]
new_list = []
for i in lst:
    if i not in new_list:
        new_list.append(i)
print(new_list)

#TO DISPLAY OCCURING ONLY ONCE
list1=[10,10,20,20,30,30,40,40,40,50,50,60]
for i in list1:
    if list1.count(i) == 1:
        print(i)

lt1=[10,10,20,20,30,30,40,40,40,50,50,60]
m_list=[x for x in lt1 if lt1.count(x)==1]
print(m_list)

