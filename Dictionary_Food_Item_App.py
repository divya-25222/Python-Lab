#FOOD ITEM APP
print('Divya Joshi')
print('0863CS241063')

def show(menu):
    print('-'*30)
    print('Welcome to Cherry Hotel')
    print('-'*30)
    i=1
    for a,b in menu.items():
        print(f'{i} {a} ---> Rs {b}')
        i=i+1
    print('-'*30)


def order(menu):
    total=0
    order_list={}               
    while True:
        items = input('Order from the menu: ')
        if items == 'e':
            break
        if items not in menu:
            print('items not found')
            continue

        qty=int(input("Enter the quantity: "))
        amount = menu[items]*qty

        if items not in order_list:
            order_list[items]= {'qty':qty , 'amount':amount}                               #nested
            print('Added')
            total = total + amount
        else:
            order_list[items]['qty'] += qty
            order_list[items]['amount'] += amount

    print('*'*30)
    print('BILL')
    print('*'*30)
    print(f'Items          Quantity          Amount')
    for a,b in order_list.items():
        print(f"{a} qty - {b['qty']} Rs {b['amount']}")
    print('Total',total)
    print('*'*30)
    print('VISIT AGAIN')
    print('*'*30)


    




def main_menu():
    menu={
        'Samosa':20,
        'Kachori':20,
        'Poha':15,
        'Jalebi':40,
        'Tea':10,
        'Coffee':25,
        'Vada':30
    }
    show(menu)                         #To iterate show
    order(menu)

main_menu()