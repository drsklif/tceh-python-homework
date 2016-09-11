# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'X'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = list(range(1,16))
    field.append(EMPTY_MARK)
    
    move_keys = list(MOVES.keys())
    max_steps = 2000    #вычислено эмпирическим путем, дает более-менее нормальное перемешивание игрового поля
    steps = 0

    #перемешивание осуществляется выполнением определенного количества случайных шагов
    while steps < max_steps:
        try:
            step = random.choice(move_keys)
            field = perform_move(field, step)
            steps += 1
        except IndexError:
            continue

    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    print(chr(27) + "[2J") #Очищаем экран (гораздо удобнее играть, когда поле остается на одном и том же месте)

    #для наглядности нужна красивая доска
    for i in range(0, len(field), 4):
        if i == 0:
            print('\u2554\u2550\u2550\u2566\u2550\u2550\u2566\u2550\u2550\u2566\u2550\u2550\u2557') #рисуем верхнюю границу поля
        else:
            print('\u2560\u2550\u2550\u256c\u2550\u2550\u256c\u2550\u2550\u256c\u2550\u2550\u2563') #рисуем промежуточные линии поля
        print('\u2551{:2s}\u2551{:2s}\u2551{:2s}\u2551{:2s}\u2551'.format(*map(str, field[i:i+4]))) #выводим текущую строку
    print('\u255a\u2550\u2550\u2569\u2550\u2550\u2569\u2550\u2550\u2569\u2550\u2550\u255d')         #рисуем нижнюю границу


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    field_finished = list(range(1,16))
    field_finished.append(EMPTY_MARK)
    return field == field_finished


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    move = MOVES[key]
    position = field.index(EMPTY_MARK)
    next_position = position + move

    if (position % 4 == 0 and move == -1) \
        or ((position + 1) % 4 == 0 and move == 1) \
        or (next_position < 0) \
        or (next_position > len(field)):
        raise IndexError('Недопустимый ход!')

    field[position], field[next_position] = field[next_position], field[position]

    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    moves = MOVES.keys()
    msg = '\nКакой будет ваш следующий ход? Допустимые варианты: {} '.format(", ".join(moves))
    choice = input(msg)

    while choice not in moves:
        choice = input(msg)
    return choice


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    field = shuffle_field()
    print_field(field)

    steps = 0

    while not is_game_finished(field):
        try:
            move = handle_user_input()
            steps += 1
            field = perform_move(field, move)
            print_field(field)
        except IndexError as ex:
            print(ex)

    print('Вы победили! Затрачено ходов: {}'.format(steps))

if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    try:
        main()
    except KeyboardInterrupt:
        print('\nshutting down')
