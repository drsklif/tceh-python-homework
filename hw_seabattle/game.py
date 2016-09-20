# -*- coding: utf-8 -*-

from models import (
    Storage,
    Player,
    Field,
    Ship,
    Coord,
)

from utils import (
    get_input_function,
    clear_screen,
)

__author__ = 'aildyakov'

class Game(object):
    """Ядро игры"""
    __obj = None

    input_function = get_input_function()

    storage = Storage()

    @classmethod
    def __new__(cls, *args):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    @classmethod
    def start(cls, *args):
        """запуск игры"""
        clear_screen()

        #инициализация 2-х игроков
        while (len(cls.storage.players) < 2):
            player = cls.construct_player(len(cls.storage.players) + 1)
            cls.storage.players.append(player)
            clear_screen()

        player = cls.storage.players[0]
        enemy = cls.storage.players[1]
        if player is None or enemy is None:
            raise Exception('Игроки не были созданы!')

        hit_result_message = ''
        while True:
            try:
                if hit_result_message != '':
                    clear_screen()
                    print(hit_result_message + '\n')
                    hit_result_message = ''

                cls.print_field(enemy.field.data, True)
                coord = cls.get_coords('Игрок {}, Ваш ход: '.format(player.name))
                hit = enemy.hit(coord)
                if hit == 2:
                    if enemy.total_hits() == 0:
                        print('Игрок {} победил!'.format(player.name))
                        return
                    hit_result_message = 'Игрок {} потопил корабль противника!!! Можете сделать еще один выстрел!'.format(player.name)
                elif hit == 1:
                    hit_result_message = 'Игрок {} попал по кораблю противника!!! Можете сделать еще один выстрел!'.format(player.name)
                else:
                    hit_result_message = 'Игрок {} промахнулся и ход переходит к {}!!!'.format(player.name, enemy.name)
                    player, enemy = enemy, player

            except Exception as e:
                clear_screen()
                print(e + '\n')


    @staticmethod
    def get_name(number):
        """
        Запрос имени игрока
        number - номер игрока
        """
        while True:
            name = Game.input_function('Игрок № {}, введите свое имя: '.format(number))
            if name == '':
                continue
            return name

    @staticmethod
    def get_coords(input_message):
        """
        Запрос координат
        input_message - отображаемое сообщение
        """
        while (True):
            user_input = Game.input_function(input_message)
            try:
                coords = user_input.split(",")
                if len(coords) != 2:
                    raise Exception("Некорректные данные. Слишко много, или мало координат.")

                return Coord(int(coords[0])-1, int(coords[1])-1)

            except ValueError:
                print("Некорректные данные. Для ввода допустимы только цифры")
            except Exception as e:
                print(e)
            print()

    @staticmethod
    def get_direction(input_message):
        """
        Запрос ориентации корабля
        input_message - отображаемое сообщение
        """
        while (True):
            user_input = Game.input_function(input_message)
            try:
                if user_input not in ('В', 'Г'):
                    raise Exception("Некорректные данные.");
                return user_input
            except Exception as e:
                print(e)
                print()

    def get_printable_row(row, hidden):
        """
        Возвращает представление строки поля
        row - строка (данные)
        hidden - прятать корабли, или нет
        """
        mask = [' ', ' ', 'X', '*', ' '] if hidden else [' ', '$', 'X', '*', ' ']
        r = []
        for i in row:
            r.append(mask[i])
        return r


    @staticmethod
    def print_field(field, hidden):
        """
        Печать игрового поля
        field - поле
        hidden - прятать корабли, или нет
        """
        print(' '*6 + ('{:4}'*10).format(*tuple(range(1, Storage.field_size + 1))))
        print(' '*7 + '-'*41)
        for y in range(Storage.field_size):
            print('   {:3} |'.format(y+1) + (' {} |'*10).format(*tuple(Game.get_printable_row(field[y],hidden))))
            print(' '*7 + '-'*41)

    @classmethod
    def construct_player(cls, *args):
        """Создание игрока"""
        
        name = cls.get_name(args[0])
        player = Player(name)

        print('Привет, {}, давай заполним твое поле'.format(name))

        for s in cls.storage.ships:
            i = 0
            while (i < s.quantity):
                try:
                    #запрашиваем левую верхнюю координату корабля
                    coord1 = cls.get_coords('Введите координаты для корабля {} № {} в формате "столбец,строка":'.format(s.name, i + 1))
                    coord2 = Coord(coord1.x, coord1.y)

                    #запрашиваем способ расположения корабля только для многоклеточных
                    if s.size > 1:
                        direction = cls.get_direction('Укажите расположение корабля, вертикальное (В), или горизонтальное (Г): [В|Г]')
                        if direction == 'В':
                            coord2.y += s.size
                        elif direction == 'Г':
                            coord2.x += s.size

                    #создаем корабль игрока
                    ship = Ship(s.name, s.size, coord1, coord2)
                    player.add_ship(ship)
                    i += 1
                    clear_screen()
                    Game.print_field(player.field.data, False)

                except Exception as e:
                    print(e)

        player.field.clean_aura()
        return player
