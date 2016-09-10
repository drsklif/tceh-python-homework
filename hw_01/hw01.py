 # -*- coding: utf-8 -*-

import sys

__author__ = 'ildyakov'

if sys.version_info[0] == 2:
    read = raw_input
else:
    read = input

answers = 0
max_questions = 5

qStorage = [
    {
        "question": "Какое Имя у нашего преподавателя? ",
        "answer": "Никита"
    },
    {
        "question": "Какому языку программирования он нас учит? ",
        "answer": "python"
    },
    {
        "question": "Верно ли утверждение, что в питоне все является объектом? [y/n] ",
        "answer": "y"
    },
    {
        "question": "Какой тип данных есть в python2, но отсутствует в python3, int, или long? ",
        "answer": "long"
    },
    {
        "question": "Как записывается объект, означающий отсутствие значения? ",
        "answer": "None"
    },
    {
        "question": "Назовите стандартную функцию, не выполняющую никаких действий: ",
        "answer": "pass"
    },
    {
        "question": "Какой оператор возвращает длину строки? ",
        "answer": "len"
    },
    {
        "question": "С помощью какого оператора осуществляется деление нацело? ",
        "answer": "//"
    },
    {
        "question": "Какой литерал указывает на использование строки в формате Unicode, 'b', или 'u'? ",
        "answer": "u"
    },
    {
        "question": "Какая функция отвечает за инициализацию класса? ",
        "answer": "__init__"
    }
]

#Узнаем кто отвечает на вопросы
user = read('Представьтесь, пожалуйста!\n')

#обязательно нужно узнать имя
while not user:
    user = read('Мне нужно знать как вас зовут!\n')

#Никита знает гораздо больше чем ученики, значит сможет ответить на всё :)
if user.lower() in ['никита', 'соболев', 'nikita', 'nsobolev', 'n.sobolev', 'sobolevn', 'sobolev']:
    max_questions = len(qStorage)

print('Здравствуй %s, у меня есть несколько вопросов для тебя \n' % user)

points = 0
i = 0
while i < max_questions:
    current = qStorage[i]
    i += 1
    answer = read(current["question"])
    if answer == current["answer"]:
        points += 1
        if points % 3 == 0:
            print('Это правильный ответ и вы получаете право на 2 шкатулки! Всего правильных ответов: %d\n' % points)
        else:
            print('Это правильный ответ! Всего правильных ответов: %d\n' % points)
    else:
        print('Неправильный ответ\n')

if points == 0:
    print('Могу смело утверждать, что вы не справились с этим маленьким опросом :(\n\n')
else:
    print('Поздравляю, вы прошли этот маленький вопросник и набрали %d очков\n\n' % points)
