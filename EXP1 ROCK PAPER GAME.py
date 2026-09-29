print('Divya Joshi')
print('0863CS241063')

u1 = input('PLAYER 1 Enter name: ')
u2 = input('PLAYER 2 Enter name: ')

c1 = input(f'{u1} Enter choice Rock/Paper/Scissor: ')
c2 = input(f'{u2} Enter choice Rock/Paper/Scissor: ')

# DRAW
if c1 == c2:
    print("IT'S DRAW!!!")

# U2 WINS
elif ((c2 == 'Paper' and c1 == 'Rock') or
      (c2 == 'Scissor' and c1 == 'Paper') or
      (c2 == 'Rock' and c1 == 'Scissor')):
    print(f'{u2} WON')

# U1 WINS
elif ((c1 == 'Paper' and c2 == 'Rock') or
      (c1 == 'Scissor' and c2 == 'Paper') or
      (c1 == 'Rock' and c2 == 'Scissor')):
    print(f'{u1} WON')

else:
    print('INVALID CHOICE!')
