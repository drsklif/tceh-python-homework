 # -*- coding: utf-8 -*-

import sys
import csv
import uuid
from datetime import datetime

__author__ = 'ildyakov'

if sys.version_info[0] == 2:
    read = raw_input
else:
    read = input

answers = 0

with open('questions.csv', 'rt') as file:
    reader = csv.DictReader(file, delimiter='\t', fieldnames = ['question', 'answer'])
    qStorage = [row for row in reader]

max_questions = len(qStorage)

#Узнаем кто отвечает на вопросы
user = read('Представьтесь, пожалуйста!\n')

#обязательно нужно узнать имя
while not user:
    user = read('Мне нужно знать как вас зовут!\n')

session_id = uuid.uuid4()

log = [ '%s\t%s\tЗапущена сессия, пользователь %s' % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), session_id, user) ]

print('Здравствуй %s, у меня есть несколько вопросов для тебя \n' % user)

points = 0
i = 0
while i < max_questions:
    current = qStorage[i]
    i += 1
    answer = read(current["question"])
    to_log = '%s\t%s\t%s\t%s\t' % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), session_id, current["question"], answer)
    if answer == current["answer"]:
        points += 1
        if points % 3 == 0:
            print('Это правильный ответ и вы получаете право на 2 шкатулки! Всего правильных ответов: %d\n' % points)
        else:
            print('Это правильный ответ! Всего правильных ответов: %d\n' % points)
        to_log += 'Ответ верен. Правильных ответов: %d' %points
    else:
        print('Неправильный ответ\n')
        to_log += 'Ответ неверен. Правильных ответов: %d' %points
    log.append(to_log)

log.append('%s\t%s\tСессия завершена, пользователь %s\tВсего правильных ответов: %d' % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), session_id, user, points))

if points == 0:
    print('Могу смело утверждать, что вы не справились с этим маленьким опросом :(\n\n')
else:
    print('Поздравляю, вы прошли этот маленький вопросник и набрали %d очков\n\n' % points)

with open('log.txt', 'wt') as log_file:
    for s in log:
        log_file.write(s + '\n')
