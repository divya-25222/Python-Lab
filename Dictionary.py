#Dictionary
#key:value
#key --> string/variable
#value --> any


d1 = {}  #Empty

d2 = {'Name': 'Divya Joshi',
    'Dept': 'CSE',
    'Place': 'Indore',
    'Salary': 45000,
    }  

'''d2 = {'Name': 'Divya Joshi',
    'Dept': 'CSE',
    'Place': 'Indore',
    'Salary': 45000,
    'Place': 456}  '''                        #If key is same then it will overwrite
d2['Age']=20     #To ADD
d2['Salary']=50000  #To UPDATE
print(d2)
print(len(d2))    


d2 = {'Name': ['Divya Joshi', 'Jay'],
    'Dept': ['CSE', 'AIDS'],
    'Place': ['Indore', 'Mumbai'],
    'Salary': [45000, 50000]}
print(d2['Name'][1])

for a in d2.keys():
    print(a)                

for b in d2.values():
    print(b[0])
    print(b[1])   #To differentiate

for a,b in d2.items():
    print(a)
    print(b)