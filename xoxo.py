field = {'A1': chr(32), 'A2': chr(32), 'A3': chr(32), 'B1': chr(32), 'B2': chr(32), 'B3': chr(32), 'C1': chr(32),
         'C2': chr(32), 'C3': chr(32)}
# field= {'A1':0,'A2':0, 'A3':0,'B1':0,'B2':0, 'B3':0,'C1':0,'C2':0, 'C3':0}
# field=['']*9
print('')
player1mark = None
player2mark = None
player2move = None
player1move = None
victory = 0

def check_player_mark():
    global player1mark, player2mark
    player1mark = input('Игрок 1, выберите Х или O?')
    player1mark=player1mark.upper()
    if player1mark !='X'or player1mark !='O':
        player1mark = 'X'
        player2mark = 'O'
        print ('Нужно было выбрать Х или 0. Теперь Игрок 1 играет за Х')

    if player1mark == 'X':
        player2mark = 'O'
    else:
        player2mark = 'X'

# player1move=input('Игрок 1: ')
def pl1(player1move):
    move_status=True
    while move_status:
        player1move = input('Игрок 1, введите координаты поля: ').upper()
        if player1move in field:
            move_status=False
        else:
            print('!!!!!!!!!')
            print('Введите корректные координаты поля.')
            move_status=True

    field[player1move] = player1mark



def pl2(player2move):
    move_status=True
    while move_status:
        player2move = input('Игрок 2, введите координаты поля: ').upper()
        if player2move in field:
            move_status=False
        else:
            print('!!!!!!!!!')
            print('Введите корректные координаты поля.')
            move_status=True


    field[player2move] = player2mark



def printField():
    print('______________')
    print('  1    2    3  ')
    print(f'''A| {field['A1']} | {field['A2']} | {field['A3']} |''')
    print(f'''B| {field['B1']} | {field['B2']} | {field['B3']} |''')
    print(f'''C| {field['C1']} | {field['C2']} | {field['C3']} |''')
    print('______________')



check_player_mark()

while victory != 1 or victory != 2:

    printField()
    pl1(player1move)
    if field['A1'] == field['A2'] == field['A3'] == player1mark:
        victory = 1
        break
    elif field['B1'] == field['B2'] == field['B3'] == player1mark:
        victory = 1
        break
    elif field['C1'] == field['C2'] == field['C3'] == player1mark:
        victory = 1
        break
    elif field['A1'] == field['B1'] == field['C1'] == player1mark:
        victory = 1
        break
    elif field['A2'] == field['B2'] == field['C2'] == player1mark:
        victory = 1
        break
    elif field['A3'] == field['B3'] == field['C3'] == player1mark:
        victory = 1
        break
    elif field['A1'] == field['B2'] == field['C3'] == player1mark:
        victory = 1
        break
    elif field['A3'] == field['B2'] == field['C1'] == player1mark:
        victory = 1
        break

    printField()
    pl2(player2move)
    if field['A1'] == field['A2'] == field['A3'] == player2mark:
        victory = 2
        break
    elif field['B1'] == field['B2'] == field['B3'] == player2mark:
        victory = 2
        break
    elif field['C1'] == field['C2'] == field['C3'] == player2mark:
        victory = 2
        break
    elif field['A1'] == field['B1'] == field['C1'] == player2mark:
        victory = 2
        break
    elif field['A2'] == field['B2'] == field['C2'] == player2mark:
        victory = 2
        break
    elif field['A3'] == field['B3'] == field['C3'] == player2mark:
        victory = 2
        break
    elif field['A1'] == field['B2'] == field['C3'] == player2mark:
        victory = 2
        break
    elif field['A3'] == field['B2'] == field['C1'] == player2mark:
        victory = 2
        break

printField()
print(victory)