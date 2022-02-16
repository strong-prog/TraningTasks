"""
Обратные крестики-нолики на поле 10 x 10 с правилом «Пять в ряд» – проигрывает тот,
у кого получился вертикальный, горизонтальный или диагональный ряд из пяти своих фигур (крестиков/ноликов).
"""

import random

BOARD = list(range(1, 101))

"""Выбор игровой роли: крестик или нолик"""

player = ''
computer = ''
while player not in ('X', 'O'):
    player = input('Вы хотите играть за красный X или желтый O?').upper()

if player == 'X':
    computer = 'O'
else:
    computer = 'X'


def draw_board(board):
    """Генерация игрового поля"""
    cell = 0
    print('-' * 71)
    for _ in range(10):
        print('|', end='')
        for _ in range(10):
            if str(board[cell]) == 'X':
                print(f'\033[31m {str(board[cell]).center(4)}', end='')
            elif str(board[cell]) == 'O':
                print(f'\033[33m {str(board[cell]).center(4)}', end='')
            else:
                print(f'\033[34m {str(board[cell]).center(4)}', end='')
            print(f'\033[0m {"|"}', end='')
            cell += 1
        print()
        print('-' * 71)


def player_step(board, token):
    """Выбор игрока следующей ячейки для хода и проверка того можно ли поставить маркер в эту ячейку"""

    while True:
        step = input(f'Куда поставим {token}?')
        try:
            step = int(step)
        except:
            print('Некорректный ввод. Вы уверены, что ввели число?')
            continue
        if 1 <= step <= 100:
            if str(board[step - 1]) not in 'XO':
                board[step - 1] = token
                break
            else:
                print('Эта клетка уже занята! Введите свободное число от 1 до 25, чтобы походить!')
        else:
            print('Некорректный ввод. Введите свободное число от 1 до 25, чтобы походить!')


def computer_step(board, token):
    """Примитивный выбор компьютера следующей ячейки для хода и проверка того можно ли поставить маркер в эту ячейку"""
    while True:
        step = random.randint(1, 100)
        if str(board[step - 1]) not in 'XO':
            board[step - 1] = token
            break


def check_lose(board):
    """Проверка проиграл ли игрок с указанным маркером игру"""

    lines = ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), (10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
             (20, 21, 22, 23, 24, 25, 26, 27, 28, 29), (30, 31, 32, 33, 34, 35, 36, 37, 38, 39),
             (40, 41, 42, 43, 44, 45, 46, 47, 48, 49), (50, 51, 52, 53, 54, 55, 56, 57, 58, 59),
             (60, 61, 62, 63, 64, 65, 66, 67, 68, 69), (70, 71, 72, 73, 74, 75, 76, 77, 78, 79),
             (80, 81, 82, 83, 84, 85, 86, 87, 88, 89), (90, 91, 92, 93, 94, 95, 96, 97, 98, 99),
             (0, 10, 20, 30, 40, 50, 60, 70, 80, 90), (1, 11, 21, 31, 41, 51, 61, 71, 81, 91,),
             (2, 12, 22, 32, 42, 52, 62, 72, 82, 92), (3, 13, 23, 33, 43, 53, 63, 73, 83, 93),
             (4, 14, 24, 34, 44, 54, 64, 74, 84, 94), (5, 15, 25, 35, 45, 55, 65, 75, 85, 95),
             (6, 16, 26, 36, 46, 56, 66, 76, 86, 96), (7, 17, 27, 37, 47, 57, 67, 77, 87, 97),
             (8, 18, 28, 38, 48, 58, 68, 78, 88, 98), (9, 19, 29, 39, 49, 59, 69, 79, 89, 99),
             (0, 11, 22, 33, 44, 55, 66, 77, 88, 99), (9, 18, 27, 36, 45, 54, 63, 72, 81, 90))

    for ls in lines:
        line = (board[ls[0]], board[ls[1]], board[ls[2]], board[ls[3]], board[ls[4]],
              board[ls[5]], board[ls[6]], board[ls[7]], board[ls[8]], board[ls[9]])
        if line.count('X') == 5 or line.count('O') == 5:
            return True
    return False


def check_nobody(board):
    """Определяет имеется ли на игровой доске оба маркера: X и O"""

    if len(set(board)) == 2:
        return True
    return False


def check_finish(board, player):
    """Проверка, завершена ли игра"""

    if check_lose(board):
        print(f'Игрок "{player}" проиграл!')
        return True

    if check_nobody(board):
        print('Игра завершилась вничью.')
        return True

    return False


def switch_player(mark):
    """Переключение роли игрока для смены очереди для хода"""

    return computer if mark == player else player


def clear_screen():
    """Очищение игрового экрана добавлением пустых строк"""

    print('\n' * 5)


CURRENT_PLAYER = player

while True:
    draw_board(BOARD)
    print(f'Ход игрока "{CURRENT_PLAYER}":')
    if CURRENT_PLAYER == player:
        player_step(BOARD, CURRENT_PLAYER)
    else:
        computer_step(BOARD, CURRENT_PLAYER)

    if check_finish(BOARD, CURRENT_PLAYER):
        draw_board(BOARD)
        break
    else:
        CURRENT_PLAYER = switch_player(CURRENT_PLAYER)
    clear_screen()
