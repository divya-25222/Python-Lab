print('Divya Joshi')
print('0863CS241063')

route = int(input('Enter the bus route number : '))

if route == 1:
    print('''
--------------------------------------------------
            BUSES ON THIS ROUTE
--------------------------------------------------
1. VRL
2. ORANGE TRAVELS
3. FLIXBUS
--------------------------------------------------
''')

    choice = input('Do you want to know the timing yes/no : ')

    if choice == 'yes':
        print('''
--------------------------------------------------
            BUSES TIMING ON THIS ROUTE
--------------------------------------------------
1. VRL                      10 AM 11 AM 2 PM
2. ORANGE TRAVELS           11 AM 12 PM 3 PM
3. FLIXBUS                  11 AM 12 PM 2 PM
--------------------------------------------------
''')

elif route == 2:
    print('''
--------------------------------------------------
            BUSES ON THIS ROUTE
--------------------------------------------------
1. VRL
2. ORANGE TRAVELS
3. FLIXBUS
--------------------------------------------------
''')

    choice = input('Do you want to know the timing yes/no : ')

    if choice == 'yes':
        print('''
--------------------------------------------------
            BUSES TIMING ON THIS ROUTE
--------------------------------------------------
1. VRL                      10 AM 11 AM 2 PM
2. ORANGE TRAVELS           11 AM 12 PM 3 PM
3. FLIXBUS                  11 AM 12 PM 2 PM
--------------------------------------------------
''')

elif route == 3:
    print('''
--------------------------------------------------
            BUSES ON THIS ROUTE
--------------------------------------------------
1. VRL
2. ORANGE TRAVELS
3. FLIXBUS
--------------------------------------------------
''')

    choice = input('Do you want to know the timing yes/no : ')

    if choice == 'yes':
        print('''
--------------------------------------------------
            BUSES TIMING ON THIS ROUTE
--------------------------------------------------
1. VRL                      10 AM 11 AM 2 PM
2. ORANGE TRAVELS           11 AM 12 PM 3 PM
3. FLIXBUS                  11 AM 12 PM 2 PM
--------------------------------------------------
''')

else:
    print('Invalid Choice')
