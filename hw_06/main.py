# -*- coding: utf-8 -*-

"""
Main file. Contains program execution logic.
"""

from utils import (get_input_function, clear_screen)

from storage import(MarkItem, SchoolLog)

import re

__author__ = 'aildyakov'


def show_marks(*args, **kwargs):
    school_log = args[0]
    marks = None

    if kwargs['name'] is None:
        marks = school_log.get_all_marks()
    else:
        marks = school_log.get_marks_by_name_and_class(kwargs['name'], kwargs['class_name'])

    if marks is None or len(marks) == 0:
        print('No marks!')
    else:
        print(*marks, sep='\n')


def add_mark(*args, **kwargs):
    school_log = args[0]
    new_mark = MarkItem(kwargs['name'], kwargs['class_name'], kwargs['mark'], kwargs['lesson'])
    school_log.add_mark(new_mark)
    print('mark added: {}'.format(new_mark))


def exit(*args, **kwargs):
    raise(KeyboardInterrupt)


def main():
    """
    Main method, works infinitelly until exit command.
    Or hits `Ctrl+C` in the console.
    """

    try:
        clear_screen()

        school_log = SchoolLog()

        commands = {
            'show': show_marks,
            'add': add_mark,
            'exit': exit,
        }

        command_pattern = r'^(?P<command>\w+)\s(all|(?P<name>.*)\sfrom\s(?P<class_name>\w+))\s(marks|got\s(?P<mark>\w)\son\s(?P<lesson>.*)\slesson)$'

        while True:
            try:
                cmd = get_input_function()("Type command or 'exit' to close application: ")

                if cmd == 'exit':
                    commands[cmd]()

                match = re.match(command_pattern, cmd)
                command_values = match.groupdict()

                if not match or command_values['command'] not in commands:
                    print('Bad command!')
                    continue

                commands[command_values['command']](school_log, **command_values)

            except (ValueError, IndexError):
                print('Bad input, try again.')

    except KeyboardInterrupt:
        school_log.save()
        print('\nGood bye!')

if __name__ == '__main__':
    main()
