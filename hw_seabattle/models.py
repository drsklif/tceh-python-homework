# -*- coding: utf-8 -*-

__author__ = 'aildyakov'

class ShipBase(object):
    """
    Базовый класс для кораблей.
    Хранит название, размер и количество кораблей этого типа на поле
    Можно попробовать не хранить количество, а рассчитывать по формуле 5 - размер,
    но это не будет работать, если правила игры изменятся
    """
    def __init__(self, name, size, quantity):
        self.name = name
        self.size = size
        self.quantity = quantity

class Storage(object):
    """
    База данных игры, хранит настройки, игроков и их поля
    """
    #для реализации синлтона
    __obj = None

    #список игроков
    players = []

    #настройки кораблей
    ships = [
        ShipBase('Линкор', 4, 1),
        ShipBase('Крейсер', 3, 2),
        ShipBase('Эсминец', 2, 3),
        ShipBase('Катер', 1, 4),
    ]

    #размер игрового поля
    field_size = 10

    #реализцем синглтон
    @classmethod
    def __new__(cls, *args):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
            cls.players = []
        return cls.__obj

class Coord(object):
    """
    Координаты в классическом декартовом пространстве
    x - позиция по горизонтали (КОЛОНКА)
    y - позиция по вертикали (СТРОКА)
    """
    def __init__(self, x, y):
        if x < 0 or x >= Storage.field_size or y < 0 or y >= Storage.field_size:
            raise Exception('Нельзя создать координату, выходящую за границу поля!')
        self.x = x
        self.y = y


class Player(object):
    """
    Игрок
    Храним имя, поле и список кораблей
    """
    def __init__(self, name):
        self.name = name
        self.field = Field(Storage.field_size)
        self.ships = []

    def __str__(self):
        return self.name

    #добавление корабля на доску
    def add_ship(self, ship):
        self.field.place_ship(ship)
        self.ships.append(ship)

    #суммарное количество жизней всех кораблей игрока
    def total_hits(self):
        if len(self.ships) == 0:
            return 0
        return sum([s.hits for s in self.ships])

    #выстрел по кораблям игрока
    def hit(self, coord):
        cell_value = self.field.data[coord.y][coord.x]
        if cell_value == 0:
            self.field.data[coord.y][coord.x] = 3
            return 0
        elif cell_value in (2, 3):
            raise Exception('Некорректный ход, уточните координаты!')

        ship = self.find_ship_by_coord(coord)
        if ship is None:
            #кто найдет как сюда попасть, тому респект!
            raise Exception('Какая-то фигня. Вроде и не промах, но корабля по таким координатам нет!')

        ship.hits -= 1
        self.field.data[coord.y][coord.x] = 2

        return 2 if ship.hits == 0 else 1

    #поиск корабля по координате
    def find_ship_by_coord(self, coord):
        selected_ship = None
        for ship in self.ships:
            if (coord.x == ship.coord1.x and ship.coord1.y <= coord.y <= ship.coord2.y) \
                or (coord.y == ship.coord1.y and ship.coord1.x <= coord.x <= ship.coord2.x):
                selected_ship = ship
                break

        return selected_ship



class Field(object):
    """Игровое поле"""
    def __init__(self, size):
        self.size = size
        self.data = []

        for i in range(size):
            row = [0 for _ in range(size)]
            self.data.append(row)

    #размещение корабля на поле. если что-то не так, вызываем эксепшен с описанием
    def place_ship(self, ship):
        #проверяем возможность горизонтального расположения
        not_empty_field_message = 'Невозможно расположить корабль, т.к. поле в указанных координатах уже занято!'
        #print('Получены координаты корабля: ({}, {}), ({}, {})'.format(ship.coord1.x, ship.coord1.y, ship.coord2.x, ship.coord2.y))

        if ship.coord1.y == ship.coord2.y and sum(self.data[ship.coord1.y][ship.coord1.x:ship.coord2.x]) > 0:
            raise Exception(not_empty_field_message)

        if ship.coord1.x == ship.coord2.x:
            for i in range(ship.coord1.y, ship.coord2.y):
                if self.data[i][ship.coord1.x] > 0:
                    raise Exception(not_empty_field_message)

        #вспомогательная функция для установки на поле палубы корабля и его "ауры"
        def init_ship_cell(field, coord):
            field[coord.y][coord.x] = 1
            for x in range(coord.x - 1, coord.x + 2):
                if x < 0 or x >= Storage.field_size:
                    continue
                for y in range(coord.y - 1, coord.y + 2):
                    if y < 0 or y >= Storage.field_size:
                        continue
                    if field[y][x] == 0:
                        field[y][x] = 4
            return field

        #для горизонтально-ориентированных кораблей
        if ship.coord1.y == ship.coord2.y:
            for x in range(ship.coord1.x, ship.coord2.x):
                self.data = init_ship_cell(self.data, Coord(x, ship.coord1.y))

        #для вертикально-ориентированных кораблей
        if ship.coord1.x == ship.coord2.x:
            for y in range(ship.coord1.y, ship.coord2.y):
                self.data = init_ship_cell(self.data, Coord(ship.coord1.x, y))

        #для однопалубников
        if ship.size == 1:
            self.data = init_ship_cell(self.data, Coord(ship.coord1.x, ship.coord1.y))

    #очистка поля от ауры кораблей
    def clean_aura(self):
        for y in range(Storage.field_size):
            for x in range(Storage.field_size):
                if self.data[y][x] == 4:
                    self.data[y][x] = 0

class Ship(ShipBase):
    """Корабль и его параметры"""
    def __init__(self, name, size, coord1, coord2):
        super(Ship, self).__init__(name, size, 0)
        self.coord1 = coord1
        self.coord2 = coord2
        self.hits = size
