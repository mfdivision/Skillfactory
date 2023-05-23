
# словарь игрового поля. Можно было и списком, но захотел сделать именно через словарь ))
field = {'A1': chr(32), 'A2': chr(32), 'A3': chr(32), 'B1': chr(32), 'B2': chr(32), 'B3': chr(32), 'C1': chr(32),
         'C2': chr(32), 'C3': chr(32)}

player1mark = None
player2mark = None
player2move = None
player1move = None
victory = 0
moves_counter=1

# Игрок №1 выбирает крестик или нолик, проверяем выбранную букву и если это не Х или О,
# назначаем букву прнудительно.
def check_player_mark():
    global player1mark, player2mark
    player1mark = input('Игрок 1, выберите букву: Х или O?').upper()
    if player1mark!='X' and player1mark!='O':
        player1mark = 'X'
        player2mark = 'O'
        print ('Нужно было выбрать Х или O. Теперь Игрок 1 играет за Х')
    if player1mark == 'X':
        player2mark = 'O'
    else:
        player2mark = 'X'


# Ход первого игрока. Проверка корректного ввода коорднат, запись хода в field
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


#Аналогично для второго игрока
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


# отрисовка поля
def printField():
    print('______________')
    print('  1    2    3  ')
    print(f'''A| {field['A1']} | {field['A2']} | {field['A3']} |''')
    print(f'''B| {field['B1']} | {field['B2']} | {field['B3']} |''')
    print(f'''C| {field['C1']} | {field['C2']} | {field['C3']} |''')
    print('______________')


# тело програмы

check_player_mark()

# проверка выигрыша
while victory != 1 or victory != 2:
    print()
    print('--------------------------')
    print(f'ход №{moves_counter}')
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
    moves_counter += 1
    if moves_counter == 10:
        print('Ничья')
        break

    print()
    print('--------------------------')
    print(f'ход №{moves_counter}')

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
    moves_counter+=1
    if moves_counter == 10:
        print('Ничья')
        break


printField()

# поздравляем победителя
if victory==1:
    print(f'Игрок 1, поздравляю с победой на {moves_counter} ходу!')

elif victory==2:
    print(f'Игрок 2, поздравляю с победой на {moves_counter} ходу!')



